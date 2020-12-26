from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pandas
from string import Template

MY_ADDRESS = 'admin@ketodiets360.com'

def load_template(templateName):
    with open('Emails/' + templateName + '.html', 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def read_list_pandas(filename):
    df = pandas.read_csv(filename + '.csv', delimiter=',')
    return df

# set up the SMTP server
def connect_SMTP():
    server = smtplib.SMTP(host='ketodiets360.com', port=587)#SSL - 465, NO SSL - 587
    #server.ehlo()
    server.starttls()
    server.login('admin@ketodiets360.com', 'KetoDiets360$%&')
    return server

def send_msg(server, email, name, message_template):
    msg = MIMEMultipart()
    message = message_template.substitute(PERSON_NAME=name)
    msg['From'] = 'KetoDiets360 <' + MY_ADDRESS + '>'
    msg['To'] = email
    -msg['Subject'] = 'Proof you can quickly transform your body'
    msg.attach(MIMEText(message, 'html'))
    server.send_message(msg)
    del msg

filename = 'list_test'
df = read_list_pandas(filename)
server = connect_SMTP()
template = load_template('C1_E1')
for index, row in df.iterrows():
    print(f'Sending email to: {row["Email Address"]} - {row["First Name"]}')
    send_msg(server, row['Email Address'], row['First Name'], template)
