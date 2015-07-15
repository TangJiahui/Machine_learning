
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