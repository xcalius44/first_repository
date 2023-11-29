def ask_yes_no (question):
    response = None
    while response not in ("y","n"):
        response  = input(question) + '(y/n)?'.lower()
    return response

def ask_number(question, low, high):
    response = None
    while response not in range(low, high + 1):
       response  = int(input(question))
    return response

if __name__ == "__main__":
    print("You have started the games module, "
        "and not imported it (import games).")
    print("Module testing. ")
    answer  = ask_yes_no("We continue testing") 
    print("The function ask_yes_no returned", answer)
    answer = ask_number("Enter an integer from 1 to 10:", 1, 10) 
    print("The ask_number function returned", answer)
