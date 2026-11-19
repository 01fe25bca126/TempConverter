def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def main():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        c = float(input("Enter Celsius: "))
        print(f"{c} C = {c_to_f(c)} F")
    elif choice == "2":
        f = float(input("Enter Fahrenheit: "))
        print(f"{f} F = {f_to_c(f)} C")
    elif choice == "3":
        c = float(input("Enter Celsius: "))
        print(f"{c} C = {c_to_k(c)} K")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()