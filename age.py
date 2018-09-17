import datetime
from datetime import date
birthyear = int(input("enter your year of birth:"))
currentyear = int(datetime.date.today().strftime("%Y"))
useyear = currentyear-birthyear
def bB(useyear):
    if len(str(birthyear)) != 4:
        print("invalid year of birth") 
    if  useyear < 18:
        print("your are minor")
    if  (useyear >= 18  and useyear <= 35):
        print("your are a youth")
    if useyear > 35:
        print("your are an elder")
bB(useyear)
