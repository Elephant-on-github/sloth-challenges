import re

def doesRhyme(phrase1, phrase2):
    phrase1 = phrase1.split()[-1].lower()
    phrase1 = re.sub(r'[^aeiouy]', '', phrase1)
    phrase2 = phrase2.split()[-1].lower()
    phrase2 = re.sub(r'[^aeiouy]', '', phrase2)
    if phrase1 == phrase2:
        print("True")
        return True
    else:
        print("False")
        return False
    
doesRhyme("Sam I am!", "Green eggs and ham.")
doesRhyme("Sam I am!", "Green eggs and HAM.")
doesRhyme("You're built like a seat", "I bet you like to eat")
doesRhyme("You are off to the races", "a splendid day.")
doesRhyme("and frequently do?", "you gotta move.")