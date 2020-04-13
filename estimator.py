
{
"data":{
    "region": {
        "name": "Africa",
        "AvgAge": 19.7,
        "avgDailyIncomeInUSD":5,
        "avgDailyIncomePopulation": 0.71
         },
    "periodType": "days",
    "timeToElapse": 58,
    "reportedCases": 2747,
    "population": 1380614
     },
"estimate": {
    "impact":{
        "currentlyInfected": 27470,
        "infectionByRequestedTime":112517120,
        "severeCasesByRequestedTime": 16877562,
        "hospitalBedsByRequestedTIME": -16639962,
        "casesForICUByRequestdTime": 2250342,
        "casesForVentilatorBrRequestedTime": 2250342,
        "dollarsFlight": 12484899635.2
        
    },
    "severeImpact": {
        "currentlyInfected": 137350,
        "infectedByRequestedTime": 5625856,
        "severeCasesByRequestedTime": 84387840,
        "hospitalBedsByRequesstedTime": -84150234,
        "casesForICUByRequestedTime": 28129280,
        "casesForVentilatorsByRequestedTime": 11251712,
        "dollarsInFlight": 62424498176
    }
} 
}


msg = "Hello World"
print (msg)
from setuptools import setup, find_packages


setup(name="covid19-estimator-py", packages=find_packages())
