import string

def char_freq(text):
    text_upper = text.upper()
    for i in string.ascii_uppercase:
        if text_upper.count == 0:
            pass
        else:
            print(i, ':', text_upper.count(i))
    return [char for char in words]

if __name__ == "__main__":
    words = input("Enter a string: ")
    char_freq(words)
    print(char_freq(words))
