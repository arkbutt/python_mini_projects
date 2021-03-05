from fuzzywuzzy import fuzz
from fuzzywuzzy import process

import json

def load_json(path):
    with open (path) as f:
        data= json.load(f)
        return data

#query = user input
#patient = bunch of data in database
#threshold = maximum ratio

def filter_ratio(query,patient, threshold):
#                                         Klaus, 
    max_fuzz_score= fuzz.token_sort_ratio(query, patient['name'])

    return max_fuzz_score >= threshold 
        

def search(query,threshold):
    data=load_json("./Fuzzy.json")
    results = []
    for patient in data['info']:
        if filter_ratio(query,patient,threshold):
            results.append(patient["name"])
    return results



print(search("Hans-Dieter",40))
