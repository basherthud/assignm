import random

class Character:
    def __init__(self, name, hp, min_damage, max_damage):
        self.name = name
        self.hp = hp
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self, target):
        damage_dealt = random.randint(self.min_damage, self.max_damage)
        target.hp -= damage_dealt
        print(f"{self.name} attacks {target.name} for {damage_dealt} damage!")

    def stats(self):
        print(f"{self.name}'s Stats /n Your Health Is:  {self.hp} /n Your Damage is:  {self.min_damage, self.max_damage}")

    def heal(self):
        self.hp += 10
        print(f"{self.name} Healing Aura Begins!")

    def special_ability(self, target):
        pass

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 130, 20, 40)

    def special_ability(self, target):
        print(f"{self.name} Charges With Shield Slam!")
    def special_ability2(self, target):
        print(f"{self.name} Actives Enrage!")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 80, 30, 60)

    def special_ability(self, target):
        print(f"{self.name} Casts Fireball!")
    
    def special_ability2(self, target):
        print(f"{self.name} Casts Arcane Surge!!")

class Ranger(Character):
    def __init__(self, name):
        super().__init__(name, 90, 25, 50)

    def special_ability(self, target):
         poison = 60
         target.hp -= poison
         print(f"{self.name} uses Poison Arrow!")

    def special_ability2(self, target):
     print(f"{self.name} Marked For Death")

class Monk(Character):
    def __init__(self, name):
        super().__init__(name, 120, 15, 30)

    def special_ability(self, target):
        print(f"{self.name} Casts Holy Aura!")

    def special_ability2(self, target):
        Bash = 75
        target.hp -= Bash
        print(f"{self.name} Invokes Great Monkey Bash!")

class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name,150,25,35)

    def regenerate_health(self):
        regen_amount = random.randint(10,20)
        self.hp += regen_amount
        print(f"{self.name} regenerates {regen_amount} health.")

    def special_ability(self, target):
        shadow = 30
        target.hp -= shadow
        print(f"{self.name} Casts Shadow Bolt!")

    def special_ability2(self, target):
        banana = 3
        target.hp -= banana
        print(f"{self.name} Conjures Banana Bolt!")

def character_choice():
    print("Choose your character:")
    print("1. the Warrior")
    print("2. the Mage")
    print("3. the Ranger")
    print("4. the Monk")
    choice = input("Enter the number of your chosen character: ")
    name = input("What is your Characters Name?: ")
    if choice == "1":
        return Warrior(name)
    elif choice == "2":
        return Mage(name)
    elif choice == "3":
        return Ranger(name)
    elif choice == "4":
        return Monk(name)
    else:
        print("Invalid Choice Your A Monk Now")
    return Monk(name)

def fight(character,wizard):
    while character.hp > 0  and wizard.hp > 0:
        if character.hp > 0:
            current_character = character
        print("\nChoose an action for", current_character.name)
        print("1. Attack")
        print("2. Heal")
        print("3. Special Ability")
        print("4. Special Ability 2")
        print("5. Checks Stats")
        action = input("Enter your choice: ")

        if action == "1":
            character.attack(wizard)
            print(f"Player hp is:{character.hp} Wizard hp is: {wizard.hp}")
        elif action == "2":
            character.heal()
            print(f"Player hp is:{character.hp} Wizard hp is: {wizard.hp}")
        elif action == "3":
            character.special_ability(wizard)
            print(f"Player hp is:{character.hp} Wizard hp is: {wizard.hp}")
        elif action == "4":
            character.special_ability2(wizard)
            print(f"Player hp is:{character.hp} Wizard hp is: {wizard.hp}")
        elif action == "5":
            character.stats()
            print(f"Player hp is:{character.hp} Wizard hp is: {wizard.hp}")
        else:
            ("Invalid!")
        if wizard.hp > 0:
            wizard.regenerate_health()
            wizard.special_ability(character)
            wizard.special_ability2(character)
        if character.hp <= 0:
            print("The heroes have been defeated! The Evil Wizard plagues pillages the village!")
        elif wizard.hp <=0:
            print("The heroes emerge victorious! The village is saved!.")
def main():
    wizard = EvilWizard("The Dark One")
    character = character_choice()
    fight(character, wizard)

if __name__ == "__main__":
    main()
