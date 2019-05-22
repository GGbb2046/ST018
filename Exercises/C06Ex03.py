import csv
with open('Subjects.csv', 'w') as csv_file:
    sample_writer = csv.writer(csv_file)
    sample_writer.writerow(['1', '2', '3', '4'])
    sample_writer.writerow(['5', '6', '7', '8'])
    sample_writer.writerow(['9', '10', '11', '12'])

with open('Subjects.csv', 'r') as csv_file:
    sample_reader = csv.reader(csv_file)
    data = list(sample_reader) 
    print(data)
    
for i in range(len(data)):
    for j in range(len(data[i]): 
        data[i][j] = int(data[i][j])
        print(data)
       
with open('Subjects_1.csv', 'w') as csv_file:
        sample_writer = csv.writer(csv_file)
        for i in j:
            sample_writer.writerow([sum[i]])

        