import pandas as pd
import sys

def main():
    csv_file_path = './corp/metadata/'
    txt_file_path = './corp/discussion/'

    repo_list = ['indexing']

    for repo_name in repo_list:

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

        review_table.loc[:, 'start_date'] = pd.Series('xxx', index=review_table.index)
        review_table.loc[:, 'start_time'] = pd.Series('xxx', index=review_table.index)
        review_table.loc[:, 'close_date'] = pd.Series('===', index=review_table.index)
        review_table.loc[:, 'close_time'] = pd.Series('===', index=review_table.index)

        print(review_table[['review_number', 'start_date', 'close_date']])


        for index, row in review_table.iterrows():
            review_number = str(row['review_number'])
            revision_number = str(row['revision_number'])

            discussion_file_name_first = review_number + "_rev1_discussion.txt"
            discussion_file_name_last = review_number + "_rev" + revision_number + "_discussion.txt"

            # Find code review start date
            f = open(txt_file_path + repo_name + '/' + review_number + '/' + discussion_file_name_first, 'r')
            lines = f.readlines()
            start_date = ''
            start_time = ''

            for l in lines:
                if 'date: ' in l:
                    date = l.split()
                    start_date = date[1]
                    start_time = date[2]
                    break
            review_table.loc[index, 'start_date'] = start_date
            review_table.loc[index, 'start_time'] = start_time
            f.close()

            # Find code review close date
            f = open(txt_file_path + repo_name + '/' + review_number + '/' + discussion_file_name_last, 'r')
            lines = f.readlines()
            close_date = ''
            close_time = ''

            for l in lines:
                if 'date: ' in l:
                    date = l.split()
                    close_date = date[1]
                    close_time = date[2]

            review_table.loc[index, 'close_date'] = close_date
            review_table.loc[index, 'close_time'] = close_time

            f.close()

        review_table.to_csv(repo_name + '_result.csv')





        print('Finish repository: ' + repo_name)

        # print(review_table[['review_number', 'start_date', 'close_date']])



if __name__ == "__main__":
    main()