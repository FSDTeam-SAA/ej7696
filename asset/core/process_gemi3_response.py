"""def get_text(response):
    processed = response[0]['text']
    #print(processed)
    return processed
"""

def get_text(response):
    # Gemini Flash sometimes returns []
    if not response:
        return None

    # Expected format: [{'text': '...'}]
    if isinstance(response, list):
        first = response[0]
        if isinstance(first, dict) and 'text' in first:
            text = first['text']
            if text and text.strip():
                return text.strip()

    return None
