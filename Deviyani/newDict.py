import json
with open ('Project - 01\Emptyquotform1.csv','r')as file:
    li = []
    for line in file.readlines():
        li.append(line.split(',')[:5])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
reqD = {}

def createD(d):
    a = dict(zip(li[0],d))
    return a

for i in li[1:] :
    if i[4] in reqD:
        reqD[i[4]].append(createD(i))
    elif i[4] != '':
        reqD[i[4]] = [createD(i)]
        
with open('req.json','w') as file:
    json.dump(reqD,file,indent=3)
    print('json created')
