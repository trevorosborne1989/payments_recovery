import logging
import smtplib
import sys
from datetime import datetime
from email.message import EmailMessage

from src.config.config import *


def send_email(recipient, subject, body):
    """
    Sends an email using the mail.mt.gov SMTP server. Can only send to
    one recipient.
    :param recipient: recipient of email
    :param subject: subject of the email
    :param body: body of the email
    :return: None
    """
    try:
        msg = EmailMessage()
        msg.set_content(body)

        msg['Subject'] = subject
        msg['From'] = EMAIL_NOTIFICATIONS_FROM
        msg['To'] = recipient

        # Send the message via the host SMTP server
        s = smtplib.SMTP(EMAIL_NOTIFICATIONS_HOST)
        s.send_message(msg)
        logging.info(f"Email notification send to {recipient}")
        s.quit()
    except Exception:
        logging.exception("Exception raised during send_email")
        raise


def configure_logging():
    logging_level = logging.DEBUG
    # An optional command-line argument can be used to explicitly
    # set logging level
    if len(sys.argv) == 2:
        input_logging_level = sys.argv[2]
        logging_level = getattr(logging, input_logging_level.upper(), None)
        if not isinstance(logging_level, int):
            raise ValueError(f'Invalid log level: {logging_level}')

    # Set up logging
    log_name = (LOCAL_LOG_DIR + '/' + 'warrant_recovery_' + (datetime.now().strftime("%Y/%m/%d")).replace('/', '') +
                '.txt')
    logging.basicConfig(filename=log_name,
                        level=logging_level,
                        format='%(asctime)s - :%(levelname)s: - %(name)s - %(message)s',
                        filemode='w')
    return log_name
