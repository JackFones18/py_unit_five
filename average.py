
total = 0
count = 0

while True:
    user_input = input("Enter an integer (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    try:
        number = int(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if count > 0:
    average = total / count
    print("Average of the entered numbers:", average)
else:
    print("No numbers were entered.")
