def make_forming(verb):
    if verb[-2:] == "be":
        new_verb = verb + "ing"
    elif verb[-2:] == "ee":
        new_verb = verb + "ing"
    elif verb[-1:] == "e":
        new_verb = verb.replace('e',"ing")
    elif verb[-2:] == "ie":
        new_verb = verb.replace("ie", 'y') + "ing"
    elif verb[-1] != 'a' or verb[-1] != 'i' or verb[-1] != 'o' or verb[-1] != 'e' or verb[-1] != 'u':
        if verb[:-2] != 'a' or verb[:-2] != 'i' or verb[:-2] != 'o' or verb[:-2] != 'e' or verb[:-2] != 'u':
            if verb[-2:-1] == 'a' or verb[-2:-1] == 'i' or verb[-2:-1] == 'o' or verb[-2:-1] == 'e' or verb[-2:-1] == 'u':
                new_verb = verb + verb[-1] + "ing"
    else:
        new_verb = verb + "ing"
    return new_verb

if __name__=="__main__":
    user_input = input("Enter a word: ")
    print(make_forming(user_input))
