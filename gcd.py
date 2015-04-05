def gcd(x,y): #Julio Cesar Gonzalez Uribe A01229898
    if(x==y):
     print(x)
    else:
        while(x!=y):
            if(x>y):
              x=x-y
            elif(x<y):
             y=y-x
        return x		
num1=int(input('give me the first number of the gcd: '))
num2=int(input('give me the second number of the gcd: '))
print(gcd(num1,num2))
