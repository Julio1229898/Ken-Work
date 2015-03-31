def invert (j):
  j=str(j)
  j=j[::-1]
  j=int(j)
  return j
def palindrome(x,y):
  nonlych=0
  possiblelych=0
  pal=0
  while(x<=y):
    a=x
    b=invert(a)
    if(b==x):
      pal=pal+1
    else:
     cont=0 
     while(cont<=30):
      cont=cont+1
      c=b+a
      d=invert(c)
      if(d==c):
       cont=31
       nonlych=nonlych+1
      else:
       if(cont>30):
         possiblelych=possiblelych+1
    x=x+1 
  print('number of palindromes: ',pal )
  print('number of nonlych: ', nonlych)
  print('number of possiblelych: ',possiblelych)
low=int(input('give me the lower number '))
high=int(input('give me the higher number: ')) 
print(palindrome(low,high))             
