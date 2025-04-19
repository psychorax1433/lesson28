try:
   num1 = int(input("Enter the 1st number: "))
   num2 = int(input("Enter the 2nd number: "))
   result = num1/num2
   print("Result is : ", result)
except ZeroDivisionError:
                          print("Division by zero is banned")
except ValueError:
                   print("Please enter only number beacause this app is made for dividing numbers")
except :
        print ("Some error occured")
finally:
        print("i do maths no matter what, ")