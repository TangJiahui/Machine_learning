#command line to run the file in Terminal/unix:
# Rscript freqpat_and_rules.R "arg1" arg2 arg3
# where arg1 is a string represents the filename 
# arg2 and arg3 are two integers refer to support and confidence


library("arules")
library("arulesViz")
args <-commandArgs(TRUE)
filename <- args[1]
sup <- as.numeric(args[2])
con <- as.numeric(args[3])
raw <- read.csv(filename, header=F, col.names=c('user','loca'))

#interactive shell in Rstudio
#raw <- read.csv("FPM_PFW3_Others.csv", header=F, col.names=c('user','loca'))

# take sample
#raw <- head(raw,10002)

# construct an empty binary incidence matrix
unique_user <- unique(raw[,1])
unique_loca <- unique(raw[,2])
binaryMat<- matrix(data=0, nrow=length(unique_user),ncol=length(unique_loca), dimnames=list(unique_user, unique_loca))

#calculate the occurance of each transaction and put it in binary matrix
for(i in 1:nrow(raw)){
  binaryMat[toString(raw[i,1]),toString(raw[i,2])] = 1+ binaryMat[toString(raw[i,1]),toString(raw[i,2])]
}

#transfer it to an itemMatrix/transaction data needed by Arules
transaction <-as(binaryMat, 'itemMatrix')

#find frequent itemsets and rules/frequent pattern
rules1 <- apriori(transaction, parameter=list(support=sup, confidence=con,target="rules"))
itemset <- apriori(transaction, parameter=list(support=sup, confidence=con,target="frequent itemsets"))
rules<-as(rules1, "data.frame")
itemset<-as(itemset, "data.frame")
write.table(rules,file=paste(substr(args[1],1,nchar(args[1])-4),'_output_rules.csv',sep=''), sep=',')
write.table(itemset,file=paste(substr(args[1],1,nchar(args[1])-4),'_output_itemset.csv',sep=''), sep=',')


#######################used for testing###########################
#rules1 <- apriori(transaction, parameter=list(support=0.001, confidence=0.05,target="rules"))
#write.table(rules,file=paste('test','_output_rules.csv'), sep=',')

#sink(file=paste(substr(args[1],1,nchar(args[1])-4),'_output_rules','.csv'), type=)
#sink(file=paste(substr(args[1],1,nchar(args[1])-4),'_output_itemsets','.csv'), type=itemset)

# or verify it with Eclat
# frequent_items<- eclat(transaction, parameter=list(support=0.01))
# inspect(head(sort(frequent_items, by ="support"), 10))
