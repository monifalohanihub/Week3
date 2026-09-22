number = int(input("Enter a 3-digit positive integer: "))

if number < 100 or number > 999:
    print("Please enter a 3-digit positive integer.")
else:
    print("Decimal:", number)
    print("Binary:", bin(number))
    print("Octal:", oct(number))
    print("Hexadecimal:", hex(number))

    last_digit = number % 10
    print("Last digit:", last_digit)

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")