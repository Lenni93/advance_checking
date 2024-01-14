city = input()
sales = float(input())
trade = 0

if city == 'Sofia':
    if 0 <= sales <= 500:
        trade = (sales * 5) / 100
    elif 0 <= sales <= 500:
        trade = (sales * 7) / 100
    elif 1000 < sales < 10000:
        trade = (sales * 8) / 100
    elif sales <= 500:
        trade = (sales * 12) / 100

elif city == 'Varna':
    if 0 <= sales <= 500:
        trade = ((sales * 4.5) / 100)
    elif 500 < sales <= 1000:
        trade = (sales * 7.5) / 100
    elif 1000 < sales <= 10000:
        trade = (sales * 10) / 100
    elif sales > 10000:
        trade = (sales * 13) / 100

elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        trade = (sales * 5.5) / 100
    elif 0 <= sales <= 500:
        trade = (sales * 8) / 100
    elif 1000 < sales < 10000:
        trade = (sales * 12) / 100
    elif sales <= 500:
        trade = (sales * 14.5) / 100
    print(f'{trade:.2f}')

    print('error')
