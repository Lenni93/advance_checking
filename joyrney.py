budget = float(input())
season = input()
place = ''
country = ''
if budget <= 100:
    country = 'Bulgaria'
    if season == 'summer':
        budget = budget - (budget * 0.70)
        place = 'Camp'
    elif season == 'winter':
        budget = budget - (budget * 0.30)
        place = 'Hotel'

elif budget <= 1000:
    country = 'Balkans'
    if season == 'summer':
        budget = budget - (budget * 0.60)
        place = 'Camp'
    elif season == 'winter':
        budget = budget - (budget * 0.20)
        place = 'Hotel'
        country = 'Balkans'

if budget > 1000:
    country = 'Europe'
    budget = budget - (budget * 0.10)
    place = 'Hotel'

print(f"Somewhere in {country}")
print(f" {place} - {budget:.2f}")
