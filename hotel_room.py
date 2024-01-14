month = input()
amount_night = int(input())
studio = 0
flat = 0

price_studio = 0
price_flat = 0
if month == 'May' or month == 'October':
    studio = 50
    flat = 65
    if amount_night > 14:
        studio *= 0.70
        price_flat = amount_night * flat
    elif amount_night > 7:
        studio *= 0.95

if month == 'June' or month == 'September':
    studio = 75.20
    flat = 68.70
    if amount_night > 14:
        studio *= 0.80
elif month == 'July' or month == 'August':
    studio = 76
    flat = 77
if amount_night > 14:
    flat *= 0.90

price_studio = studio * amount_night
price_flat = flat * amount_night
print(f"Apartment: {price_flat:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
