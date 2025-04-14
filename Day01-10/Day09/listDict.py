# Nesting List and Dictionaries

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
# travel_log = {
#     "France": ["paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# Print Lille
# print(travel_log["France"][1])

# List in List
nested_list = ["A", "B", ["C", "D"]]
# Print D
# print(nested_list[2][1])

# Dictionary >> Dictionary >> List
travel_log = {
    "France": {
        "num_time_visited":8,
        "cities_visited": ["paris", "Lille", "Dijon"]
        },
    "Germany": { 
        "cities_visits": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}
# Print Stuttgart
print(travel_log["Germany"]["cities_visits"][2])
