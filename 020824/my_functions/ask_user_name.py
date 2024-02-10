def ask_user_name(question, variable_name):
    '''
    Info: This function receives a question that's shown in the terminal and the value that the user enters. You can generate a variable.
    \n
    Input data: 
        - str: question
        - str: variable
    \n
    Output data:
        - str: variable_name
    '''
    variable_name = input(question)
    return variable_name