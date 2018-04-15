import pandas as pd
from newcostumer import C,time_expend,C_member,N_member,N

data=pd.read_csv("Ntu_Orders.csv",low_memory=False,dtype=str)
data["DateId"]=pd.to_datetime(data["DateId"],format="%Y%m%d")
# member_dic={}
E_member=[]
E=[]
S=[]
S_member=[]
sleep=[]
nap=[]
sleep_member=[]
nap_member=[]
for index,ele in enumerate(time_expend):
    time=ele.split("~")
    temp=data[data["DateId"]>time[0]]
    data_i=temp[temp["DateId"]<time[1]]
    # member_dic[ele]=data_i
    data_member=data_i.groupby("MemberId")["DateId"].nunique()
    E_member.append(set(data_member))
    E.append(len(data_member))
    if S_member==[]:
        temp=C_member[index]-E_member[index]-N_member[index]
        S_member.append(temp)
        S.append(len(list(temp)))
        sleep_member.append({0})
        sleep.append(0) 
        nap_member.append(temp)
        nap.append(len(list(temp)))
    else:
        temp=C_member[index]-E_member[index]-N_member[index]
        S_member.append(temp)
        S.append(len(list(temp)))
        temp2=temp & S_member[index-1]
        sleep_member.append(temp2)
        sleep.append(len(list(temp2)))
        temp2=temp-(temp & S_member[index-1])
        nap_member.append(temp2)
        nap.append(len(list(temp2)))
