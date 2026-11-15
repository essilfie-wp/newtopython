from functions import addTwoNumbers, multiplyThreeNumbers, countdown


addtheseforme = addTwoNumbers(17, 13)

print(addtheseforme)

multiplytheseforme = multiplyThreeNumbers(17, 10, 10)

print(multiplytheseforme)

nested = addTwoNumbers(multiplyThreeNumbers(17, 10, 10),17)

print("result", nested,  sep=" : ")

# lambda function for adding 2 numbers

addTwoNumbersLambda = lambda x, y: x + y

print("lambda function", addTwoNumbersLambda(17, 13),  sep=" : ")

countdown(5)

def my_generator():
    yield 1
    yield 2
    yield 3

# my_generator = [3, 4, 5]

for value in my_generator():
    print(value)