library(wbstats)
library(ggplot2)
w<-wb(country = "PL", indicator = "SP.POP.TOTL", startdate = 1968, enddate = 2018)
data <- data.frame(w$date,w$value/1000000)
ggplot(data, aes(w$date,w$value/1000000)) + geom_point() + labs(x="date",y="population[mln]",title="population in Poland 1968-2018")
ggsave("plot.pdf", width = 20, height = 5)

g<-wb(country = "1W",indicator = "SP.POP.TOTL", startdate = 1968, enddate = 2018)
data1 <- data.frame(g$date,g$value/1000000000)
ggplot(data1, aes(g$date,g$value/1000000000)) + geom_point() + labs(x="date",y="population[mld]",title="World population 1968-2018")
ggsave("plot1.pdf", width = 20, height = 5)

