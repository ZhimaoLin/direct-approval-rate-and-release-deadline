# Run Rscript step3_2.R

wd <- paste(getwd(),  '/step3_results', sep = "", collapse = NULL)
setwd(wd)
getwd()

fileNameList <- c('couchbase-java-client_final.csv', 'couchbase-jvm-core_final.csv', 'eclipse.platform.ui_final.csv', 'egit_final.csv', 'ep-engine_final.csv', 'jgit_final.csv', 'linuxtools_final.csv', 'ns_server_final.csv', 'org.eclipse.linuxtools_final.csv', 'spymemcached_final.csv', 'testrunner_final.csv')

for (fileName in fileNameList){
  print(fileName)
  d <- read.csv(fileName)
  result <- t.test(d$DirectlyApproveRate~d$CloseToReleaseDate)
  # print(result)

  # h0: two means are similar 
  # hAlpha: two means are different
  # if p <= Alpha --> Against h0
  # alpha = 0.01 99% confidence 

  if (result$p.value <= 0.01) {
    print(result)
    print(result$p.value <= 0.01)
  }
}
