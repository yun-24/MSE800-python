numbers = [1, 2, 3, 4, 5]

def fac(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;

def factorial():
    factorials = {str(n): fac(n) for n in numbers}
    print(factorials)

if __name__ == '__main__':
    factorial()
