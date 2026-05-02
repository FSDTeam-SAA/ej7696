from asset.core.prompts import GenQuestionPrompt
from asset.core.clear_data import CleanData
from asset.core.process_gemi3_response import get_text
from asset.service.model_output import ModelOutput

"""
def GetModelResponse(model, ex_name, sheet_content, 
                     knowledge_content, n_question):
    
    prompt = GenQuestionPrompt(ex_name=ex_name, sheet_content=sheet_content, 
                            knowledge_content=knowledge_content, n_question=n_question)
        
    response = model.invoke(prompt).content

    if model.model.startswith('gemini-3'):
            response = get_text(response)
        
    response = CleanData(response)

    return response

"""


def GetModelResponse(model, ex_name, sheet_content, 
                     knowledge_content, n_question):
                     #, exam_type):

    prompt = GenQuestionPrompt(ex_name=ex_name, sheet_content=sheet_content, 
                               knowledge_content=knowledge_content, 
                               n_question=n_question)#, exam_type=exam_type)
    
    #response = model.invoke(prompt).content
    try:
        status, response = ModelOutput(model, prompt)

        if not status:
            return status, response
        status = True
        """print('=' * 80)
        print(response)
        print('=' * 80)"""

        if model.model.startswith('gemini-3'):
            response = get_text(response)

        response = CleanData(response)
        return status, response
    except Exception as ex:
        status = False
        response = str(ex)
        print('=' * 100)
        print(str(ex))
        print('=' * 100)
        return status, response