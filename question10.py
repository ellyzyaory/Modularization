def pangram():
    if (string >= 'a' and string <= 'z') or (string >= 'A' and string <= 'Z'):
        return True
    return False

if __name__ == "__main__":
    string = input("Enter a sentence: ")
    if pangram() == True:
        print("This is a pangram")
    else:
        print("This is not a pangram")
