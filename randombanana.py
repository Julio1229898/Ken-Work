import random#Julio Cesar Gonzalez Uribe A01229898
cont=0
def ran():
      numero=random.randint(1,100)
      return numero
x= ran()
r=int(input('welcome to the random machine try to guess the number: '))
while (r != x):
  if (r>x):
    r=int(input('your number is too big choose a lower one: '))
    cont=cont+1
  else:
   if(r<x):
     r=int(input('your number is lower than the answer choose a biger one: '))
     cont=cont+1
cont=cont+1
print ('Congratulations you win in ',cont," attemps")
