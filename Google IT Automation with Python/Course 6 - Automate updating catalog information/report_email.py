#!/usr/bin/env python3
from datetime import datetime
import email.message
import mimetypes
import os
import smtplib
import reports
import sys


def generate_email(sender, recipient, subject, body, attachment_path):
    """Creates an email with an attachement."""
    # Basic Email formatting
    message = email.message.EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    # Making attachment_path optional, if the attachment variable is empty string, no email will be sent.
    if not attachment_path == "":
        # Process the attachment and add it to the email
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=attachment_filename)

    return message


def send_email(message):
    """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

def main(args):
    """Process selected data from description and generate a full report out of it."""
    folder = "supplier-data/descriptions/"
    
    supplier_data = []
    for file in os.listdir(folder):
        filename, ext = os.path.splitext(file)
        lines = open(folder+file, 'r')
        name = ['name', lines.readline().replace('\n', '').strip()]
        weight = ['weight', lines.readline().replace('\n', '')]
        supplier_data.append(name)
        supplier_data.append(weight)
        supplier_data.append(['\n'])
        supplier_data.append([])
    # create title for report
    title = "Processed Update on {}".format(datetime.now())

    # generate report
    report = reports.generate_report(
        "/tmp/processed.pdf",
        title,
        str(supplier_data)
    )

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = str(supplier_data)
    attachment_path =  "/tmp/processed.pdf"

    message = generate_email(sender, receiver, subject, body, attachment_path)

    send_email(message)

if __name__ == "__main__":
  main(sys.argv)