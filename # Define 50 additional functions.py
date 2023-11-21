# Define 10 additional functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def max_of_two(a, b):
    return max(a, b)

def min_of_two(a, b):
    return min(a, b)

def max_of_three(a, b, c):
    return max(a, b, c)

def min_of_three(a, b, c):
    return min(a, b, c)

# Create a menu for the user
while True:
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Cube")
    print("7. Power")
    print("8. Check Even")
    print("9. Check Odd")
    print("10. Factorial")
    print("11. Fibonacci")
    print("12. Reverse String")
    print("13. Is Palindrome")
    print("14. Sum of Digits")
    print("15. Max of Two")
    print("16. Min of Two")
    print("17. Max of Three")
    print("18. Min of Three")
    print("0. Exit")

    choice = input("Enter your choice (0-18): ")

    if choice == '0':
        print("Exiting the program.")
        break
    elif choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number (if applicable): "))

        if choice == '1':
            result = add(a, b)
        elif choice == '2':
            result = subtract(a, b)
        elif choice == '3':
            result = multiply(a, b)
        elif choice == '4':
            result = divide(a, b)
        elif choice == '5':
            result = square(a)
        elif choice == '6':
            result = cube(a)
        elif choice == '7':
            exponent = float(input("Enter the exponent: "))
            result = power(a, exponent)
        elif choice == '8':
            number = int(input("Enter an integer: "))
            result = is_even(number)
        elif choice == '9':
            number = int(input("Enter an integer: "))
            result = is_odd(number)
        elif choice == '10':
            number = int(input("Enter an integer: "))
            result = factorial(number)
        elif choice == '11':
            n = int(input("Enter the number of Fibonacci terms: "))
            result = fibonacci(n)
        elif choice == '12':
            string = input("Enter a string: ")
            result = reverse_string(string)
        elif choice == '13':
            string = input("Enter a string: ")
            result = is_palindrome(string)
        elif choice == '14':
            number = int(input("Enter an integer: "))
            result = sum_of_digits(number)
        elif choice == '15':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = max_of_two(a, b)
        elif choice == '16':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = min_of_two(a, b)
        elif choice == '17':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            c = float(input("Enter the third number: "))
            result = max_of_three(a, b, c)
        elif choice == '18':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            c = float(input("Enter the third number: "))
            result = min_of_three(a, b, c)

        print("Result: ", result)
    else:
        print("Invalid choice. Please select a valid option.")
