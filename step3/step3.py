import pandas as pd
import sys
from datetime import datetime
from datetime import timedelta

def main():
    csv_file_path = '../step1/'
    date_file_path = '../step2/step2_results/'

    #repo_list = ['indexing', 'couchbase-jvm-core', 'eclipse.platform.ui', 'ep-engine', 'couchbase-java-client', 'testrunner', 'ns_server', 'jgit', 'egit', 'org.eclipse.linuxtools', 'spymemcached']
    #repo_list = ['couchbase-jvm-core']
    repo_list = ['couchbase-jvm-core', 'ep-engine', 'couchbase-java-client', 'testrunner', 'ns_server', 'jgit', 'egit', 'org.eclipse.linuxtools', 'spymemcached']
    #repo_list = ['couchbase-jvm-core']

    date = []
    for repo_name in repo_list:
        print('Processing csv file: ' + repo_name + '_result.csv')

        if repo_name =='org.eclipse.linuxtools':
            read_file = pd.read_csv(csv_file_path + repo_name + '_result.csv')
            release_date = open(date_file_path + 'linuxtools_release_date.txt', "r")
        else:
            read_file = pd.read_csv(csv_file_path + repo_name + '_result.csv')
            release_date = open(date_file_path + repo_name + '_release_date.txt', "r")

        # collect release date and store them in a list
        for line in release_date:
            today = datetime.strptime(line.split(' ')[0], '%Y-%m-%d').date()
            previous = today + timedelta(days=-1)
            #nextDay = previous + timedelta(days=-1)
            #nextDay1 = nextDay + timedelta(days=-1)
            #nextDay2 = nextDay1 + timedelta(days=-1)
            date.append(str(today))
            date.append(str(previous))
            #date.append(str(nextDay))
            #date.append(str(nextDay1))
            #date.append(str(nextDay2))
        release_date.close()

        # generate columns for ApproveAfterChange, DirectlyApprove and Rejected
        #GroupByDate = read_file.groupby(['close_date']).size().to_frame('size')

        GroupByStatus = read_file.groupby(['close_date', 'status']).size()

        result = GroupByStatus.unstack(level=-1).fillna(0)

        # calculate the number for total commit
        result['TotalCommit'] = result.iloc[:,-3:].sum(axis=1)
        #result['TotalCommit'] = result['ApproveAfterChange']+result['DirectlyApprove']+result['Rejected']

        # calculate the number for approval rate
        #result[['ApprovalRate']] = result.iloc[:, 2].div(result.iloc[:, 4])
        result['DirectlyApproveRate'] = result['DirectlyApprove']/result['TotalCommit']

        # calculate the number for approve after change rate
        result['ApproveAfterChangeRate'] = result['ApproveAfterChange']/result['TotalCommit']

        #DirectlyApprove = read_file.loc[read_file['status'] == 'DirectlyApprove','close_date'].unique().tolist()
        #ApproveAfterChange = read_file.loc[read_file['status'] == 'ApproveAfterChange','close_date'].unique().tolist()
        #Rejected = read_file.loc[read_file['status'] == 'Rejected','close_date'].unique().tolist()
        
        #DirectlyApproveByDate = read_file[(read_file['status'] == 'DirectlyApprove') & read_file['close_date'].isin(DirectlyApprove)].groupby('close_date').size().to_frame('size')
        #ApproveAfterChangeByDate = read_file[(read_file['status'] == 'ApproveAfterChange') & read_file['close_date'].isin(DirectlyApprove)].groupby('close_date').size().to_frame('size')
        #RejectedByDate = read_file[(read_file['status'] == 'Rejected') & read_file['close_date'].isin(DirectlyApprove)].groupby('close_date').size().to_frame('size')

        result.to_csv(repo_name + '_final.csv')
       
        final = pd.read_csv('./' + repo_name + '_final.csv')

        # generate a boolean column to define whether the close date close to the commit date
        final['CloseToReleaseDate'] = 'False'
        final.loc[final['close_date'].isin(date), 'CloseToReleaseDate'] = 'True'

        final.to_csv(repo_name + '_final.csv')


        #print(final)


if __name__ == "__main__":
    main()