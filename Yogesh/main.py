import json
import trial1 as m

m.login()


def getLog():
    with open('mainLog.json', 'r') as file:
        return json.load(file)


def parseReqLog(id):
    log = getLog()['pending'][id]
    mails = list(log['quotedComp'].keys())

    return [log, mails]


# print(parseReqLog('reqId1')[0]['quotedComp']['aravindkbarath3@gmail.com'])

id = 'reqId1'
searchMails = parseReqLog(id)[1]


# Request LOG dict
reqLog = parseReqLog(id)[0]

recM = m.getMail(id, searchMails)

print(recM)
if len(recM[-1]) > 0:
    for x in recM[-1]:
        # print(x)
        reqLog['quotedComp'][x]['quote'] = True
        reqLog['quotedComp'][x]['MailInfo'] = recM[recM[-1].index(x)]
    print('Successful Walk')
    print(reqLog)
    Final = getLog()
    Final['pending'][id] = reqLog

    with open('mainLog.json', 'w') as file:
        json.dump(Final, file, indent=4)
        print('mainLog.json updated')



# # To store the mail information from Py-dictionary to JSON
# def dbMail():
#     try:
#         with open('MailsInfo.json', 'w') as file:
#             json.dump(receivedMails, file, indent=3)
#         print('Updated JSON file')
#     except Exception as e:
#         print('Error', e)
