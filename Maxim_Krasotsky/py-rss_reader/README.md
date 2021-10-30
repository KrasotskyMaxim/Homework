# Content
- ***rss_package*** folder for storing program modules
- ***news_data*** folder for created pdf and json files
- ***tests*** folder for test files
- ***venv*** folder contains dependendences, settings and etc...
- ***requirements.txt*** for nessesary modules
- ***rss_reader.py*** is main program file
- ***setup.py*** is settings for client
- additional ***.eggs*** and ***rss_reader.egg-info*** folders
# Dynamic files
during the execution of the program, a .log file and a local .scv storage will be created, and a file with html markup will be created when you call --to-html
```
rss_parser.log
local_Storage.scv
rss_news.html
```