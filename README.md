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



## Step 1: 
This step will generate `step1_results` folder that contains a csv file for each repository. Each csv file contains the following information:
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

### Download the dataset from [CROP](https://crop-repo.github.io) website and extract to `direct-approval-rate-and-release-deadline/step1` folder
Please go to [https://crop-repo.github.io/](https://crop-repo.github.io/) and click `Download` on the left-hand side bar. You can download a file called `corp.zip` on that page. <br>
If you cannot find the dataset from above website, please check our backup repository [direct-approval-rate-and-release-deadline-dataset](https://github.com/ZhimaoLin/direct-approval-rate-and-release-deadline-dataset), which contains a copy of the dataset that we use.


### Open Terminal on your Mac and direct to our repo directory, `direct-approval-rate-and-release-deadline/step1` using command `cd` <br>
  If you do not know how to use command `cd`, you can Google it or check this [tutorial](https://macpaw.com/how-to/use-terminal-on-mac).
### Run 
  ```python3 step1.py```



## Step 2: 
This step will generate `step2_results` folder, which contains a csv file for each repository. Each csv file stores the release date and time of each repository. 
<br>

Please note that for GitHub API requests using Basic Authentication or OAuth, you can make up to **5000** requests per hour. Since the [eclipse.platform.ui](https://github.com/eclipse/eclipse.platform.ui) has over 6000 releases, we have to collect all release date and time in 3 steps with 1 hour cooling-down time between each step.

### Add your GitHub access token
First generate your access token. If you have any problems with it, please check this help page: [https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line). Then copy and paste you token in to line 6 of `step2_1.py`, `step2_2.py`, and `step2_3.py`. 
You can also use our access token. Just simply comment line 6 and uncomment line 7. However, we highly recommend using your own GitHub access token because we cannot guarantee it will still work after May 1st, 2019. 

### Run 
  ```python3 step2_1.py```

### Wait for 1 hour after finishing previous step due to GitHub API limitations. 

### Run 
  ```python3 step2_2.py```

### Wait for 1 hour after finishing previous step due to GitHub API limitations. 

### Run 
  ```python3 step2_3.py```



## Step 3: 
This step will generate the .csv file for each repository. They are stored at `results/<repository name>/` separately. The csv file has the following structure:

|date|commit_id|findbugs|pmd|
|:-------------------|:---------:|:------:|:------:|
|2015-11-03 09:39:13|601ce|2|79|
|2015-11-03 09:39:13|8da58|3|79|
|2015-11-03 15:53:24|b66b8|5|77|

* `date` column contains the commit time of the commit. It is in the format: `YYYY-MM-DD HH:MM:SS`.
* `commit_id` column contains the first 5 characters of the commit sha. 
* `findbugs` column contains the number of warning/errors detected by Findbugs.
* `pmd` column contains the number of warning/errors detected by PMD.

### Run 
  ```python3 step3.py```

## Step 4: 
This step will generate all plots and charts asked by the assignment into [`images` folder](https://github.com/cmput402-w19/assignment5-sca-sz/tree/master/images).
* `<Repository name>_fingbugs.png` contains the box-plot of Fingbugs of that repository.
* `<Repository name>_pmd.png` contains the box-plot of PMD of that repository.
* `<Repository name>_line_chart.png` contains the line chart of the number of detected warnings/errors of that repository.

### Run 
  ```python3 step4.py```


# Results
### [Here is our results](https://github.com/cmput402-w19/assignment5-sca-sz/blob/master/Results.md)


# References