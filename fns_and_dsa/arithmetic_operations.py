#performs arithmetic operations on two numbers
def perform_operation(num1, num2, operation):
    if operation == 'add' :
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    else:
        if num1 or num2 != 0:
            return num1 / num2 
        else:
            print("Cannot divide by zero")