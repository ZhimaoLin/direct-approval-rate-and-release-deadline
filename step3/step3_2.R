# Run Rscript step3_2.R
# https://stats.idre.ucla.edu/r/dae/logit-regression/
# https://www.statmethods.net/advstats/glm.html
# http://www-bcf.usc.edu/~gareth/ISL/ISLR%20First%20Printing.pdf

wd <- paste(getwd(),  '/step3_results', sep = "", collapse = NULL)
setwd(wd)
getwd()

fileNameList <- c('couchbase-java-client_final.csv', 'couchbase-jvm-core_final.csv', 'eclipse.platform.ui_final.csv', 'egit_final.csv', 'ep-engine_final.csv', 'jgit_final.csv', 'linuxtools_final.csv', 'ns_server_final.csv', 'linuxtools_final.csv', 'spymemcached_final.csv', 'testrunner_final.csv')
# fileNameList <- c('couchbase-jvm-core_final.csv')

pValueThreshold <- 0.01
onlyShowSignificant <- TRUE   # Enter TRUE or FALSE

for (fileName in fileNameList){
  d <- read.csv(fileName)
  d$CloseToReleaseDate <- factor(d$CloseToReleaseDate)

  print('=============================================')
  print(fileName)
  print('=============================================')
  print('|     T test                                |')
  print('=============================================')

  # h0: two means are similar 
  # hAlpha: two means are different
  # if p <= Alpha --> Against h0
  # alpha = 0.01 99% confidence 
  result <- t.test(d$DirectlyApproveRate~d$CloseToReleaseDate)
  pValue <- result$p.value

  if (onlyShowSignificant == FALSE) {
    print(result)
  } else {
    if (pValue <= pValueThreshold) {
      print(result)
    }
  }

  print('=============================================')
  print('|     Logistics Regression                  |')
  print('=============================================')

  # If p-value <= pValueThreshold, 
  # then there is association between DirectlyApproveRate and CloseToReleaseDate.
  mylogit <- glm(d$CloseToReleaseDate ~ d$DirectlyApproveRate, data = d, family="binomial")
  result <- summary(mylogit)

  pValue <- result$coefficients[2,4]

  if (onlyShowSignificant == FALSE) {
    print(result)
  } else {
    if (pValue <= pValueThreshold) {
      print(result)
    }
  }

  print('=============================================')
  cat('\n')
  cat('\n')
  cat('\n')
}
