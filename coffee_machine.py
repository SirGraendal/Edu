class CoffeeMachine:

    recipe = [[250, 0, 16, 4],
              [350, 75, 20, 7],
              [200, 100, 12, 6]]

    message = {"main": "\nWrite action (buy, fill, take, remaining, exit):",
               "fill_water": "\nWrite how many ml of water do you want to add:",
               "fill_milk": "Write how many ml of milk do you want to add:",
               "fill_beans": "Write how many grams of coffee beans do you want to add:",
               "fill_cups": "Write how many disposable cups of coffee do you want to add:",
               "buy": "\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"}

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.status = "main"

        print("Write action (buy, fill, take, remaining, exit):")

    def cmd(self, choice):
        # Fill
        if self.status == "main" and choice == "fill":
            self.status = "fill_water"

        elif self.status == "fill_water" and choice.isdigit():
            self.water += int(choice)
            self.status = "fill_milk"

        elif self.status == "fill_milk" and choice.isdigit():
            self.milk += int(choice)
            self.status = "fill_beans"

        elif self.status == "fill_beans" and choice.isdigit():
            self.beans += int(choice)
            self.status = "fill_cups"

        elif self.status == "fill_cups" and choice.isdigit():
            self.cups += int(choice)
            self.status = "main"

        # BUY
        elif self.status == "main" and choice == "buy":
            self.status = "buy"

        elif self.status == "buy":

            if choice == "back":
                self.status = "main"
                print()

            if choice.isdigit():
                choice = int(choice)
                choice -= 1
                if self.water < CoffeeMachine.recipe[choice][0]:
                    print("Sorry, not enough water!")
                elif self.milk < CoffeeMachine.recipe[choice][1]:
                    self.status = "main"
                elif self.beans < CoffeeMachine.recipe[choice][2]:
                    print("Sorry, not enough coffeebeans!")
                elif self.cups < 1:
                    print("Sorry, not enough cups!")
                else:
                    print("I have enough resources, making you a coffee!")
                    self.water -= CoffeeMachine.recipe[choice][0]
                    self.milk -= CoffeeMachine.recipe[choice][1]
                    self.beans -= CoffeeMachine.recipe[choice][2]
                    self.money += CoffeeMachine.recipe[choice][3]
                    self.cups -= 1

            self.status = "main"

        elif self.status == "main" and choice == "take":
            print("I gave you ${}".format(self.money))
            self.money = 0

        elif self.status == "main" and choice == "remaining":
            print("\nThe coffee machine has:")
            print(self.water, " of water")
            print(self.milk, " of milk")
            print(self.beans, " of coffee beans")
            print(self.cups, " of disposable cups")
            print("$" + str(self.money) + " of money")

        # exit
        elif self.status == "main" and choice == "exit":
            return False

        print(self.message[self.status])
        return True


saeco = CoffeeMachine()
running = True

while running:
    running = saeco.cmd(input())
