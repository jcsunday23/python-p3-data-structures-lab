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
    foods_name=[]
    for food in spicy_foods:
        food_name = food["name"]
        foods_name.append(food_name)
    return foods_name
    

def get_spiciest_foods(spicy_foods):
    spiciest_food=[]
    for spice in spicy_foods:
        if spice["heat_level"] > 5:
            spices = spice
            spiciest_food.append(spices)
    return spiciest_food


    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_levels = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_levels}')
      
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food           

    pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat = "🌶" * food["heat_level"]
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat}')

def get_average_heat_level(spicy_foods):
    total_heat = 0
    for food in spicy_foods:
        total_heat += food["heat_level"]
    return total_heat // len(spicy_foods)
    
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
