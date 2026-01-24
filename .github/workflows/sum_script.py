import sys

def sum_two_numbers(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    # Standard check to ensure two arguments are passed
    if len(sys.argv) > 2:
        val1 = float(sys.argv[1])
        val2 = float(sys.argv[2])
        result = sum_two_numbers(val1, val2)
        print(f"The sum of {val1} and {val2} is: {result}")
    else:
        print("Please provide two numbers as arguments.")
