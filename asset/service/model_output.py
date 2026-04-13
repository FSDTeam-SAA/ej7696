def ModelOutput(model, prompt):
    try:
        response = model.invoke(prompt).content
        status=True
        # print(response)
    
    except Exception as ex:
        status = False
        response = str(ex)

    """print('-' * 80)
    print(response)
    print('-' * 80)"""
    return status, response