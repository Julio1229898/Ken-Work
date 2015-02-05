print ('welcome this will convert Fahrenheit to Celsius')

print ('give me the temperature that you want to convert')

temp= float(input())

res= 5*(temp-32)/9

if (res>=100):

 print ('the temperature is', res, 'at this temperature the water will boil at normal conditions' )

else:
    print ('the temperature is', res, 'at this temperature the water will not boil at normal conditions')
