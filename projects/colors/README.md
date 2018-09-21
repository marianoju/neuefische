# Colors 

## About 

This project is based on Randall Munroe's “Color Name Survey”, see 
- [Color Name Survey (blogpost)](https://blog.xkcd.com/2010/03/01/color-name-survey/) 
- [Color Name Survey“ (questionnaire)](https://web.archive.org/web/20100303073002/http://aram.xkcd.com/color/)
- [Color Survey Results (blogpost)](https://blog.xkcd.com/2010/05/03/color-survey-results/) 
- [Dataset (SQLite dump, 84 MB .tar.gz file)](http://xkcd.com/color/colorsurvey.tar.gz)

*arbitrary examples for color palettes and color terms*
- [HTML Color Names](https://www.w3schools.com/colors/colors_names.asp)
- [216 web safe colors](https://www.colorhexa.com/web-safe-colors)
- [List of colors by names](https://www.colorhexa.com/color-names)


## Tables 

1. users 
2. answers 
3. names 


## Table Headers 

- id INTEGER PRIMARY KEY, user_id, datestamp, r, g, b, colorname 
- id INTEGER PRIMARY KEY, colorname, numusers, numinstances 
- id INTEGER PRIMARY KEY, user_key, datestamp, ip, language, monitor, temperature, gamma, colorblind, ychrom, samplecolors, spamprob 


## SQLite dumps and sizes 

1. satfaces_sqldump
	- answers = 1,894,522
	- names = 127,761
	- users = 68,781

2. mainsurvey_sqldump
	- answers = 3,408,039
	- names = 183,429
	- users = 152,403


## Data wrangling with Bash 

Checks the first lines of the SQL dump file: 

`
$ head mainsurvey_sqldump.txt
`

Checks for tables in the SQL dump file: 

`
$ grep 'CREATE TABLE' mainsurvey_sqldump.txt
`

Greps all lines including `users`, `answers` and `names` and writes them to dedicated text files: 

`
$ grep 'users' mainsurvey_sqldump.txt > mainsurvey_sqldump_users.txt
$ grep 'answers' mainsurvey_sqldump.txt > mainsurvey_sqldump_users.txt
$ grep 'names' mainsurvey_sqldump.txt > mainsurvey_sqldump_users.txt
`

Removes all `,` from files: 

`
$ find mainsurvey_sqldump_* -type f -exec sed -i 's/,/\ /g' {} \;
`

Checks the number of lines per file: 
`
grep -c "." mainsurvey_sqldump_*
`

Checks the file sizes: 

`
$ ls -hl mainsurvey_sqldump_*
`

