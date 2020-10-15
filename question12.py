def make_forms(verb):
    if verb[-1] == 'y':
        new_verb = verb.replace('y', "ies", -1)
    elif verb[-1] == 'o':
        new_verb = verb + "es"
    elif verb[-2:] == "ch":
        new_verb = verb + "es"
    elif verb[-2:] == "sh":
        new_verb = verb + "es"
    elif verb[-1] == 's':
        new_verb = verb + "es"
    elif verb[-1] == 'x':
        new_verb = verb + "es"
    elif verb[-1] == 'z':
        new_verb = verb + "es"
    else:
        new_verb = verb + 's'
    return new_verb

if __name__=="__main__":
    user_input = input("Enter a word: ")
    print(make_forms(user_input))
