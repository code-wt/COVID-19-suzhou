import requests
import json
import re
import pandas as pd
import csv
import os
import numpy as np
url = 'https://covidtracking.com/api/states'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
res = requests.get(url,headers=headers)
a = res.text
pattern=r'state":"(.*?)"'
state = re.findall(pattern, a)
for i in np.arange(len(state)):
    if state[i]=='AK':
        state[i]='Alask'
    if state[i]=='AL':
        state[i]='Alabama'
    if state[i]=='AR':
        state[i]='Arkansas'
    if state[i]=='AZ':
        state[i]='Arizona'
    if state[i]=='CA':
        state[i]='california'
    if state[i]=='CO':
        state[i]='colorado'
    if state[i]=='CT':
        state[i]='Connecticut'
    if state[i]=='DC':
        state[i]='Washington.D.C'
    if state[i]=='DE':
        state[i]='Delaware'
    if state[i]=='FL':
        state[i]='Florida'
    if state[i]=='GA':
        state[i]='Georgia'
    if state[i]=='HI':
        state[i]='Hawaii'
    if state[i]=='IA':
        state[i]='Iowa'
    if state[i]=='ID':
        state[i]='Idaho'
    if state[i]=='IL':
        state[i]='Illinois'
    if state[i]=='IN':
        state[i]='Indiana'
    if state[i]=='KS':
        state[i]='Kansas'
    if state[i]=='KY':
        state[i]='Kentucky'
    if state[i]=='LA':
        state[i]='Louisiana'
    if state[i]=='MA':
        state[i]='Massachusetts'
    if state[i]=='MD':
        state[i]='Maryland'
    if state[i]=='ME':
        state[i]='Maine'
    if state[i]=='MI':
        state[i]='Michigan'
    if state[i]=='MN':
        state[i]='Minnesota'
    if state[i]=='MO':
        state[i]='Missouri'
    if state[i]=='MS':
        state[i]='Mississippi'
    if state[i]=='MT':
        state[i]='Montana'
    if state[i]=='NC':
        state[i]='North Carolina'
    if state[i]=='ND':
        state[i]='North Dakota'
    if state[i]=='NE':
        state[i]='Nebraska'
    if state[i]=='NH':
        state[i]='New Hampshire'
    if state[i]=='NJ':
        state[i]='New Jersey'
    if state[i]=='NM':
        state[i]='New Mexico'
    if state[i]=='NV':
        state[i]='Nevada'
    if state[i]=='NY':
        state[i]='New York'
    if state[i]=='OH':
        state[i]='Ohio'
    if state[i]=='OK':
        state[i]='Oklahoma'
    if state[i]=='OR':
        state[i]='Oregon'
    if state[i]=='PA':
        state[i]='Pennsylvania'
    if state[i]=='RI':
        state[i]='Rhode Island'
    if state[i]=='SC':
        state[i]='South Carolina'
    if state[i]=='SD':
        state[i]='South Dakota'
    if state[i]=='TN':
        state[i]='Tennessee'
    if state[i]=='TX':
        state[i]='Texas'
    if state[i]=='UT':
        state[i]='Utah'
    if state[i]=='VA':
        state[i]='Virginia'
    if state[i]=='VT':
        state[i]='Vermont'
    if state[i]=='WA':
        state[i]='Washington'
    if state[i]=='WI':
        state[i]='Wisconsin'
    if state[i]=='WV':
        state[i]='West Virginia'
    if state[i]=='WY':
        state[i]='Wyoming'
    if state[i]=='PR':
        state[i]='Puerto Rico'
    if state[i]=='AS':
        state[i]='AS'
    if state[i]=='GU':
        state[i]='Guam'
    if state[i]=='MP':
        state[i]='Northern Mariana Islands'
    if state[i]=='VI':
        state[i]='US Virgin Islands'







pattern=r'positive":(.*?),'
positive=re.findall(pattern,a)
pattern=r'positiveScore":(.*?),'
positiveScore=re.findall(pattern,a)
pattern=r'negativeScore":(.*?),'
negativeScore=re.findall(pattern,a)
pattern=r'negativeRegularScore":(.*?),'
negativeRegularScore=re.findall(pattern,a)
pattern=r'commercialScore":(.*?),'
commercialScore=re.findall(pattern,a)
pattern=r'grade":(.*?),'
grade=re.findall(pattern,a)
pattern=r'score":(.*?),'
score=re.findall(pattern,a)
pattern=r'"negative":(.*?),'
negative=re.findall(pattern,a)
pattern=r'pending":(.*?),'
pending=re.findall(pattern,a)
pattern=r'"hospitalizedCurrently":(.*?),'
hospitalizedCurrently=re.findall(pattern,a)
pattern=r'"hospitalizedCumulative":(.*?),'
hospitalizedCumulative=re.findall(pattern,a)
pattern=r'inIcuCurrently":(.*?),'
inIcuCurrently=re.findall(pattern,a)
pattern=r'inIcuCumulative":(.*?),'
inIcuCumulative=re.findall(pattern,a)
pattern=r'onVentilatorCurrently":(.*?),'
onVentilatorCurrently=re.findall(pattern,a)
pattern=r'onVentilatorCumulative":(.*?),'
onVentilatorCumulative=re.findall(pattern,a)
pattern=r'recovered":(.*?),'
recovered=re.findall(pattern,a)
pattern=r'lastUpdateEt":(.*?),'
lastUpdateEt=re.findall(pattern,a)
pattern=r'checkTimeEt":(.*?),'
checkTimeEt=re.findall(pattern,a)
pattern=r'death":(.*?),'
death=re.findall(pattern,a)
pattern=r'hospitalized":(.*?),'
hospitalized=re.findall(pattern,a)
pattern=r'total":(.*?),'
total=re.findall(pattern,a)
pattern=r'totalTestResults":(.*?),'
totalTestResults=re.findall(pattern,a)
pattern=r'posNeg":(.*?),'
posNeg=re.findall(pattern,a)
pattern=r'fips":(.*?),'
fips=re.findall(pattern,a)
pattern=r'dateModified":(.*?),'
dateModified=re.findall(pattern,a)
pattern=r'dateChecked":(.*?),'
dateChecked=re.findall(pattern,a)
with open('data.csv','w',newline='')as f:
    csv_write=csv.writer(f,dialect='excel')
    csv_write.writerow(['state','positive','negative','pending','hospitalizedCurrently','hospitalizedCumulative','inIcuCurrently','inIcuCumulative','onVentilatorCurrently','onVentilatorCumulative','recovered','lastUpdateEt','checkTimeEt','death','hospitalized','total','totalTestResults','posNeg','fips','dateModified','dateChecked'])
    try:
        for i in np.arange(len(state)):
            csv_write.writerow([state[i],positive[i],negative[i],pending[i],hospitalizedCurrently[i],hospitalizedCumulative[i],inIcuCurrently[i],inIcuCumulative[i],onVentilatorCurrently[i],onVentilatorCumulative[i],recovered[i],lastUpdateEt[i],checkTimeEt[i],death[i],hospitalized[i],total[i],totalTestResults[i],posNeg[i],fips[i],dateModified[i],dateChecked[i]])
    except:
        pass        
