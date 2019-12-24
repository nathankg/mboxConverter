import mailbox
import csv
import sys
from collections import defaultdict

mboxFile = 'Takeout/Mail/Inbox.mbox'
csvFile = "mbox-output.csv"
writer = csv.writer(open(csvFile, "w"))
senderCount = defaultdict(lambda: 0)
totalEmailCount = len(mailbox.mbox(mboxFile))

for ind, message in enumerate(mailbox.mbox(mboxFile)):
    # message = message.decode('utf8')
    try:
        writer.writerow([message['message-id'], message['subject'], message['from'], message['date']])
        senderCount[message['from']] += 1
        if ind % 100 == 0: 
            print ("Completed {} of {}".format(ind, totalEmailCount))
    except:
        print("====== {} ======".format(ind))
        print(message)
        print("================")
        print("Unexpected Error: ", sys.exc_info()[0])
        raise

print("Completed Creation of CSV: {}".format())