mypath = '/Users/Hansen/Downloads/one_column'
import csv
import os
from os import listdir
from os.path import isfile, join
textfiles = [ join(mypath,f) for f in listdir(mypath) if isfile(join(mypath,f)) and '.txt' in  f]

# Output list of generator objects
o_data = []

def directory(path,extension):
  list_dir = []
  list_dir = os.listdir(path)
  count = 0
  for file in list_dir:
    if file.endswith(extension): # eg: '.txt'
      count += 1
  return count
# Open files in the succession and 
# store the file_name as the first
# element followed by the elements of
# the third column.
for afile in textfiles:
    file_h = open(afile)
    a_list = []
    a_list.append(afile)
    csv_reader = csv.reader(file_h, delimiter=' ')
    for row in csv_reader:
        a_list.append(row[directory('/Users/Hansen/Downloads/one_column','.txt')])
    # Convert the list to a generator object
    o_data.append((n for n in a_list))
    file_h.close()

# Use zip and csv writer to iterate
# through the generator objects and 
# write out to the output file
with open('output', 'w') as op_file:
    csv_writer = csv.writer(op_file, delimiter=' ')
    for row in list(zip(*o_data)):
        csv_writer.writerow(row)
op_file.close()