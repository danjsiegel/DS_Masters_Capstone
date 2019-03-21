library(httr)
library(ggplot2)
library(dplyr) 
library(readr)
library(class)
library(caret)
library(gmodels)
library(cluster)
library(fpc)
library(foreign)
library(date)
library(ROCR)

surg <- read.arff('https://archive.ics.uci.edu/ml/machine-learning-databases/00277/ThoraricSurgery.arff')
surg$Risk1Yr <- as.numeric(surg$Risk1Yr)-1
surg$DGN <- as.factor(surg$DGN)
surg$PRE6 <- as.factor(surg$PRE6)
surg$PRE7 <- as.numeric(surg$PRE7)-1
surg$PRE8 <- as.numeric(surg$PRE8)-1
surg$PRE9 <- as.numeric(surg$PRE9)-1
surg$PRE10 <- as.numeric(surg$PRE10)-1
surg$PRE11 <- as.numeric(surg$PRE11)-1
surg$PRE14 <- as.factor(surg$PRE14)
surg$PRE17 <- as.numeric(surg$PRE17)-1
surg$PRE19 <- as.numeric(surg$PRE19)-1
surg$PRE25 <- as.numeric(surg$PRE25)-1
surg$PRE30 <- as.numeric(surg$PRE30)-1
surg$PRE32 <- as.numeric(surg$PRE32)-1

#a. Fit a binary logistic regression model to the data set that predicts whether or not the patient survived for one year (the Risk1Y variable) after the surgery. Use the glm() function to perform the logistic regression. See Generalized Linear Models for an example. Include a summary using the summary() function in your results.

survived <- glm(Risk1Yr ~ DGN + PRE4 + PRE5 + PRE6 + PRE7 + PRE8 +    
                PRE9 + PRE10 + PRE11 + PRE14 + PRE17  + PRE19 + 
                  PRE25 + PRE30 + PRE32 + AGE, data=surg)
summary(survived)


#b. According to the summary, which variables had the greatest effect on the survival rate?
#DGN8, pre9, pre14/Oc14 

# c. To compute the accuracy of your model, use the dataset to predict the outcome variable. The percent of correct predictions is the accuracy of your model. What is the accuracy of your model?

set.seed(123)
n<- nrow(surg)
shuffled <- surg[sample(n),]
train <- shuffled[1:round(0.7 * n),]
test <- shuffled[(round(0.7 * n) + 1):n,]
testing_survived <- glm(Risk1Yr ~ DGN + PRE4 + PRE5 + PRE6 + PRE7 + PRE8 +    
                          PRE9 + PRE10 + PRE11 + PRE14 + PRE17  + PRE19 + 
                          PRE25 + PRE30 + PRE32 + AGE, data=train)
predicted_data <- predict(testing_survived, newdata = test)
x<- as.integer(predicted_data)
y <- test$Risk1Yr
l <- union(x, y)
Table2 <- table(factor(x, l), factor(y, l))
confusionMatrix(Table2)

# 8.2 
#a. Calculate precision, recall, and F1 score for your model using the test dataset.
set.seed(123)
n<- nrow(surg)
shuffled <- surg[sample(n),]
train <- shuffled[1:round(0.7 * n),]
test <- shuffled[(round(0.7 * n) + 1):n,]
testing_survived <- glm(Risk1Yr ~ DGN + PRE4 + PRE5 + PRE6 + PRE7 + PRE8 +    
                          PRE9 + PRE10 + PRE11 + PRE14 + PRE17  + PRE19 + 
                          PRE25 + PRE30 + PRE32 + AGE, data=train)
predicted_data <- predict(testing_survived, newdata = test)

pred <- prediction(predicted_data, test$Risk1Yr)
RP.perf <- performance(pred, "prec", "rec")
f1_score <- performance(pred,"f")
ROC.perf <- performance(pred, "tpr", "fpr")
#b. Plot the receiver operating characteristic (ROC) curve using the test dataset. Additionally, calculate the area under the curve (AUC) value.
plot (ROC.perf)
auc.tmp <- performance(pred,"auc");
auc <- as.numeric(auc.tmp@y.values)
auc

#c. Consider the case where you fit a logistic regression model. When you calculate the classifier metrics, you get an accuracy of 96%, but an AUC of 53%. Is this a good predictive model? Explain why or not.
# The AUC is the measure of performance of a binary classifier. The performance is averaged across all possible decision thresholds.
# From Wikipedia on the topic:
#   One recent explanation of the problem with ROC AUC is that reducing the ROC Curve to a single number ignores the fact that it is about the tradeoffs between the different systems or performance points plotted and not the performance of an individual system, as well as ignoring the possibility of concavity repair, so that related alternative measures such as Informedness[6] or DeltaP are recommended.[22]

############ 8.3

binary_data <- read_csv("http://content.bellevue.edu/cst/dsc/520/id/resources/binary-classifier-data.csv")

ind <- createDataPartition(binary_data$label, p=0.70, list=FALSE)
dat_train <- binary_data[ind,]       
dat_test <- binary_data[-ind,]        

binary_log <- glm(label~ x + y, data=dat_train)
binary_pred <- predict(binary_log, dat_test, type = "response")
#a. What is the accuracy of the logistic regression classifier?
confusionMatrix(table(data = as.numeric(binary_pred>0.5), reference = dat_test$label))
# b. How does the accuracy of the logistic regression classifier compare to the nearest neighbors algorithm?
binary_knn <- knn(dat_train[,-1], dat_test[,-1], factor(dat_train$label), k=5, prob=TRUE)
binary_knn_pred <- confusionMatrix(table(binary_knn, dat_test$label))
merge <- data.frame(knn.1, test.def)
names(merge)<- c("Predicted Condition", "Observed Condition")
confusionMatrix(table(as.numeric(merge$`Predicted Condition`>0.5), merge$`Observed Condition`))

# About 50% to 83%. 

#c. Why is the accuracy of the logistic regression classifier different from that of the nearest neighbors?
1) Logistic regression predicts probabilities, which are a measure of the confidence of prediction. k-nearest neighbors predicts just the labels.
2.) Logistic regression assumes is that there is one smooth linear decision boundary. The data is clearly in clusters, and a little bit of EDA would help us determine which algorithm would be the best fit for this data. 

