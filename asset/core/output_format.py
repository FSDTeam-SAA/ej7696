"""out_temp = [
    {
        "question": "string(do not mention Section, API code number, Article number)",
        "options": [
            {
                "serial_no": "A, B, C, D",
                "option": "string",
                "is_correct": bool
            }
        ],
        "explanation": "string (must explain why the correct answer is right and include only the exact API reference from the provided content, such as API {number}, Chapter {number}, Section {number}, Clause {number}, Article {number}, Page {number} if available. Do not use forbidden or generic reference words such as ASME, Body of Knowledge, Sheet Content, Knowledge Base, Book, or any non-API source)"
        #"explanation": "string (explanation for the correct answer and Section, API code number, Article number. Invalid/Forbidden referance word like ASME or other words,Body of Knowledge, Body of Knowledge, Sheet of content or other ingeneric word)"
    }
]


DIFFICULTY_MIX_CONFIG = {
    "label": "Realistic API exam blend",
    "open_book_percent": 60,
    "closed_book_percent": 40,
    "description": "Mix of clause lookup/calculation questions and conceptual recall questions"
}

QUESTION_TYPE_CONFIG = {
    "single_correct": {
        "percent": 70,
        "options_type": "only one option is correct",
    },
    "multiple_correct": {
        "percent": 30,
        "options_type": "multiple options can be correct like A and C or B and D or A and D or A and B and C etc. or All above.  There also only one option will shouild true",
    }
}
"""

# asset/core/output_format.py
out_temp = [
    {
        "question": "string — write the question in plain language; do NOT mention any API code numbers, section numbers, chapter names, article numbers, or book titles inside the question text",
        "options": [
            {
                "serial_no": "A | B | C | D | E",
                "option": "string — each option must be unique and clearly different from the others",
                "is_correct": "bool"
            }
        ],
        "type": "single_correct | multiple_correct",
        "explanation": (
            "string — two parts:\n"
            "1. WHY: A concise justification of why the correct answer is right.\n"
            "2. REFERENCE: The exact API reference extracted from the provided content, "
            "formatted as: (API {number}, Chapter {number}, Section {number.number}, "
            "Clause {number} [if applicable], Page {number} [if applicable]).\n"
            "FORBIDDEN reference words: ASME, Body of Knowledge, Sheet Content, "
            "Knowledge Base, Book, or any generic/non-API label."
        )
    }
]


DIFFICULTY_MIX_CONFIG = {
    "label": "Realistic API exam blend",
    "distribution": {
        "open_book_percent": 60,
        "closed_book_percent": 40,
    },
    "description": (
        "open_book: clause lookup or calculation questions requiring reference material. "
        "closed_book: conceptual recall questions answered from memory."
    )
}


QUESTION_TYPE_CONFIG = {
    "distribution": {
        "single_correct_percent": 70,
        "multiple_correct_percent": 30,
    },
    "definitions": {
        "single_correct": (
            "Exactly 4 options (A, B, C, D). Exactly one option is correct.\n"
            "The other three options are plausible but clearly wrong.\n"
            "Only one 'is_correct' field must be true.\n\n"

            "SHUFFLING IS MANDATORY — follow this exactly:\n"
            "  - Write all 4 options first, then physically place the correct answer "
            "at a different serial_no for every question.\n"
            "  - Distribute correct answers across all positions: "
            "some questions correct at A, some at B, some at C, some at D.\n"
            "  - Target distribution across every 4 questions: "
            "one correct at A, one at B, one at C, one at D.\n"
            "  - NEVER place the correct answer at the same position twice in a row.\n"
            "  - NEVER default to placing the correct answer at position A or B.\n\n"

            "EXAMPLE OF REQUIRED VARIATION across 4 questions:\n"
            "  Q1: { A: wrong, B: wrong, C: CORRECT, D: wrong }\n"
            "  Q2: { A: wrong, B: CORRECT, C: wrong, D: wrong }\n"  
            "  Q3: { A: wrong, B: wrong, C: wrong, D: CORRECT }\n"
            "  Q4: { A: CORRECT, B: wrong, C: wrong, D: wrong }\n\n"

            "FORBIDDEN:\n"
            "  - Correct answer at A for two or more consecutive questions.\n"
            "  - Correct answer always at A or always at B across all questions.\n"
            "  - Placing the most 'obvious sounding' option always at A.\n"
        ),

        "multiple_correct": (
            "Multiple correct question types have TWO allowed structures. "
            "Rotate between them — do NOT use the same structure for every question.\n\n"

            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "STRUCTURE 1 — 5 options (A, B, C, D, E)\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "  A: individual candidate answer\n"
            "  B: individual candidate answer\n"
            "  C: individual candidate answer\n"
            "  D: WRONG combination referencing only A, B, or C serials "
            "(e.g., 'Both A and C', 'Both B and C') — is_correct=false\n"
            "  E: CORRECT answer — rotate between these forms, do NOT always use 'All of the above':\n"
            "       - 'All of the above' (use for at most 50% of Structure 1 questions)\n"
            "       - A specific correct combination (e.g., 'Both A and B', 'Both B and C')\n"
            "     is_correct=true\n\n"

            "EXAMPLE A (All of the above):\n"
            "  { serial_no: 'A', option: 'Liquid penetrant',           is_correct: false }\n"
            "  { serial_no: 'B', option: 'Radiographic testing',       is_correct: false }\n"
            "  { serial_no: 'C', option: 'Magnetic particle',          is_correct: false }\n"
            "  { serial_no: 'D', option: 'Both A and C',               is_correct: false }\n"
            "  { serial_no: 'E', option: 'All of the above',           is_correct: true  }\n\n"

            "EXAMPLE B (Specific combination):\n"
            "  { serial_no: 'A', option: 'Liquid penetrant',           is_correct: false }\n"
            "  { serial_no: 'B', option: 'Radiographic testing',       is_correct: false }\n"
            "  { serial_no: 'C', option: 'Magnetic particle',          is_correct: false }\n"
            "  { serial_no: 'D', option: 'Both A and C',               is_correct: false }\n"
            "  { serial_no: 'E', option: 'Both A and B',               is_correct: true  }\n\n"

            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "STRUCTURE 2 — 4 options (A, B, C, D)\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "  A: individual candidate answer\n"
            "  B: individual candidate answer\n"
            "  C: CORRECT answer — rotate between these forms, do NOT always use 'All of the above':\n"
            "       - 'All of the above' (use for at most 50% of Structure 2 questions)\n"
            "       - A specific correct combination (e.g., 'Both A and B')\n"
            "     is_correct=true\n"
            "  D: WRONG distractor — rotate between these forms across questions:\n"
            "       - 'None of the above'\n"
            "       - 'A only' or 'B only'\n"
            "       - A wrong standalone answer unrelated to A or B\n"
            "       - A plausible but incorrect rephrasing of one candidate\n\n"

            "EXAMPLE A (All of the above):\n"
            "  { serial_no: 'A', option: 'Liquid penetrant',           is_correct: false }\n"
            "  { serial_no: 'B', option: 'Radiographic testing',       is_correct: false }\n"
            "  { serial_no: 'C', option: 'All of the above',           is_correct: true  }\n"
            "  { serial_no: 'D', option: 'None of the above',          is_correct: false }\n\n"

            "EXAMPLE B (Specific combination):\n"
            "  { serial_no: 'A', option: 'Liquid penetrant',           is_correct: false }\n"
            "  { serial_no: 'B', option: 'Radiographic testing',       is_correct: false }\n"
            "  { serial_no: 'C', option: 'Both A and B',               is_correct: true  }\n"
            "  { serial_no: 'D', option: 'A only',                     is_correct: false }\n\n"

            "HARD RULES (apply to BOTH structures):\n"
            "  1. Serial numbers must always follow strict order — do NOT shuffle them.\n"
            "  2. Only ONE is_correct=true exists across all options.\n"
            "  3. The wrong combination option must ONLY reference individual candidate serials "
            "(A, B, C in Structure 1 — A, B in Structure 2) — NEVER reference D or E.\n"
            "  4. 'All of the above' may ONLY be the correct answer — NEVER a distractor.\n"
            "  5. 'None of the above' may ONLY be a wrong distractor — NEVER the correct answer.\n"
            "  6. NEVER repeat the same distractor form or correct answer form across consecutive questions.\n"
            "  7. NEVER exceed the option count of the chosen structure (4 or 5 only).\n"
            "  8. 'All of the above' must NOT be used as the correct answer more than 50% of the time "
            "across all multiple_correct questions — force variety by using specific combinations instead.\n"
        )
    }
}