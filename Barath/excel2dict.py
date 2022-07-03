import json
import os
import pandas as pd
import pathlib

def loadmain():
    with open(r"C:\Users\bhara\PycharmProjects\KothariSugars\teamClumsy-main\Yogesh\mainLog.json","r") as mainlog:
        mainjso = json.load(mainlog)
        return mainjso

def getreq(id):
    d = loadmain()
    return d["pending"][id]

def makeLog(logDict):
    with open('res.json', 'w') as file:
        json.dump(logDict, file, indent=4)
    print('Done')

def getLog(somejson):
    with open(somejson, 'r') as file:
        requestdict = json.load(file)
    return requestdict
    print('Done')




def reqfileextract(reqfile):
    with open(reqfile, 'r') as file:
        li = []
        for line in file.readlines():
            li.append(line.split(',')[:5])
            # print(line.split(',')[:5])
    # print(li)
    return li
reqD = {}


# print(reqD)

def createD(d,l):
    a = dict(zip(l, d))
    return a

def listcreation(li):
    superlist = []
    devi = 0
    for i in li[1:]:
        if i[4] != '':
            superlist.append(createD(i,li[0]))
            devi = li.index(i)
            li.remove(i)
    # print(li)
    joker = []
    for j in li[devi:]:

        for d in j:
            if d != "":
                joker.append(d)


    deva = list(" "*len(joker))
    superlist.append(createD(deva,joker))
    return superlist



    # with open('summaddaa.json', 'w') as file:
    #     json.dump(superlist, file, indent=3)
    #     print('json created')

# for i in li[1:]:
#     if i[4] in reqD:
#         reqD[i[4]].append(createD(i))
#     elif i[4] != '':
#         reqD[i[4]] = [createD(i)]


# for i in reqD:
#     for x in reqD[i]:
#         reqUpd[x['Drawing No.']] = x
# print(reqUpd)
#
# with open("reqqquuuh.json", 'w') as file:
#     json.dump(, file, indent=3)
#     print('json created')

# listcreation(reqfileextract("Emptyquotcsv.csv"))



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
    # print(nums)
    if len(nums) == 4:
        if 0 in nums:
            nums.pop(nums.index(0))
        a, b, c = nums
    elif len(nums) == 3:
        a, b, c = nums
    elif len(nums) == 2:
        a, b = nums
        return [b, a * b]
    if a * b == c:
        return [b, c]
    elif a * c == b:
        return [c, b]
    else:
        return "NaN", nums


# def makeResponse(res, quotes):
#     A = getLog(res)
#     print("makeResponse")
#     # print(quotes)
#     for k in A[:-1]:
#         print(k)
#         for i in quotes.keys():
#             print('Im in')
#             if i[-3:] != "csv":
#                 x = pd.read_excel(r'{}'.format(i))
#                 x.to_csv('{}.csv'.format(i), index=None, header=True)
#                 with open('{}.csv'.format(i), 'r') as file:
#                     y = file.readlines()
#             else:
#                 with open(i, 'r') as file:
#                     y = file.readlines()
#             # print(y)
#             a, b = list(k.values())[:2]
#             for j in y[1:]:
#                 if a in j and b in j:
#                     # print(a, b)
#                     # print(j)
#                     k[quotes[i]] = validate(extract_num(j[j.index(b) + len(b):]))[0]
#                     print('\n',k)
#             # print(k)
#     return A


# makeResponse('summaddaa.json',
respopaths = {
    r'C:\Users\bhara\PycharmProjects\KothariSugars\teamproject1\properresponse\proper_swajit.csv' : 'swajit',
    r'C:\Users\bhara\PycharmProjects\KothariSugars\teamproject1\properresponse\proper_rajamar.xlsx':'rajmar',
    r'C:\Users\bhara\PycharmProjects\KothariSugars\teamproject1\properresponse\proper_sathish.xlsx':'sathish',
    r'C:\Users\bhara\PycharmProjects\KothariSugars\teamproject1\properresponse\proper_gee_ess.xlsx':'gee_ess'
    }

def writeLine(dic, t, u=0):
    temp = ''
    if t == 'k':
        d = list(dic.keys())
    else:
        d = list(dic.values())
    for i in d:
        if d.index(i) > 4:
            if t == 'k':
                temp += str(i) + ',,'
            else:
                temp += str(i) + ',{},'.format(i * int(dic['Qty']))
        else:
            temp += str(i) + ','
    if t == 'k':
        temp += '\n'
        for i in d:
            if d.index(i) > 4:
                temp += 'Rate,Amount,'
            else:
                temp += ','
        temp += '\n'
    # if u != devi:
    #     temp += '\n{}\n'.format(u)
    #     devi = u
    # else:
    #     temp+='\n'
    temp += '\n'
    return temp


def makeFinal(jsonfile, FF):
    x = jsonfile
    # print(x)
    with open(FF, 'w') as F:
        F.write(writeLine(x[0], 'k'))
        for i in x:
            F.write(writeLine(i, 'v'))

        print('Done')


# makeFinal(r'D:\VS_CODE\KOTHARI\res.json', 'final.csv')

def clientDict(id):
    rid = getreq(id)
    d ={}
    for i,j in rid["quotedComp"].items():
        # print(i,j)
        if j["quote"] :
            # print('came')
            d[j["MailInfo"]["Attachments"][0]] = j['cName']
    return d
# clientDict('reqId1')



def excel_to_csv(filename):
    read_file = pd.read_excel(filename)

    read_file.to_csv(os.path.splitext(filename)[0] + '.csv',
                     index=None,
                     header=True)

    df = pd.DataFrame(pd.read_csv(os.path.splitext(filename)[0] + '.csv'))


def getCSV(filename):
    filename = pathlib.PureWindowsPath(filename).as_posix()
    if os.path.splitext(filename)[1] == ".csv":
        with open(filename, 'r') as file:
            return file.readlines()
    else:
        excel_to_csv(filename)
        with open(os.path.splitext(filename)[0] + '.csv', 'r') as file:
            return file.readlines()

def makeResponse(reqjson,quotationfiles):
    # reqjsoncontent = getLog(reqjson)
    for i in quotationfiles.keys():
        resplist = getCSV(i)
        for j in resplist[1:]:
            for k in reqjson[:-1]:
                desc,draw = list(k.values())[:2]
                if desc in j and draw in j:
                    k[quotationfiles[i]] = validate(extract_num(j[j.index(draw) + len(draw):]))[0]
                    resplist.remove(j)
    return reqjson
        # print(resplist)
# makeResonse("summaddaa.json",respopaths)

def createReport(id):
    rid = getreq(id)
    print(rid,'\n')
    req = reqfileextract(rid["reqFile"])
    print(req, '\n')
    reqd = listcreation(req)
    print(reqd, '\n')
    final = makeResponse(reqd,clientDict(id))
    print(final, '\n')
    makeFinal(final,"{}.csv".format(id))
    rid["resFile"] = "{}.csv".format(id)
    d = loadmain()
    d["pending"][id] = rid
    makeLog(d)

createReport('reqId1')