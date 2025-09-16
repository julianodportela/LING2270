"""
Simple Eliza Clone
Based on Haskell implementation by Tim Hunter
LING 2270, Fall 2025
"""


def response(instring):
    """
    Generate response to user input.
    Input: user input string
    Output: Eliza's response
    """
    if instring.startswith("I need "):
        return "Why do you need " + reflect(after(instring, "I need ")) + "?"
    elif instring.startswith("I am "):
        return "Do you enjoy being " + reflect(after(instring, "I am ")) + "?"
    elif instring.startswith("I can't "):
        return "Perhaps you could " + reflect(after(instring, "I can't ")) + " if you tried."
    elif instring.startswith("I don't "):
        return "Do you want to " + reflect(after(instring, "I don't ")) + "?"
    elif instring.startswith("I feel "):
        return "When do you usually feel " + reflect(after(instring, "I feel ")) +  "?"
    elif instring.startswith("You don't "):
        return "Do you really think I don't " + reflect(after(instring, "You don't ")) + "?"
    elif instring.startswith("You are "):
        return "I may be " + reflect(after(instring, "You are ")) + " --- what do you think?"
    elif instring.startswith("You "):
        return "Why do you say that about me?"
    elif instring.startswith("Because "):
        return "Is that the real reason?"
    elif "family" in instring:
        return "I see ... tell me more about your family."
    elif "computer" in instring:
        return "How do computers make you feel?"
    elif " is " in instring:
        return "Why is " + reflect(before(instring, " is ")) + " " + reflect(after(instring, " is ")) + "?"
    elif instring == "Yes":
        return "You seem very certain ... how can you be so sure?"
    elif instring == "No":
        return "Why not?"
    elif instring.startswith("I never "):
        return "You really never " + reflect(after(instring, "I never ")) + " at all?"
    else:
        if len(instring) % 3 == 1:
            return "Could you elaborate on that?"
        elif len(instring) % 3 == 0:
            return "How do you feel when you say that?"
        else: 
            return "Perhaps the answer lies within yourself?" 


def after(string, prefix):
    """
    Input: string and string prefix
    Output: portion of input string following the given prefix
    """
    return string.split(prefix)[1]


def before(string, suffix):
    """
    Input: string and string suffix
    Output: portion of the input string preceding the given suffix
    """
    return string.split(suffix)[0]


def reflect(string):
    """
    Input: string from the perspective of the patient
    Output: string from the perspective of the psychotherapist talking about the patient's experience
    """
    return ' '.join([reflect_word(word) for word in string.split()])


def reflect_word(word):
    """
    Swap perspective of speaker/listener for pronouns and agreeing verbs, if
    applicable, else return original word.
    """
    if word == "I":
        return "you"
    elif word == "me":
        return "you"
    elif word == "you":
        return "me"
    elif word == "am":
        return "are"
    elif word == "was":
        return "were"
    elif word == "my":
        return "your"
    elif word == "your":
        return "my"
    elif word == "myself":
        return "yourself"
    elif word == "yourself":
        return "myself"
    else:
        return word


# interactive loop for command line
if __name__ == "__main__":
    ui = input("Hello! I am the psychotherapist. Please describe your problems to me.\n> ")
    while not ui == "quit":
        output = response(ui)
        print(output + "\n")
        ui = input("> ")
    print("Thank you. That will be $150. Have a nice day!\n")
