import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mail_to_admin(errors_list, recipients_list):
    errors_list = str(errors_list)
    recipients = recipients_list
    subject = 'Список (id) аварийных приложений /api/apps/'
    text = f'Список аварийных app_id: {errors_list}'

    server = 'smtp.yandex.ru'
    user = 'alex.u.test@yandex.ru'
    password = 'Passwordfortest12'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'MegaFone app report from <' + user + '>'
    msg['To'] = ', '.join(recipients)

    errors_list = MIMEText(text, 'plain')
    msg.attach(errors_list)

    mail = smtplib.SMTP_SSL(server, 465)
    mail.login(user, password)
    mail.sendmail(user, recipients, msg.as_string())
    mail.quit()

