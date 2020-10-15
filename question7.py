def words_to_integers(conversion):
    number = []
    for i in conversion:
        number.append(len(i))
    return number

if __name__=="__main__":
    user_input = input("Enter a list of words: ").split(",")
    print(words_to_integers(user_input))
