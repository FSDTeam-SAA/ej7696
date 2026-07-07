"""from langchain_core.prompts import PromptTemplate
from asset.core.output_format import out_temp, DIFFICULTY_MIX_CONFIG, QUESTION_TYPE_CONFIG
from langchain.messages import SystemMessage, HumanMessage, AIMessage



def GenQuestionPrompt(ex_name, sheet_content, knowledge_content, n_question):#, exam_type):

    sys_message = SystemMessage(
    content=(
            "You are a professional exam preparation question examiner for the American Petroleum Institute (API).\n"
            f"Questions will be generated for the exam: {ex_name}.\n"
            f"Your task is to generate exactly {n_question} unique questions based only on the provided information. Ensure the answer options are distinct and shuffled each time.\n\n"
            
           
            "Do not mention any API code, book name, chapter name, section title, or other source-identifying information inside the question itself.\n\n"
            "Do not correct answer will alway option A or D. It should be shuffle every time and also options should be unique and different from each other.\n\n" 
            "For better you can sheffle the serial no like A, B, C, D or other format but it should be shuffle every time and also options should be unique and different from each other.\n\n"

            "For every question explanation, provide an accurate and verified reference strictly from the correct source.\n"
            "Do not include vague or generic labels such as 'Book', 'Sheet Content', 'Knowledge Base', 'ASME', or any other unnecessary wording.\n\n"

            "REFERENCE FORMAT RULE (MANDATORY):\n"
            "All references MUST follow this exact structure:\n"
            "Referance should be inside first parent thesis ()"
            "- API {code_number}, Chapter {chapter_number}, Section {section_number}\n"
            "- Optional: Clause {clause_number} / Subsection {subsection_number}\n"
            "- Optional: Page {page_number}\n\n"

            "Examples of valid format (structure only, not fixed values):\n"
                "- API {number}, Section {number.number}\n"
                "- API {number}, Chapter {number}, Section {number.number}\n"
                "- ASME, API {number}, Chapter {number}, Section {number.number}\n"
                "- API {number}, Section {number.number.number}\n\n"

                "Instance ASME give API code"
                "Invalid/Forbidden referance word like ASME or other words,Body of Knowledge, Body of Knowledge, Sheet of content or other ingeneric word"

            "DO NOT hardcode or reuse fixed API numbers like 'API 650' unless it explicitly exists in the provided content.\n"
            "Always extract and use the correct API code and numbers from the given material.\n\n"

            "Always clearly identify what each number refers to, such as Section, Clause, Figure, Table, Chapter, or Page. Do not list raw numbers without labels.\n\n"

            "Each explanation must also include a clear and concise justification of why the correct answer is right.\n\n"

            "The reference used in the explanation must match the provided source exactly. Do not infer, invent, or introduce references from outside the provided material.\n\n"

            f"Exam difficulty mix should be as follows: {DIFFICULTY_MIX_CONFIG}.\n\n"
            f"Question type mix should be as follows: {QUESTION_TYPE_CONFIG}.\n\n"
            f"Follow this exact dictionary output format: {out_temp}\n"
             
            "Question also carry option like A and B or C amd D, A and D or all above etc."
           
            "Do not add any extra text outside the required output list of dictionaries.\n"
            f"Do not hallucinate or include any information outside the provided content. Return exactly {n_question} questions.\n"
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

# asset/core/prompts.py

from asset.core.output_format import DIFFICULTY_MIX_CONFIG


SINGLE_CHOICE_OUTPUT_TEMPLATE = """
[
    {
        "question": "string — plain language question only",
        "options": [
            {"serial_no": "A", "option": "string", "is_correct": false},
            {"serial_no": "B", "option": "string", "is_correct": false},
            {"serial_no": "C", "option": "string", "is_correct": true},
            {"serial_no": "D", "option": "string", "is_correct": false}
        ],
        "type": "single_choice",
        "explanation": "string — explain why the correct option is right and include the exact API reference in parentheses"
    }
]
"""

TRUE_FALSE_OUTPUT_TEMPLATE = """
[
    {
        "question": "string — plain language question only",
        "options": [
            {"serial_no": "True", "option": "True", "is_correct": false},
            {"serial_no": "False", "option": "False", "is_correct": true}
        ],
        "type": "true_false",
        "explanation": "string — explain why the correct option is right and include the exact API reference in parentheses"
    }
]
"""

MULTIPLE_ANSWER_OUTPUT_TEMPLATE = """
[
    {
        "question": "string — plain language question only",
        "options": [
            {"serial_no": "A", "option": "string", "is_correct": true},
            {"serial_no": "B", "option": "string", "is_correct": false},
            {"serial_no": "C", "option": "string", "is_correct": true},
            {"serial_no": "D", "option": "string", "is_correct": false}
        ],
        "type": "multiple_answer",
        "explanation": "string — explain why the correct options are right and include the exact API reference in parentheses"
    }
]
"""

QUESTION_TYPE_RULES = {
    "single_choice": {
        "description": "Single-choice questions must have exactly 4 options (A, B, C, D) and exactly one correct answer.",
        "output_template": SINGLE_CHOICE_OUTPUT_TEMPLATE,
    },
    "true_false": {
        "description": "True/false questions must have exactly 2 options labelled True and False, with one correct answer.",
        "output_template": TRUE_FALSE_OUTPUT_TEMPLATE,
    },
    "multiple_answer": {
        "description": "Multiple-answer questions must have 4 options (A, B, C, D) and at least two correct answers, possibly three or all four.",
        "output_template": MULTIPLE_ANSWER_OUTPUT_TEMPLATE,
    },
}

SYSTEM_TEMPLATE = """
    You are a professional exam question writer for American Petroleum Institute (API) certification exams.

    ═══════════════════════════════════════════
    TASK
    ═══════════════════════════════════════════
    Generate exactly {n_question} unique exam questions for: {ex_name}.
    Base every question strictly on the provided Effectivity Sheet and Body of Knowledge content.
    Do NOT hallucinate, infer, or introduce any information not present in the provided material.

    ═══════════════════════════════════════════
    QUESTION TYPE
    ═══════════════════════════════════════════
    {question_type_description}

    ═══════════════════════════════════════════
    QUESTION WRITING RULES
    ═══════════════════════════════════════════
    1. Never mention API codes, section numbers, chapter names, article numbers, book titles,
    or any source-identifying label inside the question text.
    2. Each question must be clear, concise, and based only on the provided content.
    3. Options must be unique, plausible, and clearly distinct from each other.
    4. The correct answer position must be shuffled appropriately for the question type.
    5. Do not include any extra text outside the required Python list.

    ═══════════════════════════════════════════
    DIFFICULTY DISTRIBUTION
    ═══════════════════════════════════════════
    {difficulty_config}

    ═══════════════════════════════════════════
    REFERENCE FORMAT (MANDATORY)
    ═══════════════════════════════════════════
    All references in explanations MUST:
    - Be enclosed in parentheses: ( )
    - Use only real API codes extracted from the provided content — never hardcode values
    - Follow this structure:
        (API {{number}}, Chapter {{number}}, Section {{number.number}})
        (API {{number}}, Section {{number.number}}, Clause {{number}})
        (API {{number}}, Chapter {{number}}, Section {{number.number}}, Page {{number}})

    FORBIDDEN reference words (never use these):
    ASME, Body of Knowledge, Sheet Content, Knowledge Base, Book,
    or any non-API / non-specific label.

    Always label every number explicitly: Section, Clause, Chapter, Figure, Table, or Page.
    Do not list raw numbers without context labels.

    ═══════════════════════════════════════════
    OUTPUT FORMAT
    ═══════════════════════════════════════════
    Return a valid Python list of exactly {n_question} dictionaries.
    Follow this exact structure for every item:
    {output_template}

    - Do NOT include any text, comments, or explanation outside the list.
    - Do NOT wrap the output in markdown code fences.
    - Every string value must be properly escaped.
"""

USER_TEMPLATE = """
    Exam Name: {ex_name}

    Effectivity Sheet Content:
    {sheet_content}

    Body of Knowledge Content:
    {knowledge_content}
"""


def GenQuestionPrompt(ex_name: str, sheet_content: str, knowledge_content: str, n_question: int, question_type: str = "single_choice") -> str:
    question_type = question_type.lower()
    if question_type not in QUESTION_TYPE_RULES:
        question_type = "single_choice"

    type_rule = QUESTION_TYPE_RULES[question_type]
    system_prompt = SYSTEM_TEMPLATE.format(
        ex_name=ex_name,
        n_question=n_question,
        question_type_description=type_rule["description"],
        difficulty_config=DIFFICULTY_MIX_CONFIG,
        output_template=type_rule["output_template"],
    )

    user_prompt = USER_TEMPLATE.format(
        ex_name=ex_name,
        sheet_content=sheet_content,
        knowledge_content=knowledge_content,
    )

    return f"SYSTEM:\n{system_prompt}\n\nUSER:\n{user_prompt}"