from github import Github

# Create a Github instance
# For API requests using Basic Authentication or OAuth, you can make up to 5000 requests per hour. 
# For unauthenticated requests, the rate limit allows for up to 60 requests per hour.
g = Github('9fc70c72f642a8979bc0788cdd90d3c9f23cd2a2')

# repo_full_name_list = ['eclipse/eclipse.platform.ui', 'eclipse/linuxtools', 'eclipse/jgit', 'eclipse/egit', 'couchbase/couchbase-jvm-core', 'couchbase/ns_server', 'couchbase/testrunner', 'couchbase/ep-engine', 'couchbase/indexing', 'couchbase/couchbase-java-client', 'couchbase/spymemcached']

# repo_full_name_list = ['eclipse/jgit', 'eclipse/egit']
repo_full_name_list = ['eclipse/egit']


for repo_full_name in repo_full_name_list:

    repo = g.get_repo(repo_full_name)
    print('Open repo: ' + repo.name)

    tag_list = repo.get_tags()

    print(tag_list.totalCount)
    print()

    for t in tag_list: 
        print(t.name)
        # print(t.commit.sha)
        print(t.commit.commit.committer.date)
        print('\n')
