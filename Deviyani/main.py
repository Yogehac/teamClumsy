# x = 'D:\VS_CODE\KOTHARI\response\swajit.xlsx'
from matplotlib.font_manager import json_load
import pandas as pd
import json


def makeLog(logDict):
    with open('res.json', 'w') as file:
        json.dump(logDict, file, indent=4)
    print('Done')


def extract_num(line):
    num = []
    temp = ''
   
    for x in line:
        
        if x.isdigit():
           temp += x
        elif len(temp) > 0:
            num.append(int(temp))
            temp = ''
    if len(temp) > 0:
        num.append(int(temp))
    return num

def validate(nums):
    if len(nums) == 4:
        if 0 in nums:
            nums.pop(nums.index(0))
        a, b, c = nums
    elif len(nums) == 3:
        a, b, c = nums
    elif len(nums) == 2:
        a, b = nums
        return [b,a*b]
    if a * b == c:
        return [b,c]
    elif a * c == b:
        return [c,b]
    else:
        return "NaN" ,nums



def makeResponse(res,quotes):
    with open(res,'r')as F:
        A = json.load(F)
    for k in A :
        for i in quotes.keys():
            if i[-3:] != "csv":       
                x = pd.read_excel(i)
                x.to_csv('{}.csv'.format(i),index=None,header=True)
                with open('{}.csv'.format(i),'r') as file:
                    y = file.readlines()
            else:
                with open(i,'r') as file:
                    y = file.readlines()
            a,b = list(k.values())[:2]
            for j in y:
                if a in j and b in j:
                    k[quotes[i]]=validate( extract_num(j[j.index(b) + len(b):]))[0]
    makeLog(A)       
                    # print( validate(extract_num(j[j.index(b) + len(b):])))

makeResponse('requuhh.json',{
    r'response\swajit.xlsx':'swajit',
    r'response\rajamar.xlsx':'rajmar',
    r'response\sathish.xlsx':'sathish',
    r'response\gee_ess.xlsx':'gee_ess'
    })



    