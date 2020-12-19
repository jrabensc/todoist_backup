#!/usr/bin/env python3

import todoist
import requests
import argparse
import os
import sys

parser = argparse.ArgumentParser(description = 'Save a backup from Todoist.')

parser.add_argument('token', help = 'Token to access the Todoist API.')
parser.add_argument('path', help = 'Path where the zip file should be saved to.')                

args = parser.parse_args()

input_token = args.token
input_path = args.path

def check_input(token, output_path):
    if os.path.isdir(output_path) == False:
      sys.exit('No or bad path provided.')
    if len(token) != 40:
      sys.exit('No or bad token provided.')

def get_todoist_bak(token, output_path):
    # sanity check
    check_input(token = token, output_path = output_path)
    # create API object
    api = todoist.TodoistAPI(token)
    # get list of all available backups
    backups = api.backups.get()
    # check if API error
    try:
      if backups['http_code'] == 403:
        sys.exit('API Error: Invalid token')
    except TypeError:
        pass; 
    # get latest backup url
    url = backups[0]['url']
    # get latest timestamp
    timestamp = backups[0]['version']
    # define headers
    header = {'Authorization':'Bearer '+ token}
    # download file
    response = requests.get(url, headers = header)
    # check for http error
    response.raise_for_status()
    # define filename using the timestamp from the todoist backup
    file_name = 'todoist_backup_' + timestamp + '.zip'
    # define save path
    save_path = output_path + file_name
    # save file
    with open(save_path, 'wb') as fd:
      for chunk in response.iter_content(chunk_size=128):
          fd.write(chunk)
    print('Successfully saved file '+file_name+' to '+output_path+'.')

get_todoist_bak(token = input_token, output_path = input_path)

