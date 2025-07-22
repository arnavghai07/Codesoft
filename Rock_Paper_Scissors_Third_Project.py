import random

options = {1: "Rock", 2: "Paper", 3: "Scissors"}

def get_winner(player, computer):
    if player == computer:
        return "It's a draw!"
    elif (player == 1 and computer == 3) or          (player == 2 and computer == 1) or          (player == 3 and computer == 2):
        return f"You win! {options[player]} beats {options[computer]}"
    else:
        return f"Computer wins! {options[computer]} beats {options[player]}"

def play_game():
    while True:
        try:
            print("\n🔹 Choose your move:")
            print("   1. Rock")
            print("   2. Paper")
            print("   3. Scissors")
            choice = int(input("Your choice (1-3): "))

            if choice not in options:
                print("Invalid number. Try again.")
                continue

            cpu_choice = random.choice(list(options.keys()))
            print(f"🧍 You: {options[choice]}")
            print(f"💻 Computer: {options[cpu_choice]}")

            print(get_winner(choice, cpu_choice))

            again = input("Play another round? (y/n): ").lower()
            if again not in ['y', 'yes']:
                print("👋 Thanks for playing!")
                break

        except ValueError:
            print("❗ Please enter a valid number between 1 and 3.")

if __name__ == "__main__":
    play_game()