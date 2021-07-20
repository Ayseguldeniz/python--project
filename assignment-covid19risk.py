age = input("Are you a cigarette addict older than 75 years old? (please Yes or No)").title().strip()  #Yes=True, No = False
if age == "Yes" :
    age = True
else :
    age = False

chronic = input("Do you have a severe chronic disease? (Please Yes or No)").title   #Yes=True, No = False

if chronic == "Yes" :
    chronic = True
else :
    chronic = False

immune = input("Is your immune system too weak? (Please Yes or No)").title()  #Yes=True, No = False

if immune == "Yes" :
    immune = True
else : 
    immune = False

risk = age or chronic or immune

if risk == True :
    print("You are in risky group")
else :
    print("You are not in risky group")