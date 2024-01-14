type_flower = input()
amount_flower = int(input())
budget = int(input())
total = 0

if type_flower == 'Roses':
    total = amount_flower * 5
if amount_flower >= 80:
    total *= 0.10
if type_flower == 'Dalli':
    total = amount_flower * 3.80
elif amount_flower >= 90:
    total *= 0.15
if type_flower == 'Tulips':
    total = amount_flower * 2.80
if amount_flower >= 80:
    total *= 0.20
if type_flower == 'Narcissus':
    total = amount_flower * 3
elif amount_flower >= 120:
    total *= 0.15
if type_flower == 'Gladiolus':
    total = amount_flower * 2.50
elif amount_flower >= 80:
    total *= 0.25
    print(f"Hey, you have a great garden with {amount_flower} {type_flower} and {total:.2f} leva left.")
else:
    print(f"Not enough money, you need {total - budget:.2f} leva more.")
