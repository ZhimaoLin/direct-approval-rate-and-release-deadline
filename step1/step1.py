import pandas as pd
import sys
import numpy as np
import os

def main():
    csv_file_path = './crop/metadata/'
    txt_file_path = './crop/discussion/'

    try: 	
        os.mkdir('step1_results')
    except:
        print("step1_results folder exists.")

    repo_list = ['couchbase-jvm-core', 'eclipse.platform.ui', 'ep-engine', 'couchbase-java-client', 'testrunner', 'ns_server', 'jgit', 'egit', 'org.eclipse.linuxtools', 'spymemcached']
    # repo_list = ['ns_server']

    for repo_name in repo_list:
        print('Processing repository: ' + repo_name)

        revision_number_without_change = 2

        read_file = pd.read_csv(csv_file_path + repo_name + '.csv')


        index = read_file.groupby(['review_number'])['revision_number'].transform(max) == read_file['revision_number']

        groupby_table = read_file[index]

        review_table = groupby_table[['review_number', 'revision_number', 'status', 'author', 'url']].copy()

        # As for the status is "NEW," at most of the cases, the review is rejected.
        # In the indexing.csv, there are 95 out of 8316 rows are NEW. Out of 95 rows, there are 37 reviews
        review_table.loc[review_table.status != 'MERGED', 'status'] = 'Rejected'
        review_table.loc[(review_table.status != 'Rejected') & (review_table.revision_number <= revision_number_without_change), 'status'] = 'DirectlyApprove'
        review_table.loc[(review_table.status != 'Rejected') & (review_table.revision_number > revision_number_without_change), 'status'] = 'ApproveAfterChange'

        # print(review_table[['review_number', 'revision_number', 'status']])

        review_table.loc[:, 'close_date'] = pd.Series(np.nan, index=review_table.index)
        review_table.loc[:, 'close_time'] = pd.Series(np.nan, index=review_table.index)

        # print(review_table[['review_number', 'start_date', 'close_date']])

        skipped_count = 0

        for index, row in review_table.iterrows():
            review_number = str(row['review_number'])
            revision_number = str(row['revision_number'])

            discussion_file_name_last = review_number + "_rev" + revision_number + "_discussion.txt"

            skipped_last = False

            try:
                f = open(txt_file_path + repo_name + '/' + review_number + '/' + discussion_file_name_last, 'r')
                f.close()
            except:
                skipped_last = True
                print('Skipped: ' + txt_file_path + repo_name + '/' + review_number + '/' + discussion_file_name_last)

            if (not skipped_last):
                # Find code review close date
                f = open(txt_file_path + repo_name + '/' + review_number + '/' + discussion_file_name_last, 'r')
                lines = f.readlines()
                close_date = ''
                close_time = ''

                l = ''

                for l in lines:
                    if 'date: ' in l:
                        date = l.split()
                        close_date = date[1]
                        close_time = date[2]
                
                # Cannot find 'date: '
                if l == '\n':
                    print('Skiped file: [' + repo_name + '/' + review_number + '/' + discussion_file_name_last + '] due to no close date')
                    skipped_count += 1

                review_table.loc[index, 'close_date'] = close_date
                review_table.loc[index, 'close_time'] = close_time

                f.close()
            else:
                # print(review_table.loc[index])
                skipped_count += 1

        print('Skipped [' + str(skipped_count) + '] reviews out of [' + str(review_table.shape[0]) + '] rows')
        # Clean some invalid rows
        # It removes a review: 21388 from ns_server repo.
        review_table = review_table.dropna(axis=0)
        review_table.to_csv(os.path.join('./step1_results/', repo_name + '_result.csv'), index=False)
        print('Finish repository: ' + repo_name + '\n')



if __name__ == "__main__":
    main()