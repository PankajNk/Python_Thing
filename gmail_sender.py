import smtplib as s 
ob=s.SMTP("smtp.gmail.com",587)

ob.starttls()
#tls is encryptn  
#turn (less secure) in gmail
ob.login("pankajrnaik317@gmail.com",'Password_of_email')

subject="test for sending email using python"
body="email is sent by using python  on 1st SePt...Happy Lockdown:):)"

message = "Subject:{}\n\n{}".format(subject,body)
#print(message)

#In place of 1st email write the person gmail who you want to send 
listOfAddress=["1st email.com","2nd gmail.com"]
ob.sendmail("pankajrnaik317",listOfAddress,message)
#take 3 parameter email from ,no of email and msg

print("jale ra send or finished ")
ob.quit()

