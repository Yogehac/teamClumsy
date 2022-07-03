import imaplib
import email
import json

def getCred(m, c = 0):
    if m == 'r':
        with open('F:\PROJECTS\Team Project\Main\cred.bin', 'rb') as file:
            y = file.readline()
            return [len(y) != 0, *y.split(',')]
    else:
        with open('F:\PROJECTS\Team Project\Main\cred.bin', 'wb') as file:
            file.write(c.encode('ascii'))

            


def login(user = 0, code = 0):
    host = 'imap.gmail.com'
    mail = imaplib.IMAP4_SSL(host)
    try:
        if user == 0:
            c = getCred('r')
            if c[0]:
                mail.login(c[1], c[2])
                return mail
        else:
            getCred('w', '{},{}'.format(user, code))
            mail.login(user, code)
            return mail
    except Exception:
        return False

# a = login() 
# print('sucess' if a else 'Failed')


# To get mail from the specified email
def getMail(id, searchMails):
    mail = login()
    if mail:
        AllMails = []
        signals = []
        mail.select('inbox')
        gmail = searchMails
        for a in gmail:
            # print(a)
            _, mails = mail.search(None, f'(FROM "{a}" SUBJECT "{id}")')
            if len(mails[0].decode().split()) > 0:
                for x in mails[0].decode().split():
                    mailInfo = {}
                    _, data = mail.fetch(x, 'RFC822')
                    msg = email.message_from_bytes(data[0][1])

                    for val in ['from', 'to', 'subject', 'date']:
                        mailInfo[val] = msg[val]
                    mailInfo['Attachments'] = []
                    texts = ''

                    if msg.is_multipart():
                        for part in msg.walk():
                            # print(part.get('Content-Disposition'))
                            if part.get("Content-Disposition"):
                                print(part.get_filename())
                                # F:\PROJECTS\Team Project\Main\MailAttachments
                                pathA = r'F:\PROJECTS\Team Project\Main\MailAttachments\{}'.format(part.get_filename())
                                try:
                                    with open(pathA, 'wb') as file1:
                                        file1.write(part.get_payload(decode=True))
                                        print('file created')
                                       
                                    mailInfo['Attachments'].append(pathA)
                                except Exception as e:
                                    print('Error in downloading Attachments', e)

                            if part.get_content_type() == 'text/plain':
                                data = part.get_payload(decode=True)
                                texts += data.decode()
                            elif part.get_content_type() == 'text/html':
                                continue
                    print()
                    mailInfo['body'] = texts
                    AllMails.append(mailInfo)
                    signals.append(a)
            else:
                print('no mail from {}'.format(a))
        mail.close()
        AllMails.append(signals)
        return AllMails




def parseHim():
    mail = login()
    if mail:
        mail.select('inbox')

        # To search multiple mails
        gmail = ['aravindkbarath3@gmail.com', 'no-reply@accounts.google.com', 'google-noreply@google.com']
        for x in gmail:
            _, mails = mail.search(None, f'(FROM "{x}")')
            print(x, len(mails[0].decode().split()))

        mail.close()
    else:
        print('Auth error')



