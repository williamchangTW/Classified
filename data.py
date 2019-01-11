import random
import numpy as np
data_set=[]
for i in range(10000):
    x=[]
    x.append(random.randint(0,1))
    x.append(random.randint(0,1))
    x.append(random.randint(30,300))
    x.append(random.randint(0,1))
    data_set.append(x)
lable=[]
for d in data_set:
    if d[0]==0:
        if d[1]==1:
            lable.append(1)
        else:
            lable.append(-1)
    else:
        if d[2]>=100:
            if d[3]==1:
                lable.append(1)
            else:
                lable.append(-1)
        else:
            lable.append(1)
data_train=data_set[0:8000]
data_test=data_set[8001:]
lable_train=lable[0:8000]
lable_test=lable[8001:]
np.save("Data\data_train",np.asarray(data_train))
np.save("Data\data_test",np.asarray(data_test))
np.save("Data\lable_train",np.asarray(lable_train))
np.save("Data\lable_test",np.asarray(lable_test))
