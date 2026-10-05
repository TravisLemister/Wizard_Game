class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health = self.health - damage

    def is_alive(self):
        return self.health > 0

# Inherited class
class Wizard(Character):
    def __init__(self, name, health, mana):
        super().__init__(name, health)
        self.mana = mana
        self.spells = ["Fire", "Ice", "Dark"]

    def choose_spell(self):
        print("Choose a spell:")
        for x in range(len(self.spells)):
            print(f"{x+1}. {self.spells[x]}")
        while True:
            choice = input("Enter spell number:")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(self.spells):
                    return self.spells[choice - 1]
            print("Invalid input. Try again.")


    # Inherited class
class Enemy(Character):
    def __init__(self, name, health):
        super().__init__(name, health)


def main():

    inventory = []  # list
    player_health = 50  # int
    location = "Town of Beginnings"  # string

    # Start the game
    print("Welcome to the Wizard Game!")

    name = input("Enter your wizard's name: ")

    wizard = Wizard(name, player_health, 50)
    enemy = Enemy("Angered Sorcerer", 30)

    print(f"{wizard.name} is in the {location}.")
    print(f"An {enemy.name} appears!")

    #Battle Loop
    while wizard.is_alive() and enemy.is_alive():
        decision= input("Select 'attack' to battle or 'run' to escape \n")

        if decision == 'attack':
            spell = wizard.choose_spell()
            print(f"You cast the {spell} spell")

            enemy.take_damage(15)
            print(f"{enemy.name}'s health: {enemy.health}")

            if enemy.is_alive():
                print(f"{enemy.name} counter attacks!")
                wizard.take_damage(10)
                print(f"{wizard.name}'s health: {wizard.health}")
            else:
                print(f"{enemy.name} has been defeated.")
                break

        elif decision == 'run':
            print("You ran away safely")
            break
        else:
            print("Decision not possible.")

#After Battle
    if wizard.is_alive() and not enemy.is_alive():
        print("You won the battle. Congrats!")

        inventory.append("Beginner Wizard Medal")

        print("You've earned the Beginner Wizard Medal! It has been added to your inventory.")

    elif not wizard.is_alive():
        print("You were defeated, better luck next time.")

main()
