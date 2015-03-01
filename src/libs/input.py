def ask_user_int(prompt):
    try:
        return int(input(prompt + ' '))
    except ValueError:
        return ask_user_int(prompt)
