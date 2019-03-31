import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime as dt

# repo_list = ['couchbase-jvm-core', 'ep-engine', 'eclipse.platform.ui', 'couchbase-java-client', 'testrunner', 'ns_server', 'jgit', 'egit', 'org.eclipse.linuxtools', 'spymemcached']
repo_list = ['couchbase-jvm-core']

year_range_dic = {'couchbase-jvm-core': (2015, 2016), \
                    'ep-engine': (2012, 2016), \
                    'eclipse.platform.ui': (2014, 2016), \
                    'couchbase-java-client': (2013, 2016), \
                    'testrunner': (2011, 2015), \
                    'ns_server': (2011, 2016), \
                    'jgit': (2010, 2016), \
                    'egit': (2010, 2016), \
                    'org.eclipse.linuxtools': (2013, 2016), \
                    'spymemcached': (2011, 2016)}

try: 	
    os.mkdir('step4_results')
except:
    print("step4_results folder exists.")

for repo in repo_list:
    csv_file_name = repo + "_final.csv"
    df = pd.read_csv(os.path.join('../step3/step3_results/', csv_file_name))
    df['close_date'] = pd.to_datetime(df['close_date'])

    release_date_file_name = repo + "_release_date.csv"
    rd = pd.read_csv(os.path.join('../step2/step2_results/', release_date_file_name), header=None, names=['release_date'])
    rd['release_date'] = pd.to_datetime(rd['release_date'])
    
    
    
    



    closed_to_release = df.loc[(df.CloseToReleaseDate == True)].copy()
    far_from_release = df.loc[(df.CloseToReleaseDate == False)].copy()


    bp = df.boxplot(by='CloseToReleaseDate', column=['DirectlyApproveRate'])
    plt.suptitle("")
    bp.set_ylabel("Directly Approve Rate")
    bp.set_xlabel("Is Closed to Release Date?")
    bp.set_title('Boxplot of Directly Approve Rate of ' + repo)
    plt.savefig(os.path.join("./step4_results/", repo + "_boxplot.png"), format="png")
    plt.close()

    
    # line_plot = df.plot(x='close_date', y=['DirectlyApproveRate'], figsize=(20,5), title=repo, rot=270)
    
    year_range = year_range_dic[repo]
    # print(year_range)
    for y in range(year_range[0], year_range[1]+1):

        rd_current_year = rd[rd['release_date'].dt.year == y].copy()

        
        df_current_year = df[df['close_date'].dt.year == y].copy()

        line_plot = df_current_year.plot(x='close_date', y=['DirectlyApproveRate'], figsize=(20,5), title="Directly Approve Rate of " + repo + " in " + str(y), rot=270)

        line_plot.set_ylabel("Directly Approve Rate")
        

        for index, row in rd_current_year.iterrows():
            line_plot.axvline(x=row['release_date'], color='r')


        line_plot.legend(["Directly Approve Rate", "Release Date"])
        plt.savefig(os.path.join("./step4_results/", repo + "_" + str(y) + "_line_chart.png"), format="png")
        plt.close()
