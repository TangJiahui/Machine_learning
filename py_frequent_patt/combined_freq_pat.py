## run the script
## >> python combined_freq_pat.py datafile.csv


#transfer the dataset to another format
import csv
import sys

def insertIntoDataStruct(name,location,mydict):
    if not name in mydict:
        mydict[name]=[location]
    else:
        mydict[name].extend([location])

mydict={}

filename_i = sys.argv[1]
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
        r_format=str(r).replace(' -> ', '->')
        r_format=str(r_format).replace(" ","&&")
        writer2.writerow(["%5.3f %5.3f %5.3f %s" % (r.support, r.confidence, r.lift, r_format)]) 



#### Part 3: find the significant outliers ######
lift = []
support =[]
confidence = []

for r in rules:
    lift += [r.lift]
    support += [r.support]
    confidence += [r.confidence]

import numpy

iqr_l = numpy.subtract(*numpy.percentile(numpy.array(lift),[75,25]))
iqr_s = numpy.subtract(*numpy.percentile(numpy.array(support),[75,25]))
iqr_c = numpy.subtract(*numpy.percentile(numpy.array(confidence),[75,25]))

thre_l = numpy.percentile(numpy.array(lift),75) + 1.5*iqr_l
thre_s = numpy.percentile(numpy.array(support),75) + 1.5*iqr_s
thre_c = numpy.percentile(numpy.array(confidence),75) + 1.5*iqr_c

rules_s=sorted(rules, key = lambda r: r.support, reverse=True )
rules_c=sorted(rules, key = lambda r: r.confidence, reverse=True )


filename_sign_l = filename_i[:-4]+'_significant_lift.csv'
filename_sign_s = filename_i[:-4]+'_significant_support.csv'
filename_sign_c = filename_i[:-4]+'_significant_confidence.csv'


with open(filename_sign_l,"w") as f:
    writer1 = csv.writer(f, delimiter = ' ')
    writer2 = csv.writer(f, delimiter=',')
    #writer1.writerow(["Significant outliers derived by lift"])
    writer1.writerow(["supp","conf","lift","rule"])
    for r in rules:
        if r.lift > thre_l:
            r_format=str(r).replace(' -> ', '->')
            r_format=str(r_format).replace(" ","&&")
            writer2.writerow(["%5.3f %5.3f %5.3f %s" % (r.support, r.confidence, r.lift, r_format)]) 

with open(filename_sign_s,"w") as f:
    writer1 = csv.writer(f, delimiter = ' ')
    writer2 = csv.writer(f, delimiter=',')
    #writer1.writerow(["Significant outliers derived by support"])
    writer1.writerow(["supp","conf","lift","rule"])
    for r in rules_s:
         if r.support > thre_s:
            r_format=str(r).replace(' -> ', '->')
            r_format=str(r_format).replace(" ","&&")
            writer2.writerow(["%5.3f %5.3f %5.3f %s" % (r.support, r.confidence, r.lift, r_format)]) 

with open(filename_sign_c,"w") as f:
    writer1 = csv.writer(f, delimiter = ' ')
    writer2 = csv.writer(f, delimiter=',')
    #writer1.writerow(["Significant outliers derived by confidence"])
    writer1.writerow(["supp","conf","lift","rule"])
    for r in rules_c:
        if r.confidence > thre_c:
            r_format=str(r).replace(' -> ', '->')
            r_format=str(r_format).replace(" ","&&")
            writer2.writerow(["%5.3f %5.3f %5.3f %s" % (r.support, r.confidence, r.lift, r_format)]) 










