"""
Demonstrates the concept of variable scope in Python:
- Local Scope
- Global Scope
- No Block Scope
"""

# Global Scope Example
enemies = 1


def increase_enemies():
    """
    Function demonstrating local variable with the same name as a global one.
    """
    enemies = 2  # Local scope
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope Example
def drink_potion():
    """
    Demonstrates local scope with a variable only accessible inside the function.
    """
    potion_strength = 2
    print(f"Potion strength inside function: {potion_strength}")


drink_potion()
# The following line would cause an error because potion_strength is not defined outside the function.
# print(potion_strength)


# Global Scope Accessed Inside Function
player_health = 10


def game():
    """
    Accesses global variable 'player_health' from within a nested function.
    """

    def drink_potion():
        potion_strength = 2
        print(f"Accessing global variable inside nested function: {player_health}")

    drink_potion()


game()
print(f"Player health in global scope: {player_health}")

# No Block Scope in Python
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    """
    Demonstrates that Python does not have block-level scope like other languages.
    Variables declared inside if/for/while blocks are still accessible within the function.
    """
    if game_level < 5:
        new_enemy = enemies[0]  # Still accessible outside the if-block within this function
    print(f"Enemy created based on level: {new_enemy}")


create_enemy()
