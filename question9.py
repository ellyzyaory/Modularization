def filter_long_words(lwords,n):
    lst = []
    for i in lwords:
        if len(i) > n:
            lst.append(i)
        else:
            pass
    return lst

if __name__=="__main__":
    words = list(input("Enter a list of words: ").split(","))
    numbers = int(input("Enter a list of numbers: "))
    print(filter_long_words(words, numbers))

