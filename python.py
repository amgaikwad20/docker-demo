#!/usr/bin/env python3

def greet(name):
    return f"Hello, {name}! Welcome to Python."

def add(a, b):
    return a + b

def main():
    name = input("Enter your name: ")
    print(greet(name))

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = add(num1, num2)
    print(f"Sum = {result}")

if __name__ == "__main__":
    main()
