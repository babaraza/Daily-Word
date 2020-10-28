from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from utilities.settings import sendgrid_api_key


def send_mail(email_from, email_to, email_name, email_sub, email_msg):
    """
    Sends an email using SendGrid API

    :param email_from: The sender email
    :param email_to: List of emails to send to (can be more than 1)
    :param email_name: The sender name
    :param email_sub: The subject of the email
    :param email_msg: The email message body
    """

    message = Mail(
        from_email=(email_from, email_name),
        to_emails=email_to,
        subject=email_sub,
        html_content=email_msg)
    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
