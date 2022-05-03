cd api; pip freeze > requirements.txt; git add -A; git commit -m "update dependencies"; git push origin master;cd ..; git push origin `git subtree push --prefix api heroku master` --force
