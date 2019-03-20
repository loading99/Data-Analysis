setwd("C:/Users/nuc005/Desktop/189")
BabyData <- read.table("babies.txt",header = TRUE)
BabyData2 <- read.table("babies2.txt",header = TRUE)

#summary,mean,variance,standard deviation
summary(BabyData2$wt)
var(BabyData2$wt)
sd(BabyData2$wt)

#subset smoke/nonsmoke mother
BabyData2.smoke <- subset(BabyData2,BabyData2$smoke == 1)
BabyData2.nonsmoke <- subset(BabyData2,
                            (BabyData2$smoke == 0 |
                             BabyData2$smoke == 2 |
                             BabyData2$smoke == 3 ))

#histogram of baby weight
hist(BabyData2$wt,breaks = 100,probability = TRUE, 
     xlab = "baby weights born", 
     main = "Histogram of baby weights")

lines(density(BabyData2$wt, bw = 0.25),col = "red")
lines(density(BabyData2$wt, bw = 0.5),col = "green")

hist(BabyData2.smoke$wt)
hist(BabyData2.nonsmoke$wt)

#histogram of baby weight
boxplot(wt~smoke,BabyData2,
        xlab = "smoke level")
