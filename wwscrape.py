# -*- coding: UTF-8 -*-

#Modules we need
import os
import subprocess
import time
import json
import sys
import re
import base64
import requests
import argparse
import random
import lxml
import urlparse
import mechanize
from datetime import datetime
from bs4 import BeautifulSoup

#color codes
black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
blue = lambda text: '\033[0;34m' + text + '\033[0m'
magenta = lambda text: '\033[0;35m' + text + '\033[0m'
cyan = lambda text: '\033[0;36m' + text + '\033[0m'
white = lambda text: '\033[0;37m' + text + '\033[0m'

#stuff for the setup
#|color list for the random module
colors = [red,white,blue,cyan,yellow,magenta,green]
#|disables all warnings from the requests module
requests.packages.urllib3.disable_warnings()

ERASE_LINE = '\033[2K\033[1G'

target_links = []
parameter = []
is_redirecting_check = []

def banner():
    banner = '''
__  _  ____  _  ________ ________________  ______   ____
\\ \\/ \\/ /\\ \\/ \\/ /  ___// ___\\_  __ \\__  \\ \\____ \\_/ __ \\
 \\     /  \\     /\\___ \\  \\___|  | \\// __ \\|  |_> >  ___/
  \\/\\_/    \\/\\_//____  >\\___  >__|  (____  /   __/ \\___  >
                     \\/     \\/           \\/|__|        \\/
                                by Mrdebugger
'''
    random_color = random.choice(colors)
    print (random_color(banner))

def extract_links(url):
    try:
        response = requests.get(url)
        return re.findall('(?:href=")(.*?)"', response.content)
    except requests.exceptions.SSLError:
        time.sleep(0.1)
    except requests.exceptions.ConnectionError:
        time.sleep(0.1)
    except requests.exceptions.InvalidSchema:
        time.sleep(0.1)

def crawl(url):
    try:
        all_links = extract_links(url)
        for link in all_links:
            link = urlparse.urljoin(url, link)
            if '#' in link:
                link = link.split('#')[0]
            if url in link and link not in target_links:
                parameter.append(link)
                sys.stdout.write(ERASE_LINE)
                sys.stdout.write("[crawling: " + link + "]")
                sys.stdout.flush()
                sys.stdout.write(ERASE_LINE)
                target_links.append(link)
                crawl(link)
    except TypeError:
        pass

def url_function(url):
    start_time = datetime.now()
    start_time_new = start_time.strftime("%H:%M:%S")
    print ("[{}] starting\n").format(start_time_new)
    print (yellow("[*] " + white("Extracing all urls directories and files\n\n")))
    crawl(url)
    my_new_param = set(parameter)
    my_new_param_list = list(my_new_param)
    for param in my_new_param_list:
        param = param.strip()
        is_redirecting = requests.get(str(param))
        sys.stdout.write(ERASE_LINE)
        sys.stdout.write("[Checking: " + str(param) + "]")
        sys.stdout.flush()
        sys.stdout.write(ERASE_LINE)
        is_redirecting_check.append(is_redirecting.url)
    sys.stdout.write(ERASE_LINE)
    print (cyan("[*] " + white("All Urls directories and files:\n")))
    my_new_redirects = set(is_redirecting_check)
    my_new_redirects_list = list(my_new_redirects)
    for is_redirecting in my_new_redirects_list:
        print (green("[+] " + white("Found: " + str(is_redirecting))))

    stop_time = datetime.now()
    stop_time_new = stop_time.strftime("%H:%M:%S")
    print ("\n[{}] Done\n").format(stop_time_new)

os.system("clear")
try:
    url = sys.argv[1]
    banner()
    url_function(url)
except IndexError:
    try:
        list = sys.argv[1]
        banner()
        list_fucntion(list)
    except IndexError:
        os.system("clear")
        banner()
        print ("provide at least one option (a url)\n\nUrl Example: \npython wwscrape.py https://test.com")
        sys.exit(0)
