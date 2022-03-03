import csv
import datetime
import os
import json
import random
import pandas as pd

now = datetime.datetime.now()
today = now.date()
stringToday = today.strftime("%d/%m/%Y")

def send_email(customers, email_template, error_file): 
  with open(email_template, 'r') as f:
    email_template = json.load(f)
    with open(customers, 'r') as file:
      reader = csv.reader(file)
      next(reader)
      check = pd.read_csv(customers)
      if check.empty: 
        raise Exception("No customers found")
      else:
        for row in reader:
          if not row[3]:
            print(row[0] + row[1] + row[2] + "No email found")
            with open(error_file, 'a+', newline='') as error:
              writer = csv.writer(error, dialect='excel')
              writer.writerow([row[0], row[1], row[2]])
              error.close()
          else: 
            email_template['to'] = row[3]
            newBody = json.dumps(email_template['body'])
            email_template['body'] = newBody.format(TITLE=row[0],FIRST_NAME=row[1],LAST_NAME=row[2],TODAY=stringToday)
            sentDir = 'sentEmails'
            file = row[1] + row[2] + str(random.randint(1111,9999)) + '.json'
            messageStr = json.dumps(email_template)
            with open (os.path.join(sentDir, file), 'w') as f:
              f.write(messageStr)
              print("Message sent to: " + row[3])
              f.close()
if __name__ == '__main__':
  send_email('customers.csv', 'email_template.json', 'error.csv')