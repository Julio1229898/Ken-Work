print ('Give me a number')

num1 = int(input()) 

print ('Enter the sign of the operation (add, subtract, divide, product) you want to do (if you want the remainder of the division put %)')                                                                                                                                                                                                                                                                                                                                                                                                                                            

sign = (input())

print ('Give me the other number')

num2 = int(input())

if(sign == '+'):

   answer = (num1+num2)

   print ('the answer is: ',answer)

else:
    if (sign=='-'):

       answer = (num1-num2)

       print ('the answer is:', answer)

    else:
        if (sign=='/'):

            answer = (num1//num2)

            print ('the answer is:', answer)

        else:
            if (sign=='*'):
                answer = (num1*num2)

                print ('the answer is:', answer)
            else:
                if (sign=='%'):
                    answer = (num1%num2)

                    print ('the answer is:', answer)
