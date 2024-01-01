cd /config/
git add .
git commit -m "config files on `date +'%d-%m-%Y %H:%M:%S'`" >/config/git_log.txt 2>&1
git push -u origin master --force
#pushes updates to github