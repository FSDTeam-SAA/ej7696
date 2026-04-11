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
            "6. For every question's explanation, provide the correct BOOK/API/Chapter reference hardly check that it is comming from correct referance. 
                Note: For explanation The API reference will remain the same, as the knowledge is derived from the same API source." 
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


# def GenQuestionPrompt(ex_name, sheet_content, knowledge_content, n_question):#, exam_type):

#     sys_message = SystemMessage(
#         content=(
#         "You are a professional exam preparation question examiner for the American Petroleum Institute (API).\n"
#         #f"Your task is to generate {n_question} unique questions based on the provided information and make options different and shuffle every time.\n\n"
#         "You can not mension API/Book/Chapter or other identification on question"
#         f"Question will be generated from {ex_name}"
#         f"Your task is to generate {n_question} unique questions based on the provided information, ensure the options are unique, and shuffle them each time.\n\n"
#         f"For every question's explanation, provide the correct BOOK/API/Chapter reference hardly check that it is comming from correct referance. "
#          "Note: For explanation The API reference will remain the same, as the knowledge is derived from the same API source."
#         #f"Exam difficulty mix should be as follows: {DIFFICULTY_MIX_CONFIG[exam_type]}.\n\n"
#         f"Exam difficulty mix should be as follows: {DIFFICULTY_MIX_CONFIG}.\n\n"
#         f"Follow the specified dictionary output format: {out_temp}.Do not add any extra text except the output list of dictionary template.\n\n"
#         f"Do not hellociate or add any extra information outside the specified format. and give {n_question} questions\n"
#         )
#     )


#     hum_message = HumanMessage(
#         content=(
#             f"Exam Name:\n{ex_name}\n\n"
#             f"Effectivity Sheet Content:\n{sheet_content}\n\n"
#             f"Body of Knowledge Content:\n{knowledge_content}\n\n"
#         )
#     )

#     temp = PromptTemplate(
#         template="SYSTEM INSTRUCTIONS:\n{sys_message}\n\n"
#         "USER CONTENT: \n{hum_message}",
#         input_variables=['sys_message', 'hum_message']
#     )

#     prompt = temp.invoke(
#         input={
#             'sys_message': sys_message.content,
#             'hum_message': hum_message.content
#         }
#     )

#     prompt = prompt.text

#     return prompt



# def GenQuestionPrompt(ex_name, sheet_content, knowledge_content, n_question):
#     sys_message = SystemMessage(
#         content=(
#             "You are a professional exam preparation question generator for the American Petroleum Institute (API).\n\n"

#             f"Question will be generated only for the exam: {ex_name}.\n"
#             f"Generate exactly {n_question} unique multiple-choice questions based only on the provided information.\n\n"

#             "STRICT RULES:\n"
#             "1. Generate questions ONLY from the provided Effectivity Sheet Content and Body of Knowledge Content.\n"
#             "2. Do NOT use outside knowledge, related standards, related API documents, ASME codes, recommended practices, or general industry knowledge unless they are explicitly written in the provided contents.\n"
#             "3. Do NOT generate any question from outside the exam scope.\n"
#             "4. Do NOT mention API/Book/Chapter/Code name/Section number or any document identification inside the question stem.\n"
#             "5. Every question must have 4 options.\n"
#             "6. Only 1 option must be correct.\n"
#             "7. Options must be unique and shuffled.\n"
#             "8. Do NOT hallucinate any topic, answer, explanation, or reference.\n"
#             "9. If a valid reference is not available in the provided contents, do NOT create that question.\n"
#             "10. It is better to return fewer valid questions than to generate out-of-scope questions.\n\n"

#             "REFERENCE AND EXPLANATION RULES:\n"
#             "1. Every question must include an explanation.\n"
#             "2. Every explanation must include the exact correct Book/API/Chapter/Section reference.\n"
#             "3. The reference must come only from the provided contents.\n"
#             "4. Never invent or guess a reference.\n"
#             "5. If the provided contents do not support the explanation and reference, discard the question.\n\n"

#             "SELF-CHECK BEFORE FINALIZING EACH QUESTION:\n"
#             "1. Is the topic explicitly present in the provided contents?\n"
#             "2. Is the correct answer explicitly supported by the provided contents?\n"
#             "3. Is the explanation supported by the provided contents?\n"
#             "4. Is the Book/API/Chapter/Section reference explicitly available in the provided contents?\n"
#             "If any answer is NO, discard that question.\n\n"

#             f"Exam difficulty mix should be as follows: {DIFFICULTY_MIX_CONFIG}.\n\n"

#             f"Follow the exact dictionary output format: {out_temp}\n"
#             "Do not add any extra text, heading, note, markdown, or explanation outside the output list.\n"
#         )
#     )

#     hum_message = HumanMessage(
#         content=(
#             f"Exam Name:\n{ex_name}\n\n"
#             f"Effectivity Sheet Content:\n{sheet_content}\n\n"
#             f"Body of Knowledge Content:\n{knowledge_content}\n\n"
#         )
#     )

#     temp = PromptTemplate(
#         template="SYSTEM INSTRUCTIONS:\n{sys_message}\n\nUSER CONTENT:\n{hum_message}",
#         input_variables=["sys_message", "hum_message"]
#     )

#     prompt = temp.invoke(
#         input={
#             "sys_message": sys_message.content,
#             "hum_message": hum_message.content
#         }
#     )

#     return prompt


def GenQuestionPrompt(ex_name, sheet_content, knowledge_content, n_question):
    sys_message = SystemMessage(
        content=(
            "You are a professional exam preparation question generator for the American Petroleum Institute (API).\n\n"

            f"Questions must be generated only for the exam: {ex_name}.\n"
            f"Generate exactly {n_question} unique multiple-choice questions based only on the provided information.\n\n"

            "STRICT SCOPE RULES:\n"
            "1. Generate questions ONLY from the provided Effectivity Sheet Content and Body of Knowledge Content.\n"
            "2. Do NOT use outside knowledge, related standards, related API documents, ASME codes, recommended practices, or general industry knowledge unless they are explicitly written in the provided contents.\n"
            "3. Do NOT generate any question from outside the exam scope.\n"
            "4. Do NOT mention API/Book/Chapter/Code name/Section number or any document identification inside the question stem.\n"
            "5. Every question must have exactly 4 options.\n"
            "6. Only 1 option must be correct.\n"
            "7. Options must be unique and shuffled.\n"
            "8. Do NOT hallucinate any topic, answer, explanation, or reference.\n"
            "9. If a valid explicit reference is not available in the provided contents, discard the question.\n"
            "10. It is better to return fewer valid questions than to generate out-of-scope or weakly supported questions.\n\n"

            "REFERENCE RULES (VERY IMPORTANT):\n"
            "1. Every question must include an explanation and inside first parent thisis.\n"
            "2. Every explanation must include the exact reference for the correct answer.\n"
            "3. The reference must be a real document citation explicitly present in the provided contents, such as:\n"
            "   - API {number}, Section {number}\n"
            "   - {Name} Section VIII, Div. {number}, UG{number}\n"
            "   - NBIC Part {number}, {number}\n"
            "   - other Number not mension ' Body of Knowledge'"
            "4. NEVER use generic source labels as references, including but not limited to:\n"
            "   - Body of Knowledge Content\n"
            "   - Effectivity Sheet Content\n"
            "   - Section II\n"
            "   - Knowledge Content\n"
            "   - Sheet Content\n"
            "5. A valid reference must identify the actual code/book/API document and the exact section/paragraph/clause/article when available.\n"
            "6. If the provided text mentions only a topic but does NOT provide an actual document identifier and section/paragraph/clause reference, discard the question.\n"
            "7. Never guess, reconstruct, normalize, or invent a reference from partial clues.\n"
            "8. If the exact citation in the provided content is ambiguous, incomplete, or generic, discard the question.\n\n"

            "EXPLANATION RULES:\n"
            "1. The explanation must be directly supported by the provided contents.\n"
            "2. The explanation must be concise and factual.\n"
            "3. The explanation must end with the exact supporting reference.\n"
            "4. The reference must be specific enough that a student could locate it in the actual code/document.\n\n"

            "SELF-CHECK BEFORE FINALIZING EACH QUESTION:\n"
            "1. Is the topic explicitly present in the provided contents?\n"
            "2. Is the correct answer explicitly supported by the provided contents?\n"
            "3. Is the explanation explicitly supported by the provided contents?\n"
            "4. Does the reference explicitly name the actual API/code/book document?\n"
            "5. Does the reference explicitly include the actual section/paragraph/clause/article if present in the content?\n"
            "6. Is the reference something more specific than 'Body of Knowledge Content' or 'Section II'?\n"
            "If any answer is NO, discard that question.\n\n"

            f"Exam difficulty mix should be as follows: {DIFFICULTY_MIX_CONFIG}.\n\n"

            "OUTPUT RULES:\n"
            "1. Follow the exact dictionary output format provided.\n"
            "2. Do not add any extra text, heading, note, markdown, or explanation outside the output list.\n"
            "3. If fewer than the requested number of valid questions can be supported with exact references, return fewer questions.\n\n"

            f"Follow the exact dictionary output format: {out_temp}\n"
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
        template="SYSTEM INSTRUCTIONS:\n{sys_message}\n\nUSER CONTENT:\n{hum_message}",
        input_variables=["sys_message", "hum_message"]
    )

    prompt = temp.invoke(
        input={
            "sys_message": sys_message.content,
            "hum_message": hum_message.content
        }
    )

    return prompt