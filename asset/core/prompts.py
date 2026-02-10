from langchain_core.prompts import PromptTemplate
from asset.core.output_format import out_temp, DIFFICULTY_MIX_CONFIG
from langchain.messages import SystemMessage, HumanMessage, AIMessage

"""def GenBookPrompt(ex_name, sheet_content, knowledge_content):

    sys_message = SystemMessage(
        content=(
            "You are a professional exam preparation book author.\n"
            "Your task is to generate structured, exam-focused study content with more discriptive\n\n"
            "IMPORTANT RULES:\n"
            "1. Use ONLY the provided exam content and body of knowledge.\n"
            "2. Do NOT add external standards, practices, or assumptions.\n"
            "3. Do NOT invent topics beyond the given scope.\n"
            "4. Write in a clear, formal, instructional tone suitable for open-book exams.\n"
            "5. Keep terminology consistent with the provided content."
        )
    )

    hum_message = HumanMessage(
        content=(
            f"Exam Name:\n{ex_name}\n\n"
            f"Effectivity Sheet Content:\n{sheet_content}\n\n"
            f"Body of Knowledge Content:\n{knowledge_content}\n\n"
        )
    )


    temp = PromptTemplate(
        template="SYSTEM INSTRUCTIONS:\n{sys_message}\n\n"
        "USER CONTENT: \n{hum_message}",
        input_variables=['sys_message', 'hum_message']
    )

    prompt = temp.invoke(
        input={
            'sys_message': sys_message.content,
            'hum_message': hum_message.content
        }
    )

    prompt = prompt.text

    return prompt"""


def GenQuestionPrompt(ex_name, sheet_content, knowledge_content, n_question):#, exam_type):

    sys_message = SystemMessage(
        content=(
        "You are a professional exam preparation question examiner for the American Petroleum Institute (API).\n"
        #f"Your task is to generate {n_question} unique questions based on the provided information and make options different and shuffle every time.\n\n"
        f"Your task is to generate {n_question} unique questions based on the provided information, ensure the options are unique, and shuffle them each time.\n\n"
        #f"Exam difficulty mix should be as follows: {DIFFICULTY_MIX_CONFIG[exam_type]}.\n\n"
        f"Exam difficulty mix should be as follows: {DIFFICULTY_MIX_CONFIG}.\n\n"
        f"Follow the specified dictionary output format: {out_temp}.Do not add any extra text except the output list of dictionary template.\n\n"
        f"Do not hellociate or add any extra information outside the specified format. and give {n_question} questions\n"
        )
    )


    hum_message = HumanMessage(
        content=(
            f"Exam Name:\n{ex_name}\n\n"
            f"Effectivity Sheet Content:\n{sheet_content}\n\n"
            f"Body of Knowledge Content:\n{knowledge_content}\n\n"
        )
    )

    temp = PromptTemplate(
        template="SYSTEM INSTRUCTIONS:\n{sys_message}\n\n"
        "USER CONTENT: \n{hum_message}",
        input_variables=['sys_message', 'hum_message']
    )

    prompt = temp.invoke(
        input={
            'sys_message': sys_message.content,
            'hum_message': hum_message.content
        }
    )

    prompt = prompt.text

    return prompt