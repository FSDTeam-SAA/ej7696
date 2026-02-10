

from langchain_openai import ChatOpenAI

def LoadOpenAIModel(model_name='gpt-4.1-2025-04-14', temp=0.7):
    model = ChatOpenAI(
        model=model_name,
        temperature=temp
    )

    return model