initial = 6000
yearlyInterest = 0.09
recurentInvest = 200
investWeekSpan = 4

weeklyInterest = yearlyInterest / 52

nbYear = int(input("Nombre d'année de calcul souhaité\n"))
nbWeek = nbYear * 52

interest = 0
weekGrowth = 0
patrimoine = initial

for i in range(1, nbWeek):
    weeklyIncome = patrimoine * weeklyInterest

    interest = interest + weeklyIncome

    while interest > 50:
        interest = interest - 50
        patrimoine = patrimoine + 50
        

    if weeklyIncome > 50 and weekGrowth == 0:
        weekGrowth = i

    #je rajoute tous les mois 300€
    if i % investWeekSpan == 0:
        patrimoine = patrimoine + recurentInvest

print("patrimoine:", patrimoine)
print("weeklyIncome:", weeklyIncome)
dateYearGrowth = weekGrowth / 52
dateWeekGrowth = int((dateYearGrowth - int(dateYearGrowth)) * 52)
dateYearGrowth = int(dateYearGrowth)
print(f"date du dépassement: Y{dateYearGrowth}, W{dateWeekGrowth}")