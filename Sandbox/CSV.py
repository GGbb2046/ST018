import csv
with open('Galab.csv','r') as csv_file:
    sample_reader = csv.reader(csv_file)
    sample_text=list(sample_reader)
print(sample_text[0][0][0:2])