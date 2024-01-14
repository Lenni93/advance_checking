budget_grup = int(input())
season = input()
count_fisher = int(input())
ship_rent = 0
discount = 0

if season == 'Spring':
    ship_rent = 3000
elif season == 'Autumn':
    ship_rent = 4200
elif season == 'Summer':
    ship_rent = 4200
elif season == 'Winter':
    ship_rent = 2600

if count_fisher <= 6:
    ship_rent = ship_rent * 0.90
elif count_fisher < 6 or count_fisher <= 11:
    ship_rent = ship_rent * 0.85
elif count_fisher > 11:
    ship_rent = ship_rent * 0.75

if count_fisher % 2 == 0 and season != 'Autumn':
    ship_rent *= 0.95

diff = abs(ship_rent - budget_grup)
if budget_grup >= ship_rent:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
