import logging
logger=logging.getLogger(__name__)
logging.basicConfig(filename='test.log',level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(message)s')
def calculator():
    """Simple calculator for basic arithmetic operations"""
    print("Welcome to the simple calculator!")
    print("Available operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please use +, -, *, or /.")
            return
        
        logger.info(f"The result of {num1} {operation} {num2} is: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Call the calculator function
calculator()
