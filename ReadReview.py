import pandas as pd
import sys

def main():
    csv_file_name = sys.argv[1]
    print("Processing file: " + csv_file_name)

    revision_number_without_change = int(sys.argv[2])
    print("Revision number without change: %d" %revision_number_without_change)

    read_file = pd.read_csv(csv_file_name)


    index = read_file.groupby(['review_number'])['revision_number'].transform(max) == read_file['revision_number']

    groupby_table = read_file[index]
    final_table = groupby_table[['review_number', 'revision_number', 'status', 'author', 'url']].copy()

    final_table.loc[final_table.status != 'MERGED', 'status'] = 'Rejected'
    final_table.loc[(final_table.status != 'Rejected') & (final_table.revision_number <= revision_number_without_change), 'status'] = 'DirectlyApprove'
    final_table.loc[(final_table.status != 'Rejected') & (final_table.revision_number > revision_number_without_change), 'status'] = 'ApproveAfterChange'

    print(final_table[['review_number', 'revision_number', 'status']])





    

    
                




if __name__ == "__main__":
    main()