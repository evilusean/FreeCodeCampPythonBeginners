try:
    number=int(input("Enter a number"))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")
#creates a new error message for all errors can specify with 'except ZeroDivisionError:' 'ValueError:' ,etc
# best practice is to except specific errors
# except ZeroDivision as err:
# print(err)