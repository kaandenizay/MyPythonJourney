import csv

data_path = '../../data/'
input_filename = 'country_info.txt'

countries = {}
with open(data_path + input_filename) as country:
    country.readline()  # I m skipping first line
    for row in country:
        data = row.strip().split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict

print(countries)

while True:
    country = input('Enter country to see the capital city(0 exits): ').casefold()
    if country in countries.keys():
        if len(countries[country].get('capital')) > 0:
            print("The capital city is {} of the country {}".format(countries[country]['capital'], country.capitalize()))
        else:
            print("There is no capital city for {}".format(country.capitalize()))
    elif country == '0':
        break


for country in countries:
    if len(countries[country].get('capital')) > 0:
        print("The capital city is {} of the country {}".format(
            countries[country]['capital'], country.capitalize()))
    else:
        print("There is no capital city for {}".format(country.capitalize()))
