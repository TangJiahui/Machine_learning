#cmd in terminal: Rscript Significance\ analysis.R "filename.csv"

args <- commandArgs(TRUE)
filename <- args[1]
rules<- read.csv(filename)

# sort rules
rules <-rules[order(rules[,4],rules[,3], decreasing=T),]

# distribution of parameters
plot(rules)
hist(rules$lift, main="frequency distribution of lift")
hist(rules$support, main="frequency distribution of support")
hist(rules$confidence, main="frequency distribution of confidence")

#outliers in terms of lift-->how much more likely the consequent is, given the antecedent
boxplot(rules$lift, outline=T)
outliers = boxplot(rules$lift)$out
l = rules[rules$lift %in% outliers,]

#confidence-->how often rhs appears in transaction contains lhs
outliers2 = boxplot(rules$confidence)$out
c = rules[rules$confidence %in% outliers2,]

#support-->frequently appeared in all transactions
outliers3 = boxplot(rules$support)$out
s = rules[rules$support %in% outliers3,]


writeLines('outliers generated from 1.lift 2.confidence 3.support', con=paste(substr(args[1],1, nchar(args[1])-4),'_significant.csv',sep=''), sep='\n')
write.table(l, file=paste(substr(args[1],1, nchar(args[1])-4),'_significant.csv',sep=''), sep=',',append=TRUE)
write.table(c, file=paste(substr(args[1],1, nchar(args[1])-4),'_significant.csv',sep=''), sep=',',append=TRUE)
write.table(s, file=paste(substr(args[1],1, nchar(args[1])-4),'_significant.csv',sep=''), sep=',',append=TRUE)


######used for testing###########

#rules <-read.csv("FPM_PFW3_Others_output_rules.csv")
#rules <-read.csv("FPM_PFW3_All_output_rules.csv")
#writeLines('outliners generated from 1.lift 2.confidence 3.support', con='significant.csv', sep='\n')
#write.table(l, file='significant.csv', sep=',',append=TRUE)
#write.table(c, file='significant.csv', sep=',',append=TRUE)
#write.table(s, file='significant.csv', sep=',',append=TRUE)


