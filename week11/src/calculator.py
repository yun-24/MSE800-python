def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True


def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result


def get_user_input():
    user_input = input("Enter one or two numbers (separated by space): ").strip()
    inputs = user_input.split()
    try:
        numbers = [int(i) for i in inputs]
        return numbers
    except ValueError:
        print("Invalid input")


def main():
    numbers = get_user_input()
    if numbers is None:
        return

    if len(numbers) == 1:
        num = numbers[0]
        print(f"Factorial of {num}: {factorial(num)}")
        print(f"{num} is a prime number: {is_prime(num)}")

    elif len(numbers) == 2:
        base, exponent = numbers
        print(f"{base} to the power of {exponent}: {power(base, exponent)}")

    else:
        print("Please enter either one or two numeric values.")


if __name__ == "__main__":
    main()
