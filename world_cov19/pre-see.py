import keras
import numpy as np
import matplotlib.pyplot as plt
import requests
import re
from collections import OrderedDict
url = 'https://coronavirus.1point3acres.com/_next/static/chunks/eb866cddf7095f20f497cfebeab34fbb581cc2fd.e2b6d415563226f3802d.js'
headers = {
    'User-Agent':'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
}
res = requests.get(url,headers = headers)
res.encoding = "UTF-8"
pattern = re.compile('state_name":(.*?),"county":(.*?),"entries":(.*?)}',re.S)
date=re.findall(pattern,res.text)
date_new=date[0][2].replace('[[',',[').replace(']]','],')
re_compile = re.compile('"(.*?)",(.*?)]')
date_care=re.findall(re_compile,date_new)
time=[]
care=[]
for i in range(len(date_care)):
    time.append(date_care[i][0])
    care.append(date_care[i][1])

time_care=OrderedDict(zip(time,care))
y = care
for i in range(len(y)):
    y[i]=int(y[i])
x=np.arange(len(y))

#plt.scatter(x,y)
#plt.show()
model = keras.Sequential()  #顺序模型
from keras import layers
model.add(layers.Dense(1,input_dim=1))
#编译模型
model.compile(optimizer='adam',
             loss='mse'
)
# #训练模型
model.fit(x,y,epochs=50)
plt.scatter(x,y,c='r')
plt.plot(model.predict(x),y)
plt.show()
