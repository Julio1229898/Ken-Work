def find_threes(a):
    add=0
    for x in a:
        if (x%3==0):
          add=add+x
    return add
list1= [0,4,2,6,9,8,3,12]
print (find_threes(list1))
