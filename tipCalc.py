print("Welcome to the tip calculator")
bill = float(input("what is the total Bill :"))
percentageOfTip = int(input("what is the percentage of tip you like to give : 10 , 12 or 15"))
noPeople = int(input("How many people to splite the bill :"))
tipAsPercent = percentageOfTip/100
totalTipAmounnt = tipAsPercent*bill
billWihtTheTip =totalTipAmounnt + bill
eachPay=billWihtTheTip/noPeople
print(f"Each person should pay : $ {eachPay}")