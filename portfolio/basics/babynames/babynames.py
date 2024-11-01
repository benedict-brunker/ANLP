#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

# """Baby Names exercise

# Define the extract_names() function below and change main()
# to call it.

# For writing regex, it's nice to include a copy of the target
# text for inspiration.

# Here's what the html looks like in the baby.html files:
# ...
# <h3 align="center">Popularity in 1990</h3>
# ....
# <tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
# <tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
# <tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
# ...

# Suggested milestones for incremental development:
#  -Extract the year and print it
#  -Extract the names and rank numbers and just print them
#  -Get the names data into a dict and print it
#  -Build the [year, 'name rank', ... ] list and print it
#  -Fix main() to use the extract_names list
# """

def extract_names(filename):
  # """
  # Given a file name for baby.html, returns a list starting with the year string
  # followed by the name-rank strings in alphabetical order.
  # ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  # """
  # +++your code here+++

  f = open(filename, "r", encoding='utf-8')
  file_data = f.read()
  year_match = re.search(r'Popularity in (\d\d\d\d)', file_data)
  year = year_match.group(1)
  print("Year: ", year)
  # on the HTML, the names are ordered by rank, but the task asks us to order alphabetically. 
  # so, we'll have to first findall name-rank tuples (of three: ['rank', 'male', 'female']
  tuples = re.findall(r'<td>(\d+)</td><td>([A-Z]\w+)</td><td>([A-Z]\w+)', file_data)
  # we'll turn these tuples into some kind of data structure like a dictionary
  name_ranks = {}
  for tuple in tuples: 
    rank = tuple[0]
    m_name = tuple[1]
    f_name = tuple[2]
    name_ranks[m_name] = rank
    name_ranks[f_name] = rank
  # we'll instantiate a list with the year 
  # then we'll sort by name alphabetically, adding results to a list as we go
  alphabetized = sorted(name_ranks.items())
  # for key, value in name_ranks.items():
  #   print(key, value)
  alphabetized.insert(0, year)
  print(alphabetized[0:10])
  return alphabetized
  # then we're done 



def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  print("Main function called")
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  print("Script is running")
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  if summary == False:
    names = extract_names(args[0])
    # for name in names: 
    #   print(name)
    return

  elif summary == True: 
    output_file = args[0]
    del args[0]
    names = extract_names(args[0])
    with open(f'{output_file}', 'w') as f:
      f.writelines(names)
      return 
 
if __name__ == '__main__':
  print("About to call main")
  main()
