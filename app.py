def add(a: int, b: int) -> int:
    return a + b
# Subtract two numbers.
def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: float, b: float) -> float:
    return a / b

if __name__ == "__main__":
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    print(f"6 / 3 = {divide(6, 3)}")
