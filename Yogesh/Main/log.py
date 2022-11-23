import json
import trial1 as m
import paths as pp


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


# id = 'reqId1'
# print(r'{}'.format(list(parseReqLog(id)[0]['quotedComp'].values())[0]['MailInfo']['Attachments'][0]))

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


# a = {'reqID': '1', 'c1n': 'devi', 'c1e': 'd@gamil.com'}

def createReq(d):
    req = {'reqFile': d[0], 'quotedComp': {}, 'resFile': ''}
    l = list(d[1].keys())
    for x in l:
        if x[-1] == 'e':
            print(x)
            req['quotedComp'][d[1][x]] = {'cName': d[1][x[:-1]+'n'],
                                          'quote': False}
    log = getLog()
    log['pending'][d[1]['reqID']] = req
    makeLog(log)
    print('success')


def deleteReq(id):
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
