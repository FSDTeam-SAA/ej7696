from email.mime import text
import os
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from asset.hyperparameters import hyper
from fastapi.responses import JSONResponse, FileResponse
from asset.config.gen_model import LoadGenModel
from asset.config.openai_model import LoadOpenAIModel
from asset.core.clear_data import CleanData
from asset.core.process_gemi3_response import get_text
#from asset.core.prompts import GenQuestionPrompt#, GenBookPrompt
from asset.service.check_question import CheckQuestionCount
from asset.service.get_model_response import GetModelResponse
from asset.service.merge_data import MergeData


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Anyone can access
    allow_credentials=True,
    allow_methods=["*"],          # ALL methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],   
)


load_dotenv()

# model = LoadGenModel()
model = LoadOpenAIModel()
print('=' * 80)
print("Initial Model Name:", model.model)
print('=' * 80)

# print('-' * 80)
# print(' ' * 25, "API keys loading")
# print('-' * 80)
# print("Gemini Key Loaded:", os.environ.get('GOOGLE_API_KEY'))
# print("OpenAI Key Loaded:", os.environ.get('OPENAI_API_KEY'))
# print('-' * 80)

#model = LoadOpenAIModel()
@app.post('/api/config-model/')
async def config_model(model_name = Form(), temp: float =Form(1)):
    global model 
    try:
        if 'gemini' in model_name.lower():
            model = LoadGenModel(model_name=model_name, temp=temp)
            text = f'Model configured to {model.model} with temperature {model.temperature}'
        elif 'gpt' in model_name.lower() or 'openai' in model_name.lower():
            model = LoadOpenAIModel(model_name=model_name, temp=temp)
            text = f'Model configured to {model.model_name} with temperature {model.temperature}'
        
        message = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'text': text
            }
        )
        return message
    except Exception as ex:
        message = JSONResponse(
            status_code=500,
            content={
                'status': False,
                'status_code': 500,
                'text': str(ex)
            }
        )
        return message

@app.get('/api/model-name/')
async def get_model_name():
    global model 
    try:
        text = model.model if hasattr(model, 'model') else model.model_name
        message = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'text': text
            }
        )
        return message
    except Exception as ex:
        message = JSONResponse(
            status_code=500,
            content={
                'status': False,
                'status_code': 500,
                'text': str(ex)
            }
        )
        return message
 

@app.post('/api/gen-question/')
async def generate_question(ex_name= Form(), 
                            sheet_content=Form(), 
                            knowledge_content=Form(), 
                            n_question: int =Form()):
                            #exam_type: str = Form()):
    try:
        #prompt = GenQuestionPrompt(ex_name=ex_name, sheet_content=sheet_content, knowledge_content=knowledge_content, n_question=n_question)
        
        #response = model.invoke(prompt).content
        #print(response)
        #if type(response) != list:
            #response = CleanData(response)
        status, text = GetModelResponse(model=model, ex_name=ex_name,
                                    sheet_content=sheet_content,
                                   knowledge_content=knowledge_content,
                                   n_question=n_question)
                                   #exam_type=exam_type)
        
        if not status:
            message = JSONResponse(
                status_code=500,
                content={
                    'status': False,
                    'status_code': 500,
                    'text': text 
                }
            )
            return message
        

        s_count = 0
        while not status and s_count < 3:
            print(f"Retrying... Attempt {s_count + 1}")
            status, text = GetModelResponse(model=model, ex_name=ex_name,
                                        sheet_content=sheet_content,
                                       knowledge_content=knowledge_content,
                                       n_question=n_question)
                                       #exam_type=exam_type)
            s_count += 1
        
        s_count = 0
        
        count, response = CheckQuestionCount(response=text, n_question=n_question)

        if count != 0:
            new_data = GetModelResponse(model=model, ex_name=ex_name,
                                        sheet_content=sheet_content,
                                        knowledge_content=knowledge_content,
                                        n_question=count)
                                        #exam_type=exam_type)
            
            response = MergeData(previous=text, new=new_data)

        print('=' * 80)
        print("Current Model Name in API:", model.model)
        print('=' * 80)
        """if model.model.startswith('gemini-3'):
            response = get_text(response)
        
        response = CleanData(response)
        """
        #print(response)


        print('x' * 100)
        print("Number of question generated:", len(response))
        print('x' * 100)

        
        message = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'text': response 
            }
        )
        return message
    
    except Exception as ex:
        message = JSONResponse(
            status_code=500,
            content={
                'status': False,
                'status_code': 500,
                'text': str(ex) 
            }
        )

        return message

"""
out_dir = hyper['output_dir']
os.makedirs(out_dir, exist_ok=True)

@app.post('/api/create-book/')
async def create_book(ex_name, sheet_content, knowledge_content):
    prompt = GenBookPrompt(ex_name=ex_name, sheet_content=sheet_content, 
                           knowledge_content=knowledge_content)
    
    try:
        response = model.invoke(prompt).content
        
        serial = len(os.listdir(out_dir))+1
        path = os.path.join(out_dir, f'response_{serial}.txt')
        with open(path, 'w') as file:
            file.write(response)
        
        message = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'text': response
            }
        )
        return message
    
    except Exception as ex:
        message = JSONResponse(
            status_code=500,
            content={
                'status': False,
                'status_code': 500,
                'text': str(ex)
            }
        )
        return message


@app.get('/api/view-responses/')
async def gen_question():
    dirs = [os.path.join(out_dir, p) for p in os.listdir(out_dir)]

    print(dirs)
    response = []
    for d in dirs:
        with open(d, 'r') as f:
            data = f.read()
        response.append(data)


    message = JSONResponse(
        status_code=200,
        content={
            'status': True,
            'status_code': 200,
            'text': response
        }
    )

    return message


@app.post('/api/load_book/')
def load_book():
    f_path = r'data\response\response_1.txt'
    f_name = os.path.split(f_path)[-1]
    return FileResponse(
        path=f_path,
        media_type='text',
        filename=f_name
    )

"""