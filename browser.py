# *******************************************************************
# ***              Text based browser project of Hyperskill.org   ***
# *******************************************************************
#
#            Tests require Cachefile to be free of html Tags
#            requires modification of function get_page()
#
#
#


import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import init, Fore


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def filename(url):
    # https:// cutoff
    if url[0:8] == 'https://':
        name = url[8:]
    elif url[0:7] == 'http://':
        name = url[7:]
    else:
        name = url
    name = name.replace('/', '_',)

    # look for '?' and cutoff if found
    if '?' in name:
        index = 0
        for i in range(len(name)):
            if name[i] == '?':
                index = i
                break
        name = name[0:index]

    return name + '.txt'


def read_cached(name, path):
    if os.path.isfile(f'{path}/{name}'):
        with open(f'{path}/{name}', encoding='utf-8') as file:
            return file.read()
    else:
        return False


def write_cached(name, path, webpage):
    with open(f'{path}/{name}', 'w', encoding='utf-8') as file:
        for line in webpage:
            file.write(f"{line}")


def output(parts):
    for tag in parts:
        # Nestet Tags? => call recursion with new list items
        try:
            new = list(tag.children)
            if len(new) > 1:
                output(list(tag.children))
                continue
        except:
            pass

        # No nested Tags? Proceed
        if isinstance(tag, str):
            print(tag, end='')
        elif tag.name == 'a':
            print(Fore.BLUE + tag.get_text() + Fore.BLACK, end='')
        elif tag.name == 'title':
            print(Color.BOLD + tag.get_text() + Color.END)
        elif tag.name == 'span':
            print(tag.get_text())
        elif tag.name == 'strong':
            print(Color.BOLD + tag.get_text() + Color.END, end='')
        elif tag.name == 'p':
            print(tag.get_text())
        elif tag.name == 'br':
            pass
        elif tag.name is None:
            pass
        else:
            pass


def scrape(webpage):
    soup = BeautifulSoup(webpage, 'html.parser')
    output(soup.title)
    paragf = soup.find_all('p')
    for line in paragf:
        parts = list(line.children)
        output(parts)



def get_page(url, path):
    name = filename(url)
    cached = read_cached(name, path)
    if not cached:
        # body = []
        tab = requests.get(url)
        if 200 <= tab.status_code < 400:

            # soup = BeautifulSoup(tab.content, 'html.parser')
            # body.append(soup.title)
            # output(soup.title)
            # paragf = soup.find_all('p')
            # for line in paragf:
            #    body.append(line.get_text())
            #    parts = list(line.children)
            #    output(parts)

            #write_cached(name, path, body)
            write_cached(name, path, tab.text) #Remove 4 test
            scrape(tab.content) # Remove 4 test

        else:
            print(f'Error:{tab.status_code}')
    else:
        scrape(cached)


#########################################
### Program starts here #################
#########################################

init()

args = sys.argv
if len(args) >= 2:
    dir_name = args[1]
else:
    dir_name = 'resources'

if not os.path.isdir(dir_name):
    os.mkdir(dir_name)

history = []
command = input()
if command == '':
    command = 'doc.python.org'

while command != "exit":
    page = command
    if '.' not in page:
        print('error : Incorrect URL')
    elif page[0:4] != 'http':
        page = 'https://' + command
        get_page(page, dir_name)
    else:
        page = command
        get_page(page, dir_name)

    # Next command = 'back' ?
    command = input()
    if command == 'back':
        if len(history) > 0:
            command = history.pop()
        else:
            command = 'exit'
    else:
        history.append(page)
