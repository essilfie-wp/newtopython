print(4+5)
num1=56
num2=86
num3=num1+num2
print(num3)
num1=65+74
print(num1)
num2=74+93
print(num2)
num3=num1+num2
print(num3)
x=25
y=7
print(x/y)
x = 12
y = 5
print(x // y)
y+=3
print(y)
x%=78
print(x)
numbers={1,2,3,4,5}
if (count:= len(numbers))> 3:
    print(f"List has {count} numbers")
x=67
x="WEEKEND!" if x > 5 else "WORKDAY"
print(x)
y=24
y="Fruit" if y > 8 else "vegetable"
print(y)
z=24
z="apple" if z > 50 else "banana"
print(z)

num=35
x="mouse" if num>9 else "cat"
print(x)

num=6
x="Fri" if num == 5 else "Sat" if num== 6 else "Sun" if num == 7 else "worday"
print(x)
oddnumbers =[1,3,5,7,9,11,13,15,17,19]
total=sum(oddnumbers)
print(total)

total=0
for n in range(1,100,2):
   total+=n
print(total)
#the sum of the first ten fibonacci numbers
fibonacci=[0,1,1,2,3,5,8,13,21,34,55]
total=sum(fibonacci)
print(total)
#comparison operaators
x=4
y=7
print(x==y)
print(x!=y)
print(x>=y)
x=7
print(3>x>8)
print(x<3 and x<8)
x=5
print(x>4 and x>8)
print(x>1 or x>10)
print(not(x>1 and x>10))