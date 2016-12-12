#!/usr/bin/python3

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

with open("../final_project/final_project_dataset.pkl", "rb") as f:
    enron_data = pickle.load(f)

# Q1: How many data points (people) are in the dataset?-----------------------
print('Totally '+ str(len(enron_data)) +' people are in the dataset.')

# Q2: For each person, how many features are available?------------------------
count_features = str(len(enron_data['METTS MARK']))
print('For each person, ' + count_features + ' features are available.')

# Q3: How many POIs are there in the E+F dataset? -----------------------------
count_poi = 0
for _, value in enron_data.items():
    if value['poi'] == True:
        count_poi += 1

print(count_poi, 'POIs are in the dataset.')

# Q4: How many POI’s were there total from news papaer? -----------------------
with open('../final_project/poi_names.txt','r') as f:
    count_poi_name = 0
    for line in f:
        if line[0] == '(':
            count_poi_name += 1

print(count_poi_name, 'POIs were there total according to media.')

# Q5: What is the total value of the stock belonging to James Prentice?--------
stock_jp = enron_data['PRENTICE JAMES']['total_stock_value']
print('Total stock value for James Prentice is ', stock_jp)

# Q6: How many email messages do we have from Wesley Colwell to persons of interest?
email_to_poi_wc = enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print(email_to_poi_wc, 'emails from Wesley Colwell to persons of interest.')

# Q7: What’s the value of stock options exercised by Jeffrey K Skilling?--------
exercised_stock_options_js = enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print('The value of stock options exercised by Jeffrey K Skilling is',
     exercised_stock_options_js)

# Q8: How many folks in this dataset have a quantified salary? What about a known email address?
count_salary = 0
count_email = 0
for _,value in enron_data.items():
    if value['salary'] != 'NaN':
        count_salary += 1

    if value['email_address'] != 'NaN':
        count_email += 1

print(count_salary, 'persons have a qualified salary,',
      count_email, 'persons have a known email_address.')

# Q9: How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments?
#     What percentage of people in the dataset as a whole is this?--------------------------------
count_missing_finicial = 0
for _, value in enron_data.items():
    if value['total_payments'] == 'NaN':
        count_missing_finicial += 1

print(count_missing_finicial,"persons in the E+F dataset have 'NaN' for their total payments,",
      "{:.2f}%".format(100*count_missing_finicial/len(enron_data)),
      "of people in the dataset is missing total payments.")

# Q10: How many POIs in the E+F dataset have “NaN” for their total payments?
#      What percentage of POI’s as a whole is this?-----------------------------
count_missing_finicial_poi = 0
count_poi = 0
for _, value in enron_data.items():
    if value['poi'] == True:
        count_poi += 1
        if value['total_payments'] == 'NaN':
            count_missing_finicial_poi += 1

print(count_missing_finicial_poi, " POIs in the E+F dataset have 'NaN' for their total payments,",
      "{:.2f}%".format(100*count_missing_finicial_poi/count_poi),
      "of POIs is missing total payments.")


print(enron_data['METTS MARK'])
