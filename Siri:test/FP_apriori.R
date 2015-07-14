setwd("~/Desktop/Machine Learning")
# siri <- read.csv("Siri_data_with_class.csv", header=TRUE)
# impossible to use Siri dataset as frequent pattern needs transaction dataset

library("arules")
library("arulesViz") # this lib contains the arules


##
# use dataset in R library
data("Groceries")
summary(Groceries)


rules <- apriori(Groceries, parameter=list(support=0.001, confidence=0.5))
rules

# check the top ten rules with respect to the lift measure
inspect(head(sort(rules, by ="lift"), 10))

## visualization
plot(rules)
head(quality(rules))
plot(rules, measure=c("support","lift"), shading="confidence")

# two key plot, where the order = no of items contained in the rule
plot(rules, shading="order",control=list(main="Two-key plot"))
plot(rules, measure= c("support","lift"), shading ="confidence", interactive=T)

# sub rules
subrules <- rules[quality(rules)$confidence >0.8]
subrules
plot(subrules, method="matrix",measure="lift")
plot(subrules, method="matrix",measure="lift", control=list(reorder=TRUE))