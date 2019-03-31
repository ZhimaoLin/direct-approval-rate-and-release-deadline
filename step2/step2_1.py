from github import Github
import os

# Create a Github instance
# For API requests using Basic Authentication or OAuth, you can make up to 5000 requests per hour. 
# For unauthenticated requests, the rate limit allows for up to 60 requests per hour.
g = Github('9fc70c72f642a8979bc0788cdd90d3c9f23cd2a2')

#repo_full_name_list = ['eclipse/eclipse.platform.ui', 'eclipse/linuxtools', 'eclipse/jgit', 'eclipse/egit', 'couchbase/couchbase-jvm-core', 'couchbase/ns_server', 'couchbase/testrunner', 'couchbase/ep-engine', 'couchbase/indexing', 'couchbase/couchbase-java-client', 'couchbase/spymemcached']
repo_full_name_list = ['eclipse/linuxtools', 'eclipse/jgit', 'eclipse/egit', 'couchbase/couchbase-jvm-core', 'couchbase/ns_server', 'couchbase/testrunner', 'couchbase/ep-engine', 'couchbase/couchbase-java-client', 'couchbase/spymemcached']


# repo_full_name_list = ['eclipse/jgit', 'eclipse/egit']
# repo_full_name_list = ['couchbase/couchbase-jvm-core']

try: 	
    os.mkdir('step2_results')
except:
    print("step2_results folder exists.")


for repo_full_name in repo_full_name_list:
    repo_name = repo_full_name.split('/')[1]

    repo = g.get_repo(repo_full_name)
    tag_list = repo.get_tags()
    print('==============================')
    print('Accessing repo: [' + repo.name + ']')
    


    release_date_file_name = os.path.join('./step2_results/', repo_name + "_release_date.csv" )
    release_date_file = open(release_date_file_name, "w")

    #release_date_file.write('Total number of releases: ' + str(tag_list.totalCount) + '\n')
    
    print('Total number of releases: ' + str(tag_list.totalCount))
    print('==============================')

    for t in tag_list: 
        # print(t.name)
        # print(t.commit.sha)
        # print(t.commit.commit.committer.date)
        # print('\n')

        #release_date_file.write(str(t.name) + '\n')
        #release_date_file.write(str(t.commit.sha) + '\n')
        release_date_file.write(str(t.commit.commit.committer.date) + '\n')

    release_date_file.close()
