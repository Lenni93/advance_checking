from countryinfo import CountryInfo

country = input('Enter country name:')

country_info = CountryInfo(country)
print(f'Country Information')
print(f'Country name:', country_info.name())
print(f'Capital:', country_info.capital())
print(f'Population:', country_info.population())
print(f'Area:', country_info.area())
print('Flag:', country_info.flag())
print('Region:', country_info.region())
print('Currency:', country_info.currencies())
print('Borders:', country_info.borders())