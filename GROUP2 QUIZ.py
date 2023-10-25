print('')

quest1 = ('1. A loop enables a particular set of conditions to be executed repeatedly until a condition is satisfied.', '2. A loop does not have the ability to iterate over the items of any sequence, suc as a list or string. ', '3. If the else statement is used with a for loop, the else statement is not executed when the loop hs exhausted iterating the list.','4. A range function either takes a single number and behaves like a list of numbers.','5. if the else statement is used with  while loop[, the else statement is executed when the coondition becomes false.','6. range(n): generates a set of wholoe numbers starting from 0 to (n-1).','7. range(n): generates a set of whole number starting from start tp stop-1.','8. If a sequence contains an expression list, it is evaluated last.','9. len(): provides the total number of elements in the tuple as well as the range() to give us the actual sequence to iterate over.','10. a loop has the ability to iterate over the items of any sequence, such as list or a string.')
ans1 = ('T','F','F','T','F','T','F','F','T','T')
quest2 = ('1. it is used inside the loop to exit out of the loop.\n a.  Break Statement b. Continue Statement c. Pass Statement','2. allows you to bypass the curent iteration of any loop. \n a. Break Statement b. Continue Statement c. Pass Statement','3. Used to indicate "null" or unimplemented functions and loops. \n a. Control Statements b. Continue Statement c. Pass Statement','4. It is useful when we want to terminate the loop as soon as the condition is fulfilled. \n a. Break Statement b. Continue Statement c. Pass Statement','5. It is much like a comment, bu the python interpreter treats the pass statements as valid Python Statements while completely ignoring the comment statement. \n a. Break Statement b. Control Statements c. Pass Statement','6. It does not end the loop but rather moves on to the next iteration. \n a. Control Statements b. Continue Statement c. Pass Statement','7. They alter the execution sequence in a loop. \n a. Control Statements b. Continue Statement c. Pass Statement','8. which control statement is being used when the python interpreter ignores the rest of the loop body statements for the current iteration and returns program execution to the very first statement in the loop body? \n a. Control Statements b. Continue Statement c. Pass Statement','9. considered as a no-operation statement. \n a. Break Statement b. Continue Statement c. Pass Statement','10. it consmes the execution cycle like a valid Python Statement, but nothing happens actually when it is executed. \n a. Break Statement b. Continue Statement c. Pass Statement')
ans2 = ('A','B','C','A','C','B','A','B','C','C')
quest3 = ('1. Are used on conditional statements that yield a result of either a TRUE or FALSE value.','2. It determines whether two criteria are True at the same time.','3. It examines multiple conditions, like AND operator. However, it returns True when one or both of the condidtions are met. ','4. In case an expression has several operators with the same precedence, Python will evaluate them from the________?','5. Python evaluates logical operatos in the order they are listed when you mix them in an expression, which is known as?','6. True if either of the operand is true.','7. It is a programming concept in which the compiler skips the execution of evaluation of some sub-expressions in a logical expressions.','8. It summarizes how we combine two logical conditions based on AND, OR, NOT.','9. In testing for Python programs, you may want to check multiple conditions at the same time. to do so, ehich operator will you use?','10. True if the operand is false.',)
ans3 = ('LOGICAL OPERATORS','AND','OR','LEFT TO RIGHT','OPERATOR PRECEDENCE','OR','SHORT-CIRCUIT EVALUATION','TRUTH TABLE','LOGICAL OPERATORS','NOT')

userans1 = []
userans2 = []
userans3 = []
userscore1 = 0
userscore2 = 0
userscore3 = 0
num1 = 0
num2 = 0
num3 = 0
turns=3

while turns <= 3:
    cred = input('Enter username: ')
    cred2 = input('Enter password: ')
    if cred =='1' and cred2 =='1':
        print('Logged In!!')
        print()

        print("GROUP 2 QUIZ")
        print()
        print("MODULE 11 - Answer 'T' for True, 'F' for False")
        
        for q1 in quest1:
          print()
          print (q1)
          print()
          userans1 = input("(T/F): ")
          if userans1 == ans1[num1]:
              print("Naisu!!!")
              userscore1 += 1
          else:
              print("No! >:(")
          num1 += 1
        print()
        print("Score: " + str(userscore1))

        print()
        print("MODULE 12 - Choose the correct letter: A, B, or C")
        
        for q2 in quest2:
            print()
            print(q2)
            print()
            userans2 = input("A/B/C: ")
            if userans2 == ans2[num2]:
                print("Naisu!!!")
                userscore2 += 1
            else:
                print("No! >:(")
            num2 += 1
        print()
        print("Score: " + str(userscore2))

        print()
        print("MODULE 13 - Identification (Use CAPITAL LETTERS)")
        
        for q3 in quest3:
            print()
            print(q3)
            print()
            userans3 = input("Answer: ")
            if userans3 == ans3[num3]:
                print("Naisu!!!")
                userscore3 += 1
            else:
                print("No! >:(")
            num3 += 1
        print()
        print("Score: " + str(userscore3))
            
        userscore1 = int(userscore1/len(quest1)*10)
        userscore2 = int(userscore2/len(quest2)*10)
        userscore3 = int(userscore3/len(quest3)*10)

        totscore = (userscore1+userscore2+userscore3)/3
        print()
        print("Total Score: " + str(totscore) + "/30")

        if totscore == 30:
                print("PERFECT SCORE!!")
        elif totscore >= 20:
                print("GREAT JOB!")
        elif totscore >= 15:
                print("GOOD JOB!")
        elif totscore >= 10:
                print("GOOD!")
        elif totscore <= 9:
                print("FIGHTING!!<3")
        break
    else:
        print('Invalid!! Attempts left: ', turns)
        print()
        turns -= 1
        if turns == 0:
            print("Done")
            break

