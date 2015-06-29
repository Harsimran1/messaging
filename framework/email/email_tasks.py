import smtplib
from email.mime.text import MIMEText
from framework.celery.celery_start import celery


@celery.task
def add(a,b):
    return a+b


@celery.task
def send_email(to=None, subject=None, message=None):
    """sends email from hairycode-noreply to specified destination

    :param to: string destination address
    :param subject: subject of email
    :param message: body of message

    :return: True if successful
    """
    # prep message
    fro="harsimran@zemosolabs.com"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = fro
    msg['To'] = to

    # send message




    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('harsimran@zemosolabs.com', '')
    s.sendmail('harsimran@zemosolabs.com', to, msg.as_string())
    s.quit()
    return True
