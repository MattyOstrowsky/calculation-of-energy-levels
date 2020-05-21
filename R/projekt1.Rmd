library("COVID19")
x<-covid19(
  country = "Poland",
  level = 1,
  start = "2020-03-01",
  end = "2020-05-01",
  raw = FALSE,
  vintage = FALSE,
  verbose = TRUE,
  cache = TRUE,
  wb = NULL,
  gmr = NULL,
  amr = NULL
)
pdf("wykres.pdf")
plot(x = x$date, y = x$confirmed,
     pch = 16, frame = FALSE,
     xlab = "data", ylab = "", col = "blue")
points(x= x$date,y=x$deaths,col="red")
points(x= x$date,y=x$recovered,col="green")
dev.off() 

