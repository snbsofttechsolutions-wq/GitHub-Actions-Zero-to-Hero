import sys

def sum_two_numbers(a, b):
    return a + b

if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(f"Total: {sum_two_numbers(num1, num2)}")
