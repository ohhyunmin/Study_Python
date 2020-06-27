import csv

def save_to_file(pInfo):
  file = open("Study_Python.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["TITLE, PRICE"])
  
  for info in pInfo:
    writer.writerow(list(info.values()))
  return