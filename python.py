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


    #!/usr/bin/env python3

def write_file(filename):
    with open(filename, "w") as file:
        file.write("Welcome to DevOps!\n")
        file.write("Python is useful for automation.\n")
    print(f"Data written to {filename}")

def read_file(filename):
    with open(filename, "r") as file:
        print("\nFile Contents:")
        print(file.read())

def main():
    filename = "devops.txt"

    write_file(filename)
    read_file(filename)

if __name__ == "__main__":
    main()
