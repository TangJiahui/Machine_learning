
#transfer the dataset to another format
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

## write output into a format .basket that is suitable for Orange Package"
with open("item.basket",'w',newline='') as f:
    writer = csv.writer(f,delimiter=',')
    for row in transactions:
        writer.writerow(row)

## method 1: pymining package ####

#from pymining import itemming, assocrues, perftesting
#relim_input = itemmining.get_relim_input(transactions)
#print(relim_input)
#item_sets = itemmining.relim(relim_input, min_support=2)
#print(item_sets)
#rules = assocrules.mine_assoc_rules(item_sets, min_support=2, min_confidence=0.05)
#print(rules)


## method 2: orange package #####

import Orange

items= Orange.data.Table("item.basket")
rules= Orange.associate.AssociationRulesSparseInducer(items, support = 0.001, maxItemSets=1000000)

print(rules)
print "%4s %4s %s" % ("supp","conf","rule")
for r in rules:
    print "%5.3f %5.3f %s" % (r.support, r.confidence, r)