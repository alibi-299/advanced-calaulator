def add(p, q):
    return p + q


def subtract(p, q):
    return p - q


def multiply(p, q):
    return p * q


def power(p, q):
    return p ** q


def divide(p, q):
    if q == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return p / q


def floor_divide(p, q):
    if q == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return p // q


def modulo(p, q):
    if q == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return p % q


def get_number(prompt):
    while True:
        user_value = input(prompt).strip()
        try:
            return float(user_value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def format_number(number):
    return str(number)


def main():
    print("Advanced Calculator")
    print("Operations: +, -, *, **, /, //, %")
    print("Type '=' when you are finished.")

    total = 0.0
    print(f"Starting number: {format_number(total)}")

    while True:
        print(f"\nCurrent number: {format_number(total)}")
        operator = input("Enter operator or type '=' to stop: ").strip()

        if operator == '=':
            print(f"\nDone with numbers. Final number: {format_number(total)}")
            break

        if operator not in ['+', '-', '*', '**', '/', '//', '%']:
            print("Invalid operator. Please type +, -, *, **, /, //, or %.")
            continue

        next_num = get_number(f"Enter number to {operator} by: ")

        try:
            if operator == '+':
                total = add(total, next_num)
                print(f"Final number after addition: {format_number(total)}")
            elif operator == '-':
                total = subtract(total, next_num)
            elif operator == '*':
                total = multiply(total, next_num)
            elif operator == '**':
                total = power(total, next_num)
            elif operator == '/':
                total = divide(total, next_num)
            elif operator == '//':
                total = floor_divide(total, next_num)
            elif operator == '%':
                total = modulo(total, next_num)
        except ZeroDivisionError:
            print("Error: Cannot divide by zero. Total remains unchanged.")


if __name__ == "__main__":
    main()
