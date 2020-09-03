---
title: "Checking_Spam"
author: "Prakhar"
date: "2 September 2020"
output: html_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

### Loading of preprocessed data from *kernlab* library..
```{r}
	library(kernlab)
	data(spam)
```
### Performing the Subsampling..
```{r}
	set.seed(3435)
	trainIn <- rbinom(4061, size=1, prob=0.5)	
	table(trainIn)
```
### Randomly and unevenly distrbuting the data in train and test datasets..
```{r}
	trainspam <- spam[trainIn==1,]
	testspam <- spam[trainIn==0,]
```
### Summaries of the data.. 
```{r}
	names(trainspam)
	head(trainspam)
	table(trainspam$type)
```
### Performing EDA for better Analysis of predictors..
```{r}
	plot(trainspam$capitalAve ~ trainspam$type)
```
```{r}
  plot(log10(trainspam$capitalAve + 1) ~ trainspam$type, pch=19,
		col=trainspam$type,xlab="type",ylab="CapitalAve")
```
```{r}
  plot(log10(trainspam[,1:4]))
```

### Using Clustering Algorithm..
```{r}
	hcluster <- hclust(dist(t(trainspam[, 1:57])))
	plot(hcluster,xlab="trainspam[,1:57]",ylab="Height",
		main="Clustering Dendogram")
```
```{r}
	hcupdate <- hclust(dist(t(log10(trainspam[ , 1:55] + 1))))
	plot(hcupdate,xlab="log10(trainspam[,1:55]+1)",ylab="Height",
		main="Clustering Dendogram")
```

### Preparing the model.. 
```{r , results='hide',warning=FALSE}	
	trainspam$numType <- as.numeric(trainspam$type) - 1
	cvError <- rep(NA,55)
	costfunction <- function(x, y) sum(x != (y > 0.5))
	library(boot)
	for (i in 1:55) {
		lmformula = reformulate(names(trainspam)[i],response="numType")
		glmFit = glm(lmformula, family = "binomial" , data = trainspam)
		cvError[i] = cv.glm(trainspam, glmFit, costfunction, 2)$delta[2]
	}
```
### Which predictor has minimum cross validation error??
```{r}	
	pred <- names(trainspam)[which.min(cvError)]
	print(pred)
```
### Use the best model form the group.. 
```{r , results='hide',warning=FALSE}	
	predictModel <- glm(numType ~ charDollar, family="binomial", data=trainspam)
```
### Get prediction the test set..
```{r}
	predictionTest <- predict(predictModel, testspam)
	predictspam <- rep("nonspam",nrow(testspam))
```
### Classify as "spam" for those with prob > 0.5
```{r}
	predictspam[predictModel$fitted > 0.5] = "spam"
	predictTable <- table(predictspam , testspam$type)
```
### Calculating the error in the Predicting Model..
```{r}
	error = (predictTable[1,2]+predictTable[2,1])/sum(predictTable)
	sprintf("Error percentage in the Model is %f ",error*100)
```