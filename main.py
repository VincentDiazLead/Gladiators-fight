import os, time
from random import randint
import pandas as pd

def cls():
    os.system("cls || clear")

class Gladiator:
    def __init__(self, name: str = "admin", health: float = 100, 
                 damage: float = 50, armor: float = 100):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.names = ["Noah", "Liam", "Robert", 
        "Lucas", "Benjamin", "Elijah", 
        "Thomas", "Henry", "Charles", 
        "John", "James", "William"]

    def get_options(self):
        options = {
            'name': self.name,
            'health': self.health,
            'damage': self.damage,
            'armor': self.armor,
        }
        return options

    def set_random_stats(self, names: list):
        self.name = names[randint(0, len(names) - 1)]
        self.health = float(randint(90, 120))
        self.damage = float(randint(20, 30))
        self.armor = float(randint(20, 50))

        return self.get_options()
    
def get_user(user1: dict, user2: dict):
    users = {'': user1,
             ' ': user2}
    df = pd.DataFrame(users) 
    
    print(df)


def attack(*user1: dict, **user2: dict):
    user1['health'] -= (randint(0, user2['damage'] + 1)) / 100 * user1['armor']

class Game:
    def __init__(self) -> None:
        pass

def game():
    os.system('cls || clear')
    game = True

    names = ["Noah", "Liam", "Robert", "Lucas", "Benjamin", "Elijah", "Thomas", "Henry", "Charles", "John", "James", "William"]

    user1 = Gladiator()
    user1 = user1.set_random_stats(names)

    user2 = Gladiator()
    user2 = user2.set_random_stats(names)

    get_user(user1, user2)

    while game:
        if (float(user1['health']) > 0)&(float(user2['health']) > 0):
            user1['health'] -= (randint(0, user2['damage'] + 1)) / 100 * user1['armor']
            user2['health'] -= (randint(0, user1['damage'] + 1)) / 100 * user2['armor']
            print(f"Здоровье гладиатора {user1['name']}: {user1['health']}\nЗдоровье гладиатора {user2['name']}: {user2['health']}")
            time.sleep(2)
            
        else:
            if user1["health"] > user2['health']:
                print(f"Победил: {user1['name']}")  
            elif user1['health'] == user2["health"]:
                print(f"Ничья", user1["health"], user2["health"])   
            else:
                print(f"Победил: {user2['name']}")     
            # for i in range(7):
            #     print(f"Перезагрузка")
            #     time.sleep(1)
            cls()
            break

            

if __name__ == '__main__':
    game()
