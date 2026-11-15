def addTwoNumbers(one, two):
    result = one + two
    return result

def multiplyThreeNumbers(one, two, three):
    result = one * two * three
    return result
    
def subtractTwoNumbers(one, two):
    result = one - two
    return result

def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)
