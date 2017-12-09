'''
Created on Nov 28, 2017

@author: Victoria Hobbs


'''

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def genderEnum (strobject):
    objStr = str(strobject)
    if (objStr == 'F') or (objStr == 'f') or ("Female" in objStr) or ("female" in objStr):
        return 0 #F
    elif (objStr == 'M') or (objStr == 'm') or ("Man" in objStr) or ("Guy" in objStr) or ("Male" in objStr) or (" male" in objStr) or ("male" in objStr) or ("guy" in objStr):
        return 1 #M
    else:
        return 2 #N
    
def processColumn(colName, func):
    copyList = techhealth[colName].tolist()
    replaceList = []
    for entry in copyList:
        replaceList.append(func(entry))
    return pd.Series(replaceList)

#could delete and use inline
    
FILENAME = "survey.csv"

techhealth_orig = pd.read_csv(FILENAME)
techhealth = techhealth_orig.copy()
#print(techhealth.sample (n=5))

#print(techhealth.dtypes)

techhealth['Gender'] = processColumn('Gender', genderEnum)
commentList = []
for entries in techhealth['comments']:
    if pd.isnull(entries):
        commentList.append(0)
    else:
        commentList.append(1)
techhealth = techhealth.assign(has_comment=pd.Series(commentList))

techhealth = techhealth[techhealth['Age'] < 100]
techhealth = techhealth[techhealth['Age'] > 17]
  
techhealth['Timestamp'] = pd.to_datetime(techhealth['Timestamp'])

techhealth['work_interfere']=techhealth['work_interfere'].map({'Never':1, 'Rarely':2, 'Sometimes':3, 'Often':4})
techhealth['work_interfere'].fillna(0, inplace=True)

techhealth['family_history']=techhealth['family_history'].map({'Yes':2,'No':1})
techhealth['treatment']=techhealth['treatment'].map({'Yes':2,'No':1})
techhealth['remote_work']=techhealth['remote_work'].map({'Yes':2,'No':1})
techhealth['tech_company']=techhealth['tech_company'].map({'Yes':2, 'No':1})
techhealth['obs_consequence']=techhealth['obs_consequence'].map({'Yes':2, 'No':1})

techhealth['self_employed']=techhealth['self_employed'].map({'Yes':2, 'No':1})
techhealth['self_employed'].fillna(0, inplace=True)

techhealth['no_employees']=techhealth['no_employees'].map({'1-5':1, '6-25':2, '26-100':3, '100-500':4, '500-1000':5, 'More than 1000':6})
techhealth['benefits']=techhealth['benefits'].map({'Yes':2, 'No':1, "Don't know":3})
techhealth['care_options']=techhealth['care_options'].map({'Not sure':3, 'Yes':2, 'No':1})
techhealth['wellness_program']=techhealth['wellness_program'].map({'Don\'t know':3, 'Yes':2, 'No':1})
techhealth['seek_help']=techhealth['seek_help'].map({'Yes':2, 'No':1, 'Don\'t know':3})
techhealth['anonymity']=techhealth['anonymity'].map({'Yes':2, 'No':1, 'Don\'t know':3})#techhealth['']
techhealth['leave']=techhealth['leave'].map({'Don\'t know':5, 'Very easy':1, 'Somewhat easy':2, 'Somewhat difficult':3, 'Very difficult':4})
techhealth['mental_health_consequence']=techhealth['mental_health_consequence'].map({'Yes':2,'No':1,'Maybe':3})
techhealth['phys_health_consequence']=techhealth['phys_health_consequence'].map({'Yes':2,'No':1,'Maybe':3})
techhealth['coworkers']=techhealth['coworkers'].map({'Yes':2, 'No':1, 'Some of them':3})
techhealth['supervisor']=techhealth['supervisor'].map({'Yes':2,'No':1,'Some of them':3})
techhealth['mental_health_interview']=techhealth['mental_health_interview'].map({'Yes':2,'No':1,'Maybe':3})
techhealth['phys_health_interview']=techhealth['phys_health_interview'].map({'Yes':2,'No':1,'Maybe':3})
techhealth['mental_vs_physical']=techhealth['mental_vs_physical'].map({'Yes':2,'No':1,'Don\'t know':3})

#I want to make a new column that contains 0 if no comment, 1 if comment

#print("comments counts: \n" , techhealth['comments'].value_counts(sort=False, dropna=False))



#print("has_comment counts:\n", techhealth['has_comment'].value_counts(sort=False,dropna=False))



#techhealth['comments'] = pd.Series(commentList)

#print(techhealth.describe())
#print(techhealth['Gender'].count)
#print("Gender counts:")
#print(techhealth["Gender"].value_counts())
#print("treatment counts:")
#print(techhealth["treatment"].value_counts())

techhealth.to_csv('mental_health_out.csv')

#techhealth['Gender'].hist(bins=3)
#plt.show()
