#!/usr/bin/env python3
import argparse
import random
from os import listdir
from webbrowser import open as wopen

# Command line arguments
parser = argparse.ArgumentParser(description='Working toolkit')
parser.add_argument('-p', '--pages', nargs='+', 
                    help="The pages you want to work on")
parser.add_argument('-n', '--name', 
                    help="Name of the file, default is the first page number")
parser.add_argument('-r', '--random', action='store_true',
                    help="Set this flag if you want to browse a random page")
parser.add_argument('-v2', '--volume_2', action='store_true',
                    help="Set this flag if you want to work on volume 2")
args = parser.parse_args()

# Image URL
URL_V1 = "http://library.ctext.org/s1890343/s1890343_{}.png"
URL_V2 = "http://library.ctext.org/s1890344/s1890344_{}.png"
# Page URL
URL_P1 = "http://ctext.org/library.pl?if=gb&file=92738&page={}"
URL_P2 = "http://ctext.org/library.pl?if=gb&file=92739&page={}"
# Max Page number
MAX_V1 = 204
MAX_V2 = 224

if args.volume_2:
    max_page = MAX_V2
    url = URL_V2
    url_p = URL_P2
else:
    max_page = MAX_V1
    url = URL_V1
    url_p = URL_P1

# Browsing mode
if args.random:
    page = random.randint(1, max_page)
    wopen(url_p.format(str(page)), new=2, autoraise=True)

# Generating Markdown mode
elif args.pages:
    if max([int(num) for num in args.pages]) > max_page:
        raise ValueError("The last page of this volume is {}".format(max_page))

    # Getting file name
    fp = 'p' + args.name + '.md' if args.name else 'p' + args.pages[0] + '.md'

    # Check duplicate
    for entry in listdir('.'):
        if entry == fp:
            raise NameError("The file exists, please give another filename by \
                            using -n or use the default name instead")

    # Write the file
    with open(fp, 'w') as out:
        out.write("[//]: # (scanned texts)\n")
        for page in args.pages[::-1]:
            out.write('<img src="{}" width="170">\n'.format\
                      (url.format(str(page).zfill(4))))
        out.write("\n[//]: # (texts)\n")

    print("{} is generated".format(fp))

