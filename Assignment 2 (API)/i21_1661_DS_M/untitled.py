import sys
import requests
lst = sys.argv
print(lst)
if len(lst) > 4 or len(lst) < 4:
    print("[ERROR] You need to provide 3 arguments in the following order: <date> <currency1> <currency2> ")
else:
    currencies = requests.get(f"https://api.frankfurter.app/currencies")
    correct_currencies = currencies.json()
    if lst[2].upper() not in correct_currencies or lst[3].upper() not in correct_currencies:
        print("This is not a valid currency code")
        exit()
    dates = lst[1]
    hyphen = "-"
    if hyphen not in dates:
        print("Provided date is invalid.")
        exit()
    else:
        splitter = dates.split("-")
        year=int(splitter[0])
        month=int(splitter[1])
        date=int(splitter[2])
        if year < 1999 or year > 2022 or month > 12 or month < 1 or date > 31 or date < 1 :
            print("Provided date is invalid.")
            exit()
        response = requests.get(f"https://api.frankfurter.app/{lst[1]}?from={lst[2]}&to={lst[3]}")
        print(f"The conversion rate on {lst[1]} from {lst[2].upper()} to {lst[3].upper()} is {response.json()['rates'][lst[3].upper()]}")
        inverse_response = requests.get(f"https://api.frankfurter.app/{lst[1]}?from={lst[3]}&to={lst[2]}")
        print(f"The inverse rate was {inverse_response.json()['rates'][lst[2].upper()]}")
    
    