def translate(text):
    words = ""
    for i in range(len(text)):
        if text[i] =='a' or text[i] =='e' or text[i] =='i' or text[i] =='o' or text[i] =='u' or text[i] == ' ':
            words += text[i]
        else:
            words += text[i] + "o" + text[i]
    return words

if __name__ == "__main__":
    user_input = input("Type a text: ")
    print(translate(user_input))
