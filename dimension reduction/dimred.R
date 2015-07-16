library(car)
#raw <- read.csv("CellSite.csv", header=F, col.names=c("value","attr","id","label"))
raw <- read.csv("SM120.csv", header=F)
data <- raw[,2:169]

# reshape the data, unlabeled
data1<-reshape(raw[,1:3], idvar="id", timevar="attr", direction="wide")

# get the label
id<-unique(raw$id)
label<-matrix('', nrow=length(id), ncol=1)
for (i in 1:length(raw$id)){
  label[raw[i,3]]=raw[i,4]
}

label <-recode(label,"'1'='A';'2'='B';'3'='C';'4'='D'")

# the data with labels
data <- cbind(data1,label)

##### apply PCA to the data (without label) #####
data[is.na(data)] <- 0
# pca <- prcomp(data[,2:25], scale.=TRUE)
pca <- prcomp(data, scale.=TRUE)
pca$sdev #sqrt of eigenvalues
pca$rotation #loadings, eigenvectors
pca$x #scores

summary(pca) #first 9PC explains 99% of the data
plot(pca)

##generating new PCA data##
newdat<-pca$x[,1:130]
newdat<-as.data.frame(newdat)
newdat <- cbind(newdat,label)
write.table(newdat, file="SM120_PCA130.csv",sep=",")

##### apply LDA to the data (label)#####
lda <- lda(data[,2:25], grouping=data[,26], scale.=TRUE)
lda$svd #between and within-group standard deviation
lda # three LDAs explains 99% of the classes

##generating new LDA data##
lda_mat <-as.matrix(lda$scaling)
data_lda <- as.matrix(data[,2:25])
new_lda_data <- data_lda %*% lda_mat
new_lda_data <- cbind(new_lda_data, label)
write.table(new_lda_data, file="LDA3.csv", sep =',')
