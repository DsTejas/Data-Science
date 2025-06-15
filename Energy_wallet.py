# Energy Wallet - Virtual Point System

class EnergyWallet:
    def __init__(self, owner):
        self.owner = owner
        self.energy = 100  # everyone starts with 100 points

    def earn_energy(self, points):
        if points > 0:
            self.energy += points
            print(f"+{points} ⚡ earned! Current energy: {self.energy}")
        else:
            print("That’s not how energy works 😅")

    def use_energy(self, points):
        if points <= self.energy:
            self.energy -= points
            print(f"-{points} ⚡ used! Remaining energy: {self.energy}")
        else:
            print("Not enough energy. Go rest or earn more!")

    def status(self):
        print(f"🔋 {self.owner}'s Energy: {self.energy} ⚡")


# Interaction logic
def main():
    print("🌟 Welcome to your Energy Wallet 🌟")
    name = input("Who's the adventurer? 👉 ")
    player = EnergyWallet(name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Earn Energy")
        print("2. Use Energy")
        print("3. Check Energy Status")
        print("4. Exit")
        choice = input("Pick (1-4): ")

        if choice == "1":
            pts = int(input("Enter energy to add: "))
            player.earn_energy(pts)

        elif choice == "2":
            pts = int(input("Enter energy to use: "))
            player.use_energy(pts)

        elif choice == "3":
            player.status()

        elif choice == "4":
            print("Logging out... Stay energized! 💪")
            break

        else:
            print("Not a valid option. Try again.")

if __name__ == "__main__":
    main()
