import Orange

items= Orange.data.Table("item.basket")
rules= Orange.associate.AssociationRulesSparseInducer(items, support = 0.001, maxItemSets=1000000)

print(rules)
print "%4s %4s %s" % ("supp","conf","rule")
for r in rules:
    print "%5.3f %5.3f %s" % (r.support, r.confidence, r)