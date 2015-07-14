setwd("~/Desktop/Machine Learning")
library("arules")
library("arulesViz")

# FP-Growth Algorithm
data("Groceries")
summary(Groceries)
rules <- eclat(Groceries, parameter=list(support=0.01, target="frequent itemsets"))
rules

inspect(head(sort(rules, by ="support"), 5))

