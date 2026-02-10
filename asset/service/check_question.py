

def CheckQuestionCount(response, n_question):

    if len(response) > n_question:
        response = response[:n_question]
        need_question = 0
        print("Trimmed the response to match the requested number of questions.")
    elif len(response) < n_question:
        need_question = n_question - len(response)
        print(f"Need to generate {need_question} more questions.")
    elif len(response) == n_question:
        need_question = 0
        print("Generated the exact number of requested questions.")
    return need_question, response
