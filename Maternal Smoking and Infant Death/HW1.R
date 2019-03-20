# HW 1
rt1<- read.table('E:/Zhijian Hu/19win/math 189/babies.txt',head=TRUE)
rt2<- read.table('E:/Zhijian Hu/19win/math 189/baby123.txt',head=TRUE)

rt1.weight

set.seed(1)
a <- rnorm(100)
b <- rnorm(100)

boxplot(a, at=1,xlim=c(0,4))
boxplot(b, at=2, add=TRUE)

