# Simple Todoist Backup Script

As Todoist currently (2020-12-19) lacks an automatic backup function, I wrote this script to run daily backups using cronjob.

### Requirements:

- Python3
- [todoist-python](https://pypi.org/project/todoist-python/)
- [API-Token](https://todoist.com/prefs/integrations)

### Usage

1. ```git clone https://github.com/jrabensc/todoist_backup.git```
2. ```chmod +x make_todoist_backup.py```
3. Run script and append the token and output path to the script like this: ```./make_todoist_backup.py a0cdb278227e822a73f4d71c878c4583be40e15a /home/johannes/Downloads/```
