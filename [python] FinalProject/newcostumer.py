import pandas as pd
import gc
import numpy as np
gc.collect()

data=pd.read_csv("NTU_1317_Member.txt",delimiter="\t",low_memory=False)
data['MinOrderDate']=pd.to_datetime(data['MinOrderDate']) 
time_expend=["2017-1~2017-2","2017-2~2017-3","2017-3~2017-4","2017-4~2017-5","2017-5~2017-6","2017-6~2017-7","2017-7~2017-8","2017-8~2017-9","2017-9~2017-10","2017-10~2017-11","2017-11~2017-12","2017-12~2018-1"]
# newCustomer_dic={}
N=[]
N_member=[]
C=[]
C_member=[]
for ele in time_expend:
    time=ele.split("~")
    # print(time)
    customer_data=data[data['MinOrderDate']<=time[1]]
    # newCustomer_dic[ele]=customer_data
    C_member.append(set(customer_data['MemberId']))
    temp=customer_data.count()
    customer=temp["MemberId"]
    C.append(customer)
    newCustomer_data=customer_data[customer_data['MinOrderDate']>=time[0]]
    temp=newCustomer_data.count()
    newCustomer=temp["MemberId"]
    N_member.append(set(newCustomer_data['MemberId']))
    N.append(newCustomer)
