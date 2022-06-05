import imaplib
import email
import json
import pypdfium2 as pdfium


def login():
    host = 'imap.gmail.com'
    username = 'teamclumsy.dev@gmail.com'
    pword = 'dev.CLUMSYteam'

    try:
        mail = imaplib.IMAP4_SSL(host)
        mail.login(username, pword)
        return mail
    except Exception as e:
        return False


# pdf to Image conversion function
def convertCsv(src, file):
    if file[-3:] == 'pdf':
        try:
            dst = 'Converted/' + file[:-4] + '/'
            print(dst)
            for image, suffix in pdfium.render_pdf_topil(src):
                dst = 'Converted/' + file[:-4] + '_%s.jpg' % suffix
                with open(dst, 'w'):
                    image.save(dst)
                    print(dst)

        except Exception as e:
            print('error', e)
    else:
        print('not pdf format')


# To get mail from the specified email
def getMail():
    mail = login()
    if mail:
        AllMails = []

        # To view list of mailboxes in the mail
        # _, directories = mail.list()
        # for x in directories:
        #     print(x.decode())

        mail.select('inbox')
        _, mails = mail.search(None, 'ALL')

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
                        pathA = r'C:\Users\Yogesh\PycharmProjects\EmailTrial\Trail\MailAttachments\{}'.format(
                            part.get_filename())
                        try:
                            with open(pathA, 'wb') as file1:
                                file1.write(part.get_payload(decode=True))
                                print('file created')
                                convertCsv(pathA, part.get_filename())
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
        mail.close()
        return AllMails


# To store the mail information from Py-dictionary to JSON
def dbMail():
    try:
        with open('MailsInfo.json', 'w') as file:
            json.dump(getMail(), file, indent=3)
        print('Updated JSON file')
    except Exception as e:
        print('Error', e)


# To retrieve the JSON file to Py-dictionary
def getDbMail():
    with open('MailsInfo.json', 'r') as file:
        db = json.load(file)
    return db


# Driver code
# if __name__ == '__main__':
#     dbMail()


def parseHim():
    mail = login()
    if mail:
        mail.select('inbox')
        # To view list of mailboxes in the mail
        # _, directories = mail.list()
        # for x in directories:
        #     print(x.decode())

        # to search for particular mail
        # _, mails = mail.search(None, '(FROM "aravindkbarath3@gmail.com")')
        # print(mails[0].decode().split())

        # to create sub directories in mail
        # mail.select('testing', readonly=False)
        # print(mail.create('testing/first'))
        # print(mail.expunge())

        # To copy from inbox to testing/first -- not rectified
        # _, mails = mail.search(None, '(FROM "aravindkbarath3@gmail.com")')
        # mailIds = ':'.join(mails[0].decode().split())
        # print(mailIds)
        #
        # # print(mail.copy(mailIds, 'testing/first'))
        # for id in mailIds:
        #     print(mail.copy(id, 'testing/first'))

        # To search multiple mails
        gmail = ['aravindkbarath3@gmail.com', 'no-reply@accounts.google.com']
        for x in gmail:
            _, mails = mail.search(None, f'(FROM "{x}")')
            print(x, len(mails[0].decode().split()))

        mail.close()
    else:
        print('Auth error')


# parseHim()

# parseHim()
