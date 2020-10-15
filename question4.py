def is_member(val, list):
    if list.count(val) >= 1:
        return True
    else:
        return False

if __name__ == "__main__":
    x = eval(input("Enter a value: "))
    a = list(eval(input("Enter a list: ")))
    print(is_member(x,a))
