# coding: utf-8
import csv
new = open('new_fellowship.csv', 'w')
fieldnames = ['id','name','email','paper','purpose','college','ws_date','is_coordinator']
writer = csv.DictWriter(new,fieldnames=fieldnames)
writer.writeheader()
google_sheet = open('/home/binson/Downloads/Self Learning Participants - Sheet1.csv')
reader_google_sheet= csv.DictReader(google_sheet)
googl_sheet_list = [i['Email'] for i in reader_google_sheet]
march = open('data_fellowship.csv')
reader_march = csv.DictReader(march)
for row in reader_march:
    name_title = row['name']
    email = row['email']
    college = row['college']
    purpose = 'sel'
    if email not in googl_sheet_list:
        writer.writerow({'id':'','name':name_title,'email':email,'paper':row['paper'],'purpose':purpose,
        'college':college,'ws_date':'March 2018','is_coordinator':0})
new.close()
