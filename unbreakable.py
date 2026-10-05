# unbreakable.py - a program that keeps running no matter what the user types.
# Two kinds of problems are handled differently:
#   * bad input    -> not a number at all (int() raises ValueError -> use try/except)
#   * unwise input -> a valid number that makes no sense (use an if check)

while True:
    text = input("Enter your age (or 'q' to quit): ")

    if text.lower() == "q":
        print("Goodbye!")
        break

    try:
        age = int(text)          # bad input ("abc") raises ValueError here
    except ValueError:
        print("Please type a whole number, like 25.")
        continue                 # keep the program running

    if age < 0 or age > 120:     # unwise input: a number, but not a sensible age
        print("That age doesn't look realistic. Try again.")
    else:
        print(f"Thanks! Next year you will be {age + 1}.")
