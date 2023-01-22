import csv
import re 
new_list=[] 
pattern = r'\/city\/directory\/[a-zA-Z0-9]+\.html' 
pattern_contact1 = r'\/good\/[a-zA-Z0-9]+\/owner_info'
pattern_contact2 = r'\/bulletin\/[a-zA-Z0-9]+\/ajax_contact'
with open('exp1.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        row_new=[]
        row_new.append(row[0][-1])
        row_new.extend(row)
        match = re.search(pattern, row[2]) 
        match_contact1 = re.search(pattern_contact1, row[2]) 
        match_contact2 = re.search(pattern_contact2, row[2])
        if match:
            row_new.append('Card')
        elif match_contact1:
            row_new.append('Contact')
        elif match_contact2:
            row_new.append('Contact')
        else:
            row_new.append('Not found')
        new_list.append(row_new)




with open('exp2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(new_list)
