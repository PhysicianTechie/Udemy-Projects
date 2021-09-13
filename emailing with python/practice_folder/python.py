import smtplib

#makes password invisible
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com',587)

print(smtp_object.ehlo())

print(smtp_object.starttls())

#password = getpass.getpass('Password Please : ')


#generate app password for gmail -

email = getpass.getpass('Email : ')
password = getpass.getpass('Password: ')
print(smtp_object.login(email, password))



from_address = email
to_address = email
subject = input('enter the subject line : ')
message = input('Enter the body message : ')
msg = "Subject: " + subject + '\n' + message


smtp_object.sendmail(from_address, to_address,msg)



smtp_object.quit()
