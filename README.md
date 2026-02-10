**Repository Description**  
- FastAPI service that generates exam‑preparation material using generative AI models.  
- Integrates LangChain adapters for Gemini and OpenAI chat models.  
- Utilities for prompt construction, response cleaning, and question validation.  
- Centralized configuration for model parameters and data paths.  
- Core modules handle JSON sanitization and output formatting.  
- Service layer provides functions to invoke models, merge results, and check question counts.  
- Example script demonstrates end‑to‑end Gemini‑2.5‑flash workflow.  
- Environment variables loaded via `dotenv` for API keys.  
- Dependencies listed in `requirements.txt`.  

**Run Instructions**  
a. Clone the repository: 
```bash
git clone <repo-url>
```  
b. Create a virtual environment: 
```bash
py -3.12 -m venv venv
```  
c. Activate the virtual environment:  
```bash
On Windows: venv\Scripts\activate`  
On Unix/Mac: source venv/bin/activate
``` 
d. Install dependencies: 
```bash
pip install -r requirements.txt
```
e. Run only the important files (ignore non‑essential files):  
```bash
    uvicorn main:app --host 0.0.0.0 --port 10000
```

**Folder Structure**  
```
repo
|--- .gitignore
|--- .python-version
|--- main.py
|--- test.py
|--- asset
    |--- hyperparameters.py
    |--- config
    |   |--- gen_model.py
    |   |--- openai_model.py
    |--- core
    |   |--- clear_data.py
    |   |--- output_format.py
    |   |--- process_gemi3_response.py
    |   |--- prompts.py
    |--- service
        |--- check_question.py
        |--- get_model_response.py
        |--- merge_data.py
        |--- model_output.py
```  

**File Overview**  
- `.gitignore`: excludes env files, virtual environment, and `__pycache__` directories.  
- `.python-version`: specifies required Python version 3.12.  
- `main.py`: FastAPI entry point; loads env, configures CORS, instantiates generative model.  
- `test.py`: demo script using Asset library with Gemini‑2.5‑flash model; builds prompt, invokes model, prints result.  
- `asset/hyperparameters.py`: defines `hyper` dict with `input_dir` and `output_dir` paths.  
- `asset/config/gen_model.py`: `LoadGenModel` factory creates Gemini chat model with configurable parameters.  
- `asset/config/openai_model.py`: `LoadOpenAIModel` factory creates OpenAI `ChatOpenAI` client.  
- `asset/core/clear_data.py`: `CleanData` sanitizes raw JSON strings and returns deserialized object.  
- `asset/core/output_format.py`: defines `out_temp` exam‑question template and `DIFFICULTY_MIX_CONFIG` presets.  
- `asset/core/process_gemi3_response.py`: extracts clean text from Gemini API response list.  
- `asset/core/prompts.py`: builds LangChain prompt template for exam material generation.  
- `asset/service/check_question.py`: `CheckQuestionCount` validates and adjusts generated question list to desired count.  
- `asset/service/get_model_response.py`: builds prompt, calls model, extracts & cleans response, returns status and data.  
- `asset/service/merge_data.py`: `MergeData` extends previous list with new items (returns `None`).  
- `asset/service/model_output.py`: invokes model with prompt, returns `(status, response)` tuple with error handling.  