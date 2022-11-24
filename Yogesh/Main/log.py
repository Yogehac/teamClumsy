import json
import trial1 as m
import companies as cmp
import paths as pp

import os
import shutil

# isAuthorized = False


def makeLog(logDict):
    with open(pp.mainLog, 'w') as file:
        json.dump(logDict, file, indent=4)
        print('mainLog.json updated')


def getLog():
    with open(pp.mainLog, 'r') as file:
        return json.load(file)


def parseReqLog(id):
    log = getLog()['pending'][id]
    mails = list(log['quotedComp'].keys())

    return [log, mails]


def mailWalk(id):
    reqLog, searchMails = parseReqLog(id)

    # mails recieved from companies list
    gotMail = list()

    for q in searchMails:

        if reqLog['quotedComp'][q]['quote']:

            searchMails.remove(q)

    recM = m.getMail(id, searchMails)
    # print('######', recM)
    if len(recM[-1]) > 0:
        for x in recM[-1]:
            reqLog['quotedComp'][x]['quote'] = True
            reqLog['quotedComp'][x]['MailInfo'] = recM[recM[-1].index(x)]
            gotMail.append(reqLog['quotedComp'][x]['cName'])
        print('Successful Walk')
        # print(reqLog)
        Final = getLog()
        Final['pending'][id] = reqLog

        with open('F:\PROJECTS\Team Project\Main\mainLog.json', 'w') as file:
            json.dump(Final, file, indent=4)
            print('mainLog.json updated')

        return gotMail


def createReq(d, s=False):
    print(d)
    req = {'reqFile': d[0], 'quotedComp': {}, 'resFile': ''}
    l = list(d[1].keys())

    compData = {}
    for x in l:
        if x[-1] == 'e':
            print(x)
            req['quotedComp'][d[1][x]] = {'cName': d[1][x[:-1]+'n'],
                                          'address': d[1][x[:-1]+'a'],
                                          'Mail sent': 'Not sent',
                                          'quote': False}
            compData[d[1][x[:-1]+'n']] = {
                'email': d[1][x],
                'address': d[1][x[:-1]+'a']
            }

    req['Mail Content'] = {
        'subject': d[1]['subject'],
        'body': d[1]['mail-body']
    }

    log = getLog()
    log['pending'][d[1]['reqID']] = req
    makeLog(log)
    cmp.updateData(compData)
    print('success')
    if s:
        m.sendMail(parseReqLog(d[1]['reqID'])[0], d[1]['reqID'])


def mailStatusUpd(id, success):
    d = parseReqLog(id)[0]
    for mailId, t in success.items():
        d['quotedComp'][mailId]['Mail sent'] = t

    log = getLog()
    log['pending'][id] = d
    makeLog(log)
    print('Mail status updated')


def deleteReq(id):
    folder = pp.requestDir + id
    if os.path.exists(folder):
        shutil.rmtree(folder, ignore_errors=True)

    d = getLog()
    d['pending'].pop(id)
    makeLog(d)


# createReq(a)
# mail Log creation
mainLog = {
    'pending': {
        'reqId1': {
            'reqFile': '',
            'quotedComp': {
                'aravindkbarath3@gmail.com': {'cName': 'Barath', 'quote': False},
                "deviyani492@gmail.com": {'cName': 'Devi', 'quote': False}
            },
            'resFile': ''
        },
        'reqId2': {
            'reqFile': '',
            'quotedComp': {
                'email1': {'cName': '', 'quote': False},
                'email2': {'cName': '', 'quote': False}
            },
            'resFile': ''
        }
    },
    'completed': {}
}


# def makeLog(logDict):
#     with open('F:\PROJECTS\Team Project\Main\mainLog.json', 'w') as file:
#         json.dump(logDict, file, indent=4)
#         print('mainLog.json updated')


# makeLog(mainLog)
