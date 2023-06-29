travel_log=[
    {"Country" : "France", 
     "visits":12,
     "cities":["Paris","Lille","Dijon"]},
    {"Country":"Germany", 
     "visits":5,
     "cities":["Berlin","Hamburg","Stuttgart"]}
]

def add_new_country(Country,visits,cities):
    new_country={}
    new_country["Country"]=Country
    new_country["visits"]=visits
    new_country["Cities"]=cities
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersberg"])
print(travel_log)