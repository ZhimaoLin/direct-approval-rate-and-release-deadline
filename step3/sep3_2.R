wd <- paste(getwd(),  '/step3_results', sep = "", collapse = NULL)
setwd(wd)
getwd()

for (fileName in c('couchbase-java-client_final.csv', 'couchbase-jvm-core_final.csv', 'eclipse.platform.ui_final.csv', 'egit_final.csv', 'ep-engine_final.csv', 'jgit_final.csv', 'linuxtools_final.csv', 'ns_server_final.csv', 'org.eclipse.linuxtools_final.csv', 'spymemcached_final.csv', 'testrunner_final.csv')){
  print(fileName)
  d <- read.csv(fileName)
  result <- t.test(d$DirectlyApproveRate~d$CloseToReleaseDate)
  print(result)
}
