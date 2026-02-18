import re
import ast
import json

def CleanData(text):
    # Step 1: Remove all literal backslashes
    cleaned = text.replace("\\", "")

    # Step 2: Remove backticks (` or ``` )
    cleaned = re.sub(r"`{1,3}", "", cleaned)

    # Step 3: Remove code language keywords (json, bash, python, etc.)
    cleaned = re.sub(r'\b(json|bash|python)\b', '', cleaned, flags=re.IGNORECASE)

    # Step 4: Remove newlines and extra spaces
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()

    """print('x' * 100)
    print(cleaned)
    print('x' * 100)"""
    #cleaned = ast.literal_eval(cleaned)
    print(cleaned)
    #cleaned = json.loads(cleaned)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # 3️⃣ Fallback for GPT Python-style dict output
    try:
        return ast.literal_eval(cleaned)
    except Exception as e:
        print("Parsing failed:", e)
        raise ValueError("Model response is not valid JSON or Python literal")
    return cleaned