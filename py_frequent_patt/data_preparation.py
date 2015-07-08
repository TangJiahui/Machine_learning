#from pymining import itemmining, assocrules, perftesting

import csv

def insertIntoDataStruct(name,location,mydict):
    if not name in mydict:
        mydict[name]=[location]
    else:
        mydict[name].extend([location])

mydict={}
with open("FPM_PFW3_Others.csv") as f:
#with open("test.csv") as f:
    reader = csv.reader(f)    
    for rows in reader:
        #rows = rows.split(',')
        insertIntoDataStruct(rows[0],rows[1],mydict)

transactions = list(mydict.values())

with open("transfered.csv",'w',newline='') as f:
    writer = csv.writer(f,delimiter=',')
    for row in transactions:
        writer.writerow(row)
    
#relim_input = itemmining.get_relim_input(transactions)
#print(relim_input)
#item_sets = itemmining.relim(relim_input, min_support=2)
#print(item_sets)
#rules = assocrules.mine_assoc_rules(item_sets, min_support=2, min_confidence=0.05)
#print(rules)
