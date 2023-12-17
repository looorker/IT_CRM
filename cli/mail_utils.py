import smtplib
from array import array
from email.mime.text import MIMEText
from email.header import Header

class Mailer:
    def send_mail(self, recipients_emails: list, subject: str, msg_text: str):
        login = 'mr.1o0rker@yandex.ru'
        password = ''

        msg = MIMEText(f'{msg_text}', 'plain', 'utf-8')
        msg['Subject'] = Header(f'{subject}', 'utf-8')
        msg['From'] = login
        msg['To'] = ', '.join(recipients_emails)

        s = smtplib.SMTP('smtp.yandex.ru', 587, timeout=10)
        s.set_debuglevel(1)

        try:
            s.starttls()
            s.login(login, password)
            s.sendmail(msg['From'], recipients_emails, msg.as_string())
        except Exception as ex:
            print(ex)
        finally:
            s.quit()

