#Nich willich DAT-129 2-20-20
#Capital JSON project

import csv
import json
#Creates the dictionary for completed projects, and a list for projects with missing componants
Completedprojects = {}
Incompletelist =  []

#Opens the csv file and uses the DictReader to read the dictionaries in the file, and creates a new dict for the projects that are marked as completed

with open('capital.csv') as datafile:
    read = csv.DictReader(datafile)
    for row in read:
        
        if row['status'] == 'Completed':
        
            append = row['id']
            #adds the id of each project to dict
            info= [row['fiscal_year'], row['start_date'], row['area'], row['asset_type'], row['status']]
            #adds the desired information to the corrosponding id in the new completed projects dict
            Completedprojects[append] = info
        else:
            append = row['id']
            #adds the id of each project to dict
            info= [row['fiscal_year'], row['start_date'], row['area'], row['asset_type'], row['status']]
            #adds the desired information to the corrosponding id in the new completed projects dict
            Completedprojects[append] = info
# for loop that check each of the rows in the dictionary for blank items and adds them to the incomplete list

for row in Completedprojects:
    
     if Completedprojects[row][0] == '':
         Incompletelist.append(row)
     if Completedprojects[row][1] == '':
         Incompletelist.append(row)
     if Completedprojects[row][2] == '':
         Incompletelist.append(row)
     if Completedprojects[row][3] == '':
         Incompletelist.append(row)
     if Completedprojects[row][4] == '':
         Incompletelist.append(row)
    
with open ('Completedprojects', 'w') as dumpfile:
    json.dump(Completedprojects, dumpfile, indent=1,sort_keys=True)
    dumpfile.write('\n')


    
#variables for user input 
fiscalyear = str('')
startdate = str('')
area = str('')
asset = str('')
status = str('')

#writes user input criteria to json file
with open('criteria.json') as criteria:
    search = json.load(criteria)
    
    print('Enter search criteria')
    var = input(str())
    if var == 'fiscal_year':
        print('Enter fiscal year desired')
        fy = input(str())
        search ['fiscal_year'] = fy
    if var == 'start_date':
        print('enter start date')
        sd = input(str())
        search ['star_date'] = sd
    if var == 'area':
        print('enter area')
        a = input(str())
        search ['area'] = a
    if var == 'asset_type':
        print('enter asset type')
        at = input(str())
        search ['asset_type'] = at
    if var == 'status':
        print('enter project status')
        ps = input(str())
        search ['project_status'] = ps
    
    json.dump(search,criteria)