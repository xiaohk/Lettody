import argparse
from os import listdir

# Command line arguments
parser = argparse.ArgumentParser(description='Markdown generator')
parser.add_argument('-p', '--pages', nargs='+', 
                    help="The pages you want to work on")
parser.add_argument('-n', '--name', 
                    help="Name of the file, default is the first page")
args = parser.parse_args()

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
    for page in args.pages:
        out.write('<img src="http://library.ctext.org/s1890343/s1890343_0{}.png" width="170">\n'.format(page))

    out.write("\n[//]: # (texts)\n")

print("{} is generated".format(fp))

