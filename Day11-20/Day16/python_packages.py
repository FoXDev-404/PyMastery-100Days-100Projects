# Python Packages
# To install a package "pip install <package_name>"

# Eg. pip install prettytable

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l" # Left align

print(table)
