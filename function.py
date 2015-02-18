def add(x,y):#Julio Cesar Gonzalez Uribe A01229898
 sum= x+y
 return sum
def substract(x,y):
    sub=x-y
    return sub
def multiply(x,y):
    mul=x*y
    return mul
def divide(x,y):
    div= x//y
    return div
def remainder(x,y):
    rem=x%y
    return rem
print ('welcome')
x=int(input('enter the first number '))
y=int(input('enter the second number '))
print('the sum is: ',add(x,y))
print('the substraction is: ',substract(x,y))
print('the multiplication is: ',multiply(x,y))
print('the division is: ',divide(x,y))
print('the remainder is:',remainder(x,y))
