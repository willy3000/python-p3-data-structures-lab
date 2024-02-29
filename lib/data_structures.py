spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_foods_strings = []
    for x in spicy_foods:
        spicy_foods_strings.append(x["name"])
        print(spicy_foods)
    return spicy_foods_strings
    

def get_spiciest_foods(spicy_foods):
    spicy_foods_strings = []
    for x in spicy_foods:
        if(x["heat_level"]>5):
            spicy_foods_strings.append(x)
    return spicy_foods_strings

def print_spicy_foods(spicy_foods):
    for x in spicy_foods:
        print(x["name"]+" ("+x["cuisine"]+")"+" | "+ "Heat Level: "+"🌶"*x["heat_level"])

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    new_cuisines = {}
    for x in spicy_foods:
        if(x["cuisine"] == cuisine):
            new_cuisines = x
    return new_cuisines

def print_spiciest_foods(spicy_foods):
    for x in spicy_foods:
        if(x['heat_level']> 5):
            print(x["name"]+" ("+x["cuisine"]+")"+" | "+ "Heat Level: "+"🌶"*x["heat_level"])


def get_average_heat_level(spicy_foods):
    sum = 0
    for x in spicy_foods:
        sum+=x["heat_level"]
    return sum/len(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods
