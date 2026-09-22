text = input("Enter a string with at least 8 characters: ")

if len(text) < 8:
    print("Please enter a string with at least 8 characters.")
else:
    # Display ASCII value of each character
    for char in text:
        print(char, "=", ord(char))

    # Capitalize characters at positions 2, 4, 6, 8, ...
    modified = ""

    for i in range(len(text)):
        char = text[i]

        if (i + 1) % 2 == 0:
            ascii_value = ord(char)

            if ascii_value >= 97 and ascii_value <= 122:
                ascii_value = ascii_value - 32
                char = chr(ascii_value)

        modified = modified + char

    print("Final modified string:", modified)