from langchain_google_genai.chat_models import ChatGoogleGenerativeAI

def LoadGenModel(model_name='gemini-3-flash-preview', temp=1.0):
    model = ChatGoogleGenerativeAI(
        model=model_name,
        temperature = temp
    )
    return model

"""model other parameter
    top_p: float = 0.5 more focued less diverse where result will conistent. 0.9 more focuses tokens, 1.0 considers all tokens
    top_k: int =  low value - more predictable, less diverse, higher value: more diverse, protentialyy less coherent
    n: int = number of response
    max_output_tokens: int = max response length
    timeout: float = api call timeout in seconds
    max_retries: int = number of retry for attempts on failure
    stop: list = ignore word, symbols or other things
    safty_settings: dict = 
    tools: list = 
    tool_config: dict = 
    google_api_key: str = google_api_key
    google_api_base: str = custom api endpoint
    client_options: dict = advanced client configuration
    transport: str = HTTP transport methodrest api, grpc
    client: any = provide custom client instance
    convert_system_message_to_human: bool = 
    streamings: bool = Control content filtering
    **kwargs 

"""