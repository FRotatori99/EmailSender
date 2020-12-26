from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pandas
from string import Template

MY_ADDRESS = 'admin@example.com'
MY_PASSWORD = 'password'

def load_template(templateName):
    with open('Emails/' + templateName + '.html', 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def read_list_pandas(filename):
    df = pandas.read_csv(filename + '.csv', delimiter=',')
    return df

def connect_SMTP():
    server = smtplib.SMTP(host='yourDomain.com', port=587)
    server.starttls()
    server.login(MY_ADDRESS, MY_PASSWORD)
    return server

def send_msg(server, email, name, message_template):
    msg = MIMEMultipart()
    message = message_template.substitute(PERSON_NAME=name)
    msg['From'] = 'Alias <' + MY_ADDRESS + '>'
    msg['To'] = email
    msg['Subject'] = 'Test Email'
    msg.attach(MIMEText(message, 'html'))
    server.send_message(msg)
    del msg

filename = 'list'
df = read_list_pandas(filename)
server = connect_SMTP()
template = load_template('mail1')
for index, row in df.iterrows():
    print(f'Sending email to: {row["Email Address"]} - {row["First Name"]}')
    send_msg(server, row['Email Address'], row['First Name'], template)
