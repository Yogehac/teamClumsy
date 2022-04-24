import imaplib
import email
import json
import pypdfium2 as pdfium


# C:\Users\Yogesh\PycharmProjects\EmailTrial\Trail\Converted
def convertCsv(src, file):
    # table_file = r"C:\Users\Yogesh\PycharmProjects\EmailTrial\Trail\MailAttachments\QUOTATION NO.330.pdf"
    # output_csv = r"C:\Users\Yogesh\PycharmProjects\EmailTrial\Trail\MailAttachments\QUOTATION NO.330.csv"
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



def getMail():
    host = 'imap.gmail.com'
    username = 'teamclumsy.dev@gmail.com'
    pword = 'dev.CLUMSYteam'

    AllMails = []

    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, pword)

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
        # else:
        #     for part in msg.walk():
        #         if part.get_content_type() == 'text/plain':
        #             data = part.get_payload(decode=True)
        #             texts += data.decode()
        #         elif part.get_content_type() == 'text/html':
        #             continue
        print()
        mailInfo['body'] = texts
        AllMails.append(mailInfo)
    mail.close()
    return AllMails


# C:\Users\Yogesh\PycharmProjects\EmailTrial\Trail\MailAttachments
def dbMail():
    try:
        with open('MailsInfo.json', 'w') as file:
            json.dump(getMail(), file, indent=3)
        print('Updated JSON file')
    except Exception as e:
        print('Error', e)


def getDbMail():
    with open('MailsInfo.json', 'r') as file:
        db = json.load(file)
    return db

# convertCsv(r"C:\Users\Yogesh\PycharmProjects\EmailTrial\Trail\MailAttachments\QUOTATION NO.330.pdf",
#            'QUOTATION NO.330.csv')

# for x in getDbMail():
#     print(x)

if __name__ == '__main__':
    dbMail()

# with open(r'C:\Users\Yogesh\PycharmProjects\EmailTrial\Trail\MailAttachments\hello.csv', 'w') as file:
#     file.write('hello woeld1!')
#     print('file created')
