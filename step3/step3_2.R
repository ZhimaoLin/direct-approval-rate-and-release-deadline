# Run Rscript step3_2.R
# https://stats.idre.ucla.edu/r/dae/logit-regression/
# https://www.statmethods.net/advstats/glm.html
# http://www-bcf.usc.edu/~gareth/ISL/ISLR%20First%20Printing.pdf

wd <- paste(getwd(),  '/step3_results', sep = "", collapse = NULL)
setwd(wd)
wd <- getwd()

fileNameList <- c('couchbase-java-client_final.csv', 'couchbase-jvm-core_final.csv', 'eclipse.platform.ui_final.csv', 'egit_final.csv', 'ep-engine_final.csv', 'jgit_final.csv', 'linuxtools_final.csv', 'ns_server_final.csv', 'linuxtools_final.csv', 'spymemcached_final.csv', 'testrunner_final.csv')
# fileNameList <- c('couchbase-jvm-core_final.csv')

pValueThreshold <- 0.01
onlyShowSignificant <- FALSE   # Enter TRUE or FALSE

for (fileName in fileNameList){
  d <- read.csv(fileName)
  d$CloseToReleaseDate <- factor(d$CloseToReleaseDate)

  print('=============================================')
  print(fileName)
  print('=============================================')
  print('|     Wilcoxon signed-rank test             |')
  print('=============================================')

  # If pValue <= pValueThreshold, the median of DirectAprovalRate between closedToReleaseDate and not closedToReleaseDate are significantly diffferent. 
  # If pValue > pValueThreshold, there is NOT significant evidence shows that the median of DirectAprovalRate between closedToReleaseDate and not closedToReleaseDate are significantly diffferent.
  
  result <- wilcox.test(d$DirectlyApproveRate~d$CloseToReleaseDate, data=d)
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

# Paired test
allRepoRate <- data.frame(
  repo_name = fileNameList,
  closed_to_release_date = numeric(length(fileNameList)),
  not_closed_to_release_date = numeric(length(fileNameList))
)

for (fileName in fileNameList) {
  d <- read.csv(fileName)
  d$CloseToReleaseDate <- factor(d$CloseToReleaseDate)

  closedToReleaseDateMean <- mean(d[ which(d$CloseToReleaseDate=='True'), ]$DirectlyApproveRate)

  notClosedToReleaseDateMean <- mean(d[ which(d$CloseToReleaseDate=='False'), ]$DirectlyApproveRate)

  allRepoRate[ which(allRepoRate$repo_name==fileName), ]$closed_to_release_date <- closedToReleaseDateMean

  allRepoRate[ which(allRepoRate$repo_name==fileName), ]$not_closed_to_release_date <- notClosedToReleaseDateMean
}

write.csv(allRepoRate, paste(wd,  '/all_repo_rate.csv', sep = "", collapse = NULL), row.names=FALSE)

print('=============================================')
print('        Paired Test Accross All Repos        ')
print('=============================================')
print('|     Wilcoxon signed-rank test             |')
print('=============================================')

# If pValue <= pValueThreshold, the median of DirectAprovalRate between closedToReleaseDate and not closedToReleaseDate are significantly diffferent. 
# If pValue > pValueThreshold, there is NOT significant evidence shows that the median of DirectAprovalRate between closedToReleaseDate and not closedToReleaseDate are significantly diffferent.

result <- wilcox.test(allRepoRate$closed_to_release_date, allRepoRate$not_closed_to_release_date, paired = TRUE)

pValue <- result$p.value

print(result)

print('=============================================')
cat('\n')
cat('\n')
cat('\n')

