# What is the Relationship between Code Review Direct Approval Rate and Release Deadline?

# Authors
* Shuonan Pei
* Zhimao Lin

# Dataset Detail
The [CROP](https://crop-repo.github.io) website provides code review record of 11 repositories in a period of time.
To see the detail of our data. Please go to [https://crop-repo.github.io/](https://crop-repo.github.io/) and click `Dataset Details` on the left-hand side bar.



# We picked the following 10 repositories for our research:
1. [eclipse.platform.ui](https://github.com/eclipse/eclipse.platform.ui)
2. [linuxtools](https://github.com/eclipse/linuxtools)
3. [jgit](https://github.com/eclipse/jgit)
4. [egit](https://github.com/eclipse/egit)
5. [couchbase-jvm-core](https://github.com/couchbase/couchbase-jvm-core)
6. [ns_server](https://github.com/couchbase/ns_server)
7. [testrunner](https://github.com/couchbase/testrunner)
8. [ep-engine](https://github.com/couchbase/ep-engine)
9. [couchbase-java-client](https://github.com/couchbase/couchbase-java-client)
10. [spymemcached](https://github.com/couchbase/spymemcached)



# How do we choose these ten repositories? 
* We did not pick repository [indexing](https://github.com/couchbase/indexing) because it does not have any release. 
* The main reason that we picked the other 10 repositories is that [CROP](https://crop-repo.github.io) provides very detailed code review information of those repositories. 
* These 10 projects are not toy projects. They are written by well known communities, Eclipse and Couchbase. They are also being used in the industry. 



# Instruction of reproducing our results
## Target machine and environment
* Macbook Pro
* MacOS Mojave Version 10.14.3

## Depedencies
1. Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28)
2. Pandas v0.23.0 Final (May 15, 2018)
3. Matplotlib version 3.0.3
4. PyGithub Version 1.43.5 (January 29, 2019)
5. Git version 2.17.2 (Apple Git-113)
6. R version 3.5.2 (2018-12-20)

## Reproduce steps
### Step0: Preparation 
1. Update your MacOS to MacOS Mojave Version 10.14.3 (The latest version on March 20th, 2019) or higher<br> 
   For more details, you can check [here](https://support.apple.com/en-ca/macos/mojave) or contact [Apple support](https://getsupport.apple.com/?caller=psp&PRKEYS=PF6)

2. Install Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) <br>
   You can download Python 3.7.1 [here](https://www.python.org/ftp/python/3.7.1/python-3.7.1-macosx10.6.pkg). For more details, you can follow the [Python beginners' guide](https://wiki.python.org/moin/BeginnersGuide/Download). After successfully downloading the installer, just open the .pkg file and follow the steps of the installer.

3. Install Pandas v0.23.0 Final (May 15, 2018) <br>
   Open Terminal on your Mac and run 
   ```pip3 install pandas```
   For more details, you can check [Pandas documentation](https://pandas.pydata.org/)

4. Install Matplotlib version 3.0.3 <br>
    Open Terminal on your Mac and run 
   ```pip3 install matplotlib```
   For more details, you can check [Matplotlib documentation](https://matplotlib.org/users/installing.html)

5. Install PyGithub Version 1.43.5 (January 29, 2019) <br>
    Open Terminal on your Mac and run 
    ```pip3 install PyGithub```
    For more details, you can check [PyGithub documentation](https://pygithub.readthedocs.io/en/latest/introduction.html#download-and-install)

6. Install Git version 2.17.2 (Apple Git-113) <br>
    Open Terminal on your Mac and run 
    ```git --version```
    to check if you have git on your Mac. 
    If you do not have git on your Mac, you can install it [here](https://git-scm.com/download/mac). For more details, you can check [Git documentation](https://git-scm.com/)

7. Install R version 3.5.2 <br>
    You can download R version 3.5.2 from [here](https://cran.cnr.berkeley.edu/bin/macosx/el-capitan/base/R-3.5.2.pkg) for Mac. If you are using other operating system, you can check the [R download page](https://cran.cnr.berkeley.edu/index.html). For more details, please check [R Manual](https://cran.cnr.berkeley.edu/index.html)



## Quick Start
You can run `run.sh` described in this `Quick Start`. This will automatically run from step 1 to 4. However, it will not reproduce step 2, instead, it will use the existing result in the `step2` folder to run step 3. 

### Open Terminal on your Mac and direct to step1 folder in our repository `direct-approval-rate-and-release-deadline` using command `cd` <br>
  If you do not know how to use command `cd`, you can Google it or check this [tutorial](https://macpaw.com/how-to/use-terminal-on-mac).

### Run chmod command to give the permision to run the shell script run.sh
  > ```chmod +x run.sh```

### Run 
  > ```./run.sh```

If you prefer to run each step manually and **reproduce the result in step 2**, please follow the instructions below.



## Step 1: 
This step will generate `step1_results` folder that contains a csv file for each repository. <br>
Each csv file contains the following information:
* review_number
  * The id of the code review 
* revision_number
  * How many times that the code has been revised before the code review is approved 
* status
  * The status can be the followings:
    * DirectlyApprove: Directly approved without any revision
    * ApproveAfterChange: Approved after some revision
    * Rejected: The code review is rejected
* author
  * The author who send the code review request
* url
  * The URL link of the code review record
* close_date
  * The date that the code review is closed
* close_time
  * The time that the code review is closed

For each repository, it shows the number of files that we skip due to there is no close date in the discussion txt files. Also, `step1.py` clears all the rows contains invalid data such as `NA` before it outputs the result into csv files. 

### Download the dataset from [CROP](https://crop-repo.github.io) website and extract to `direct-approval-rate-and-release-deadline/step1` folder
Please go to [https://crop-repo.github.io/](https://crop-repo.github.io/) and click `Download` on the left-hand side bar. You can download a file called `corp.zip` on that page. <br>
If you cannot find the dataset from above website, please check our backup repository [direct-approval-rate-and-release-deadline-dataset](https://github.com/ZhimaoLin/direct-approval-rate-and-release-deadline-dataset), which contains a copy of the dataset that we use.


### Open Terminal on your Mac and direct to step1 folder in our repository `direct-approval-rate-and-release-deadline/step1` using command `cd` <br>
  If you do not know how to use command `cd`, you can Google it or check this [tutorial](https://macpaw.com/how-to/use-terminal-on-mac).

### Run 
  > ```python3 step1.py```



## Step 2: 
This step will generate `step2_results` folder, which contains a csv file for each repository. Each csv file stores the release date and time of each repository. 

<br>

Please note that for GitHub API requests using Basic Authentication or OAuth, you can make up to **5000** requests per hour. Since the [eclipse.platform.ui](https://github.com/eclipse/eclipse.platform.ui) has over 6000 releases, we have to collect all release date and time in 3 steps with 1 hour cooling-down time between each step.

### Add your GitHub access token
First generate your access token. If you have any problems with it, please check this help page: [https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line). Then copy and paste you token in to **line 6** of `step2_1.py`, `step2_2.py`, and `step2_3.py`. 
You can also use our access token. Just simply comment **line 6** and uncomment **line 7**. However, we highly recommend using your own GitHub access token because we cannot guarantee it will still work after May 1st, 2019. 

### Open Terminal on your Mac and direct to step2 folder in our repository `direct-approval-rate-and-release-deadline/step2` using command `cd` <br>
  If you do not know how to use command `cd`, you can Google it or check this [tutorial](https://macpaw.com/how-to/use-terminal-on-mac).

### Run 
  > ```python3 step2_1.py```

### Wait for 1 hour after finishing previous step due to GitHub API limitations. 

### Run 
  > ```python3 step2_2.py```

### Wait for 1 hour after finishing previous step due to GitHub API limitations. 

### Run 
  > ```python3 step2_3.py```



## Step 3: 
This step will generate the `step3_results` folder, which contains a csv file for each repository and a file called `all_repo_rate.csv`. <br>
The csv file of each repository stores the following information: 
* close_date
  * We group the result of step1 by close_date for each repository.
* ApproveAfterChange
  * The number of code reviews that are approved with revision on that date
* DirectlyApprove
  * The number of code reviews that are approved without any revision on that date
* Rejected
  * The number of code review that are rejected on that day
* TotalReview
  * The total number of code reviews that are closed on that day
* DirectlyApproveRate
  * The percentage of the code reviews that are approved without any revision on that day.
  * DirectlyApproveRate = DirectlyApprove / TotalReview
* ApproveAfterChangeRate
  * The percentage of the code reviews that are approved with some revision on that day.
  * ApproveAfterChangeRate = ApproveAfterChange / TotalReview
* CloseToReleaseDate
  * A boolean variable shows if the code review is closed to the release date.


`all_repo_rate.csv` constains the mean of code review direct approval rate when it is closed to release date and when it is not closed to release date for each reository. This result is used to conduct paired Wilcoxon signed-rank test. <br>

If you choose to output the statistic result into a file, you will get a file called `statistic_result.txt` in the `step3_results` folder. It contains the `Wilcoxon signed-rank test` and `Logistics Regression` result of each repository. In addition, there is the `Paired Wilcoxon signed-rank test` result of all repositories. 

### Set date interval 
Change the value of variable `date_interval` on **line 9** of `step3.py`. The value means the number of days before release date, which are considered it is closed to release date. For example, if you want to consider the code review is closed to release date if it is closed on the day before release date or on the release day, then set this value to `2`. 
By default this value is `2`. <br>
**Once you changed this value, you need to re-run step 3 and 4 in order to get the corresponding results**

### Run 
  > ```python3 step3.py```

### Run Statistic Tests
If you want to output the statistic test result to a file, run 
  > ```rscript step3_2.R > ./step3_results/statistic_result.txt```

If you want to print the statistic test result on the Terminal, run 
  > ```rscript step3_2.R```



## Step 4: 
This step will generate a boxplot and several line charts for each repository.

### Run 
  ```python3 step4.py```


# Results
### [Here is our results](https://github.com/cmput402-w19/assignment5-sca-sz/blob/master/Results.md)


# References