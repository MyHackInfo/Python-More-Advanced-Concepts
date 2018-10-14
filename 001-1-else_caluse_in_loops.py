'''
    ### Else Caluse In Loops ###
   1-Loop statements may have an else clause;
    -it is executed when the loop terminates through exhaustion
    -of the list with for or when the condition becomes false with while.
   2-A while and for loop can have an optional else clause.


'''
#"1-While Loop
print("1-While Loop")
num =1
while num<10:
    print("Number is {}".format(num))
    num+=1
else:
    print("While loops is end")

# 2-For Loop
print("\n2-For loop")
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')
