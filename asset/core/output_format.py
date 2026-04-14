out_temp = [
    {
        "question": "string(do not mention Section, API code number, Article number)",
        "options": [
            {"option": "string",
             "is_correct": bool}
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

"""DIFFICULTY_MIX_CONFIG = {
    "realistic": {
        "label": "Realistic API exam blend",
        "open_book_percent": 60,
        "closed_book_percent": 40,
        "description": "Mix of clause lookup/calculation questions and conceptual recall questions"
    },
    "closed_book": {
        "label": "Closed-book only",
        "open_book_percent": 0,
        "closed_book_percent": 100,
        "description": "Conceptual recall questions only; no clause lookup required"
    },
    "open_book": {
        "label": "Open-book only",
        "open_book_percent": 100,
        "closed_book_percent": 0,
        "description": "Clause lookup and calculation-based questions only"
    }
}"""

