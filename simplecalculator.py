def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation: \n")
print("1.Addition \t\t\t\t 2.Subtraction")
print("3.Multiplication \t\t 4.Division\n")


while True:

    ops = input("Enter choice( 1 | 2 | 3 | 4 ): ")

    
    if ops in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if ops == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif ops == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif ops == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif ops == '4':
            if num2 != 0:
                print(num1, "/", num2, "=", divide(num1, num2))
            else:
                print("Zero Division Error")
             
        n_calcu = input("Another calculation? (yes/no): ")
        if n_calcu == "no" or n_calcu == "n":
          break
    else:
        print("Invalid Input")