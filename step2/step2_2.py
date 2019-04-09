from github import Github
import os


# Please replace "<Your GitHub Access Token>" with your own GitHub Access Token
g = Github("<Your GitHub Access Token>")
# g = Github('9fc70c72f642a8979bc0788cdd90d3c9f23cd2a2')

repo_full_name = 'eclipse/eclipse.platform.ui'

repo_name = repo_full_name.split('/')[1]

repo = g.get_repo(repo_full_name)
tag_list = repo.get_tags()
print('==============================')
print('Accessing repo: [' + repo.name + ']')


release_date_file_name = os.path.join('./step2_results/', repo_name + "_release_date.csv" )
release_date_file = open(release_date_file_name, "w")

print('Total number of releases: ' + str(tag_list.totalCount))
print('==============================')


total_count = tag_list.totalCount

for t in tag_list[0:4500]: 
    release_date_file.write(str(t.commit.commit.committer.date) + '\n')

release_date_file.close()