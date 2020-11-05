#!/usr/bin python3

import requests
import json

ec_data = {
    "Alabama": 9,
    "Alaska": 3,
    "Arizona": 11,
    "Arkansas": 6,
    "California": 55,
    "Colorado": 9,
    "Connecticut": 7,
    "Delaware": 3,
    "District of Columbia": 3,
    "Florida": 29,
    "Georgia": 16,
    "Hawaii": 4,
    "Idaho": 4,
    "Illinois": 20,
    "Indiana": 11,
    "Iowa": 6,
    "Kansas": 6,
    "Kentucky": 8,
    "Louisiana": 8,
    "Maine": 4,
    "Maryland": 10,
    "Massachusetts": 11,
    "Michigan": 16,
    "Minnesota": 10,
    "Mississippi": 6,
    "Missouri": 10,
    "Montana": 3,
    "Nebraska": 5,
    "Nevada": 6,
    "New Hampshire": 4,
    "New Jersey": 14,
    "New Mexico": 5,
    "New York": 29,
    "North Carolina": 15,
    "North Dakota": 3,
    "Ohio": 18,
    "Oklahoma": 7,
    "Oregon": 7,
    "Pennsylvania": 20,
    "Rhode Island": 4,
    "South Carolina": 9,
    "South Dakota": 3,
    "Tennessee": 11,
    "Texas": 38,
    "Utah": 6,
    "Vermont": 3,
    "Virginia": 13,
    "Washington": 12,
    "West Virginia": 5,
    "Wisconsin": 11,
    "Wyoming": 3,
    "Puerto Rico": 0
}

def create_dict(json):
    dict = {}
    stateIdx = -1
    popIdx = -1
    for i in range(len(json[0])):
        if (json[0][i] == "NAME"):
            stateIdx = i
        elif (json[0][i] == "POP"):
            popIdx = i
    
    json.pop(0)
    for item in json:
        dict[item[stateIdx]] = int(item[popIdx])
    
    return dict

def get_least_pop(data):
    pop = 99999999
    state = ""
    for key in data:
        if (data[key] < pop):
            pop = data[key]
            state = key
    return state, pop

res = requests.get("https://api.census.gov/data/2019/pep/charagegroups?get=STATE,POP,NAME&for=state:*&AGEGROUP=29")
obj = res.json()

data = create_dict(obj)
lowestState, lowestPop = get_least_pop(data)

delPerPop = float(ec_data[lowestState]) / float(lowestPop)

print("[State]: [adjusted]([actual])")
for state in data:
    print(str(state) + ": " + str(round(data[state] * delPerPop)) + " (" + str(ec_data[state]) + ")")
