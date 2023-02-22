import random
"""
    Check if the entered value is a valid integer in the range 1-49 and has not been used before.

    Args:
        lotto_number (str): A string containing the user's entered number to be validated.
        used_numbers (list): A list of numbers that have already been used.

    Returns:
        bool: True if the entered value is a valid integer and has not been used before, False otherwise.
    """


# helper function to check if the entered value is a valid integer in the range 1-49
def is_valid_number(lotto_number, used_numbers):
    try:
        # try to convert the entered value to integer
        lotto_number = int(lotto_number)
    except ValueError:
        # if it failed to convert, the value is invalid
        return False
    if lotto_number in used_numbers:
        # if the entered value has already been used, the value is invalid
        return False
    if lotto_number < 1 or lotto_number > 49:
        # if the entered value is not in the range 1-49, the value is invalid
        return False
    # otherwise the value is correct
    return True


# get the typed numbers from the user
print("Type 6 unique numbers from 1 to 49:")
typed_numbers = []
while len(typed_numbers) < 6:
    number = input(f"Number {len(typed_numbers)+1}: ")
    if not is_valid_number(number, typed_numbers):
        print("Invalid number. Try again.")
    else:
        typed_numbers.append(int(number))

# sort the entered numbers in ascending order and display on the screen
typed_numbers.sort()
print(f"Your numbers: {typed_numbers}")

# randomly pick 6 numbers from 1-49 and display them on the screen
drawn_numbers = random.sample(range(1, 50), 6)
drawn_numbers.sort()
print(f"Drawn numbers: {drawn_numbers}")

# calculate the number of hits
matches = set(typed_numbers) & set(drawn_numbers)
num_matches = len(matches)

# display a message with information about the number of hits
if num_matches == 3:
    print("Congratulations! You hit 3 numbers.")
elif num_matches == 4:
    print("Congratulations! You hit 4 numbers.")
elif num_matches == 5:
    print("Congratulations! You hit 5 numbers.")
elif num_matches == 6:
    print("Congratulations! You hit 6 numbers.")
else:
    print("Sorry, you didn't hit enough numbers. Try again next time.")
