day_stay = int(input())
type_room = input()
point = input()
price = 0
discount = 0

if type_room == 'room for one person':
    price = 18
    if day_stay < 10:
        discount = 0
    elif day_stay <= 10 or day_stay < 15:
        discount = 0
    elif day_stay < 15:
        discount = 0

if type_room == 'apartment':
    price = 25
    if day_stay < 10:
        discount = 0.30
    elif day_stay <= 10 or day_stay < 15:
        discount = 0.35
    elif day_stay < 15:
        discount = 0.50
elif type_room == 'president apartment':
    price = 35.00
    if day_stay < 10:
        discount = 0.10
    elif day_stay <= 10 or day_stay < 15:
        discount = 0.15
    elif day_stay > 15:
        discount = 0.20
total = price * (day_stay - 1)
total = price - total

if point == 'positive':
    total = total + (total * 0.25)
elif point == 'negative':
    total = total - (total * 0.10)

print(f"{total:.2f}")
