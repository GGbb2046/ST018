import csv

with open('Subjects.csv', 'r') as csv_file:
    sample_reader = csv.reader(csv_file)
    data = list(sample_reader) 
    
    
for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j]= int(data[i][j])   
print(data)

with open('Subjects_1.csv','w') as fout:
    sample_writer = csv.writer(fout)
    for i in data:
        sample_writer.writerow([sum(i)])