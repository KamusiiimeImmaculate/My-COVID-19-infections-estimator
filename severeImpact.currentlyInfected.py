reportedCases = "2747"
a = "currentlyInfected"
b = "projectednumberofinfectionsafter28days"
c = "impact.currentlyInfected"
d = "severeImpact.currentlyInfected"
e = "reportedCases * 50"
f = "e * (2 to the power of 9)"  #currentlyInfected x 512

#import reportedCases
#import population
population = 1380614
avgDailyIncomeInUSD = 5
currentlyInfected = reportedCases * 10
avgDailyIncomePopulation = 0.71

today = reportedCases.date.today()
infected_By_Requested = population.monthrange(today.year, today.month)
severeImpactcurrentlyInfected = reportedCases* 512 #(2 to the power of 9)


print(severeImpactcurrentlyInfected)
print(infected_By_Requested)