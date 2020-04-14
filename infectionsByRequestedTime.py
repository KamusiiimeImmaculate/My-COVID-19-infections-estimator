reportedCases = "2747"
a = "reportedCases"
c = "projectednumberofinfectionsafter28days"
d = "impact.currentlyInfected"
e = "severeImpact.currentlyInfected"
f = "severeCasesByRequestedTime"
g = "casesForVentilatorsByRequestedTime"

currentlyInfected = "a * 10"

b = "currentlyInfected"

c = "b *(2 to the power of 9)"  #currentlyInfected x 512
e = "c *50"
f = "15% * e"
g = "2% * e"
g = "h"

#import reportedCases
#import population
avgDailyIncomeInUSD = 5
currentlyInfected = reportedCases * 10
avgDailyIncomePopulation = 0.71

today = reportedCases.date.today()
#infected_By_Requested = population.monthrange(today.year, today.month)
severeImpactcurrentlyInfected = reportedCases* 512 #(2 to the power of 9)
Infected_By_Requested_Time = severeImpactcurrentlyInfected * (15/100)


print(Infected_By_Requested_Time)