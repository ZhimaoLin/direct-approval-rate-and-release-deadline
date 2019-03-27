from github import Github
import os

# Create a Github instance
# For API requests using Basic Authentication or OAuth, you can make up to 5000 requests per hour. 
# For unauthenticated requests, the rate limit allows for up to 60 requests per hour.
g = Github('9fc70c72f642a8979bc0788cdd90d3c9f23cd2a2')
# g = Github()

repo_full_name = 'eclipse/eclipse.platform.ui'


repo_name = repo_full_name.split('/')[1]

repo = g.get_repo(repo_full_name)
tag_list = repo.get_tags()
print('==============================')
print('Accessing repo: [' + repo.name + ']')


release_date_file_name = os.path.join('./step2_results/', repo_name + "_release_date.txt" )
release_date_file = open(release_date_file_name, "a")

print('Continue getting release date in repo: ' + repo_name + ' after 1 hour.')
print('==============================')


total_count = tag_list.totalCount

for t in tag_list[4500:]: 
    release_date_file.write(str(t.commit.commit.committer.date) + '\n')

release_date_file.close()