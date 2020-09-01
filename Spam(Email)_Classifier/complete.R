complete <- function(directory, id=1:332) {
        files <- paste(directory, "/", formatC(id, width=3, flag="0"), ".csv", sep="")
        subsetf <- files[1:length(files)]
        df <- data.frame(id)
        y<-numeric()
        for(i in 1:length(subsetf)) {
                filename <- subsetf[i]
                temp <- read.csv(filename,header=TRUE)
		    
		    y[i]<-sum(complete.cases(temp))	
                
        }
	  df <- cbind(df,nobs=y)
	  df
}


		    