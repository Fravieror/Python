from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)
print(table)








