
#transfer the dataset to another format
import csv

def insertIntoDataStruct(name,location,mydict):
    if not name in mydict:
        mydict[name]=[location]
    else:
        mydict[name].extend([location])

mydict={}

filename_i = raw_input('Please type in the filename here:')
filename_o = filename_i[:-4]+'.basket'
filename_r = filename_i[:-4]+'_result.csv'

with open(filename_i) as f:
    reader = csv.reader(f)    
    for rows in reader:
        #rows = rows.split(',')
        insertIntoDataStruct(rows[0],rows[1],mydict)

transactions = list(mydict.values())

## write output into a format .basket that is suitable for Orange Package"
with open(filename_o,'w') as f:
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
import csv

items= Orange.data.Table(filename_o)
rules= Orange.associate.AssociationRulesSparseInducer(items, support = 0.001, maxItemSets=1000000)
rules=sorted(rules, key = lambda r: r.lift, reverse=True )

with open(filename_r,"w") as f:
    writer1 = csv.writer(f,delimiter=' ')
    writer1.writerow(["supp","conf","lift","rule"])
    writer2 = csv.writer(f, delimiter=",")
    for r in rules:
        writer2.writerow(["%5.3f %5.3f %5.3f %s" % (r.support, r.confidence, r.lift, r)]) 

