print("Welcome to the Text-Based Adventure Game!")
name = input("What is your name? ")

print(f"Hello {name}! You find yourself in a dark forest. You come across a path that splits into two. Do you go left or right?")

choice = input("Enter 'left' or 'right': ")

if choice == "left":
    print("You encounter a mystical creature. It leads you to a hidden treasure!")
else:
    print("You come across a ferocious dragon. Choose to fight or run!")

    action = input("Enter 'fight' or 'run': ")

    if action == "fight":
        print("You bravely fight the dragon and emerge victorious!")
    else:
        print("You escape from the dragon and find a chest full of gold coins.")

print("The end of the adventure!")

