def roll_call_dwarves(names):
    i=1
    for name in names:
        print(f"{i}. {name}")
        i+=1

dwarves = ["Doc", "Dopey", "Bashful", "Grumpy"]
roll_call_dwarves(dwarves)

def summon_captain_planet(calls):
    updated = [x[0].upper() + x[1:] + "!" for x in calls]
    print(updated)
    return updated

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]
summon_captain_planet(planeteer_calls)

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) >= 4:
            print(True)
            return False
        else:
            print(False)
            return True

short_words = ["puff", "go", "two"]
long_planeteer_calls(short_words)

assorted_words = ["two", "go", "industrious", "bop"]
long_planeteer_calls(assorted_words)

def find_the_cheese(foods):
    for food in foods:
        if food in ["cheddar", "gouda", "camembert"]:
            print(food)
            return food
            break
    else:
        None
        
snacks = ["crackers", "gouda", "thyme"]
find_the_cheese(snacks)

soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
find_the_cheese(soup)