# Python_email_imbox
Email_process
## testing with specific folder and file format final done

import os
from imbox import Imbox # pip install imbox
import traceback
from datetime import date



userid = 'xyz.mail.com'
passw = 'password11'
smtp2 = 'host.mail.com'
download_folder = 'D:/EDW'



mail = Imbox(smtp2, username=userid, password=passw, ssl=True, ssl_context=None, starttls=False)
print(date.today())
status, folders_with_additional_info = mail.folders()
#print(folders_with_additional_info )

all_inbox_messages = mail.messages( sent_from='noreply@mai.com', folder ='"INBOX/Sigma alert"')
#messages = mail.messages(subject='edw_zip', sent_from='xyz.mial.com', unread=True, date__on=date.today(), folder ='"INBOX/Sigma alert"') 
# defaults to inbox


for uid, message in all_inbox_messages:
    mail.mark_seen(uid) # optional, mark message as read
#     print(message.sent_from)
#     print(message.sent_to)
#     print(message.subject)
#     print(message.headers)
#     print(message.message_id)
#     print(message.date)

#     print(message.attachments)

    for idx, attachment in enumerate(message.attachments):
        try:
            att_fn = attachment.get('filename')
            if '.7z' in att_fn.lower():
                download_path = f"{download_folder}/{att_fn}"
                print(download_path)
                with open(download_path, "wb") as fp:
                    fp.write(attachment.get('content').read())
        except:
            print('Downloaded File name : ',traceback.print_exc())

mail.logout()
print('we are out! ')
## this is final
