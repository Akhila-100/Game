"""
Mystery Forest Adventure - A Choose Your Own Adventure Game
A beginner-friendly interactive story game with multiple endings.
"""

def clear_screen():
    """Clear the console screen for better readability."""
    print("\n" * 2)


def get_player_name():
    """Ask the player for their name."""
    print("=" * 40)
    print("   MYSTERY FOREST ADVENTURE")
    print("=" * 40)
    print()
    
    name = input("Enter your name: ").strip()
    
    # Handle empty name input
    if not name:
        name = "Adventurer"
    
    return name


def show_welcome_message(name):
    """Display the welcome message and story introduction."""
    clear_screen()
    print(f"Welcome {name}!")
    print()
    print("You are standing at the entrance of a mysterious forest.")
    print("Legend says treasure, magic, and danger lurk within.")
    print()


def get_choice(prompt, valid_options):
    """
    Get valid user input for a choice.
    
    Args:
        prompt: The question to ask the player
        valid_options: List of valid choice numbers/strings
    
    Returns:
        The player's valid choice
    """
    while True:
        try:
            choice = input(prompt).strip()
            
            if choice in valid_options:
                return choice
            else:
                print(f"❌ Invalid choice! Please enter one of: {', '.join(valid_options)}")
        except KeyboardInterrupt:
            print("\n\nThanks for playing!")
            exit()


def forest_entrance(name):
    """First decision point - entering the forest."""
    clear_screen()
    print("What do you want to do?")
    print()
    print("1. Enter the forest")
    print("2. Walk away and go home")
    print()
    
    choice = get_choice("Choose (1 or 2): ", ["1", "2"])
    
    if choice == "1":
        return forest_paths(name)
    else:
        return ending_coward(name)


def forest_paths(name):
    """Second decision point - choosing a path in the forest."""
    clear_screen()
    print("You bravely enter the forest and find two paths.")
    print()
    print("1. Take the dark path (mysterious)")
    print("2. Take the river path (safer)")
    print("3. Climb a tree to look around")
    print()
    
    choice = get_choice("Choose (1, 2, or 3): ", ["1", "2", "3"])
    
    if choice == "1":
        return dark_path_adventure(name)
    elif choice == "2":
        return river_path_adventure(name)
    else:
        return tree_adventure(name)


def dark_path_adventure(name):
    """Adventure on the dark path."""
    clear_screen()
    print("You venture down the dark, winding path.")
    print("Strange sounds echo through the trees...")
    print()
    print("Suddenly, you see a glowing cave entrance!")
    print()
    print("1. Enter the glowing cave")
    print("2. Turn back and find another route")
    print()
    
    choice = get_choice("Choose (1 or 2): ", ["1", "2"])
    
    if choice == "1":
        return ending_treasure(name)
    else:
        return ending_lost(name)


def river_path_adventure(name):
    """Adventure on the river path."""
    clear_screen()
    print("You follow the gentle sound of flowing water.")
    print("The path opens into a beautiful clearing...")
    print()
    print("You discover a hidden treasure chest by the riverside!")
    print("However, a friendly forest guardian is sitting nearby.")
    print()
    print("1. Take the treasure and run")
    print("2. Talk to the guardian first")
    print()
    
    choice = get_choice("Choose (1 or 2): ", ["1", "2"])
    
    if choice == "1":
        return ending_treasure(name)
    else:
        return ending_friendship(name)


def tree_adventure(name):
    """Adventure by climbing a tree."""
    clear_screen()
    print("You climb a tall oak tree to get a better view.")
    print("From the top, you can see the entire forest!")
    print()
    print("You spot three interesting locations:")
    print("1. A glowing mountain in the distance")
    print("2. A mysterious castle")
    print("3. A peaceful village")
    print()
    
    choice = get_choice("Where do you go (1, 2, or 3): ", ["1", "2", "3"])
    
    if choice == "1":
        return ending_treasure(name)
    elif choice == "2":
        return ending_lost(name)
    else:
        return ending_friendship(name)


def ending_treasure(name):
    """Ending 1: Player finds treasure."""
    clear_screen()
    print("=" * 40)
    print("🎉 TREASURE ENDING 🎉")
    print("=" * 40)
    print()
    print(f"Congratulations {name}!")
    print()
    print("You found an ancient treasure chest filled with")
    print("gold coins, jewels, and mysterious artifacts!")
    print()
    print("You return home wealthy and famous.")
    print("People tell stories of your adventure for years!")
    print()
    return "treasure"


def ending_friendship(name):
    """Ending 2: Player makes a friend."""
    clear_screen()
    print("=" * 40)
    print("💚 FRIENDSHIP ENDING 💚")
    print("=" * 40)
    print()
    print(f"Wonderful, {name}!")
    print()
    print("The forest guardian becomes your friend and guide.")
    print("Together, you explore the magical forest and learn")
    print("its ancient secrets.")
    print()
    print("You gain wisdom beyond measure and true companionship!")
    print()
    return "friendship"


def ending_lost(name):
    """Ending 3: Player gets lost."""
    clear_screen()
    print("=" * 40)
    print("😕 LOST ENDING 😕")
    print("=" * 40)
    print()
    print(f"Oh no, {name}!")
    print()
    print("You wander deeper into the forest and lose your way.")
    print("After hours of wandering, you find a ranger's cabin.")
    print()
    print("The ranger gives you food and shelter, then guides you")
    print("safely back home. It was quite the adventure!")
    print()
    return "lost"


def ending_coward(name):
    """Ending 4: Player walks away."""
    clear_screen()
    print("=" * 40)
    print("🏃 COWARD ENDING 🏃")
    print("=" * 40)
    print()
    print(f"Hmm, {name}...")
    print()
    print("You decide the forest is too dangerous and walk away.")
    print("You return home safely, but you'll always wonder...")
    print()
    print("What amazing things might you have found inside?")
    print()
    return "coward"


def show_final_message(name, ending):
    """Display the final message based on the ending."""
    clear_screen()
    print("=" * 40)
    print("         GAME OVER - THANKS FOR PLAYING!")
    print("=" * 40)
    print()
    print(f"Player: {name}")
    print(f"Ending: {ending.upper()}")
    print()
    print("Would you like to play again? (yes/no)")
    print()


def play_game():
    """Main game function that controls the flow."""
    player_name = get_player_name()
    show_welcome_message(player_name)
    
    # Start the adventure
    ending_type = forest_entrance(player_name)
    
    # Show the final message
    show_final_message(player_name, ending_type)
    
    # Ask if they want to play again
    replay = get_choice("Your choice (yes or no): ", ["yes", "no", "y", "n"])
    
    if replay in ["yes", "y"]:
        clear_screen()
        play_game()  # Restart the game
    else:
        clear_screen()
        print("Thanks for playing Mystery Forest Adventure!")
        print("Goodbye!\n")


def main():
    """Entry point for the game."""
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nThanks for playing Mystery Forest Adventure!")
        print("Goodbye!\n")


if __name__ == "__main__":
    main()
