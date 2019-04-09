# What is the Relationship between Code Review Direct Approval Rate and Release Deadline?

# Authors
* Shuonan Pei
* Zhimao Lin

# Dataset Detail
The [CROP](https://crop-repo.github.io) website provides code review record of 11 repositories in a period of time.
To see the detail of our data. Please go to [https://crop-repo.github.io/](https://crop-repo.github.io/) and click `Dataset Details` on the left-hand side bar.



# We picked following 10 repositories for our research:
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

## Reproduce steps
## Download Data
[https://crop-repo.github.io/](https://crop-repo.github.io/)
### Step0: Install dependencies
1. Update your MacOS to MacOS Mojave Version 10.14.3 (The latest version on March 20th, 2019) <br> 
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

6. Install Git version 2.17.2 (Apple Git-113)
    Open Terminal on your Mac and run 
    ```git --version```
    to check if you have git on your Mac. 
    If you do not have git on your Mac, you can install it [here](https://git-scm.com/download/mac). For more details, you can check [Git documentation](https://git-scm.com/)

## Step 1: 
This step will generate `RepoFullNames.txt` that contains all the repository name. Each line contains a repository name. It will also generate `commits` folder, which contains the 30 commit sha and commit time of each repository.

### Open Terminal on your Mac and direct to our repo directory, `assignment5-sca-sz` using command `cd` <br>
  If you do not know how to use command `cd`, you can Google it or check this [tutorial](https://macpaw.com/how-to/use-terminal-on-mac).
### Run 
  ```python3 step1.py```

## Step 2: 
This step will generate `results` folder, which contains the analysis result of each repository using Findbugs and PMD. After you open `results` directory, you will see 5 directories, which are named after the 5 repository names. Each directory contains the result of the analysis of the repository. Results are divided in to 2 folders: `findbugs` and `pmd`. which contains the result of Findbugs and PMD respectively. Each folder contains 30 .txt files with the name of the first 5 characters of its commit sha. Findbugs results of the 30 commits are stored in the `findbugs` folder. PMD results of the 30 commits are stored in the `pmd` folder. 

### Run chmod command to give the permision to run the shell script step2.sh
  ```chmod +x step2.sh```
### Run 
  ```./step2.sh```

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