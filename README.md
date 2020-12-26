# EmailSender
 Script that sends an email to all addresses contained in the "list.csv" file.
 
 ## Email configuration
 Just put your email address and password in these fields.
 
 MY_ADDRESS = 'admin@example.com'
 MY_PASSWORD = 'password'
 
 Replace "yourDomain.com" with your own domain if you have one, or use "smtp.gmail.com" if you have a Gmail account.
 
 If you use a Gmail account you have to active the access from not secured apps, you can do it in your Google account settings -> Securiy -> Access less secure apps.
 
 Replace "Alias" with the name you want to show and write the subject.
 
 ## List 
 Just open the "list.csv" file and write down all cantacts that have to receive your email with their name.
 
 "Email Address","First Name"
 email1@domain.com,Name1
 email2@domani.com,Name2
 email3@domain.com,Name3
 
 ## Write your email
 Into "Emails" folder put your email html template than put your email file name into: template = load_template('mail1') 
 
 # Now you can run the script!
 
 
 
