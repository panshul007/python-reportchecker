import smtplib
import logging

from email.mime.text import MIMEText


username="user@domain.com"
password="password"


def prepareMessage(successMsg,errorMsg,recipients,date):
    messageSuccess = '<br/>'.join(successMsg)
    messageError = '<br/>'.join(errorMsg)
    message = format("%s <br/> %s" %(messageSuccess,messageError))
    msg = MIMEText(message,'html')
    if len(errorMsg)>0:
        msg['Subject'] = format("Error in VCS Report Generation Status for Date: %s" %(date))
    else:
        msg['Subject'] = format("VCS Report Generation Status for Date: %s" %(date))
    msg['From'] = username
    msg['To'] = ','.join(recipients)
    return msg
 
def sendReportGenerationStatusMail(successMsg,errorMsg,recipients,date):
    msg = prepareMessage(successMsg,errorMsg,recipients,date)
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(username,password)
    s.sendmail(username, recipients, msg.as_string())
    s.quit()
    logging.info("Status Email Sent")
