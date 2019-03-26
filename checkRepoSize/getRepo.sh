repoUrl="RepoUrls.txt"
while IFS= read -r repoUrl
do
  git clone $repoUrl
done < "$repoUrl"