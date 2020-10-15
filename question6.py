def histogram(lst):
    for i in lst:
        print(i * "*")

if __name__ == "__main__":
    my_list = list(eval(input("Make a list: ")))
    histogram(my_list)


