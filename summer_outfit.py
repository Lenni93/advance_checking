degrees = int(input())
type_day = input()
clothes = ""
shoes = ""

if type_day == "Morning":
    if 10 <= degrees <= 18:
        clothes = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degrees <= 24:
        clothes = "Shirt"
        shoes = "Moccasins"
    elif degrees >= 25:
        clothes = "T-Shirt"
        shoes = "Sandals"
    print(f"It's {degrees} degrees, get your {clothes} and {shoes}.")

if type_day == "Afternoon":
    if 10 <= degrees <= 18:
        clothes = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        clothes = "T-Shirt"
        shoes = "Sandals"
    elif degrees >= 25:
        clothes = "Swim Suit"
        shoes = "Barefoot"
    print(f"It's {degrees} degrees, get your {clothes} and {shoes}.")

if type_day == 'Evening':
    if 10 <= degrees <= 18:
        clothes = "Shirt"
        shoes = "Moccasins"
    elif 18 < degrees <= 24:
        clothes = "Shirt"
        shoes = "Moccasins"
    elif degrees >= 25:
        clothes = "Shirt"
        shoes = "Moccasins"
    print(f"It's {degrees} degrees, get your {clothes} and {shoes}.")
