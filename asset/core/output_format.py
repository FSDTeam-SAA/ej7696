out_temp = [
    {
        'question': 'string(do not mention Section, API code number, Article number)',
        'options': [
            {'option': 'string',
             'is_correct': bool}
        ], 
        'explanation': 'string (explanation for the correct answer and Section, API code number, Article number if have there. )'
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

