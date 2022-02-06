import csv

with open('./assets/addresses.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

  headertable = next(spamreader)

  print(headertable)
  
  for row in spamreader:
    print(', '.join(row))