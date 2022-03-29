#!/usr/bin/env python3
import shutil
import psutil
import socket
import os
from report_email import generate_email as email_generate
from report_email import send_email as email_send


def check_cpu_usage(cpu):
    """This function will check if CPU usage is over 80%"""
    top = psutil.cpu_percent(cpu)
    return top < 80


def check_disk_usage(disk):
    """This function will check if Available disk space is less than 20%"""
    du = shutil.disk_usage(disk)
    # calculating percent of free disk
    free_disk = du.free / du.total * 100
    return free_disk > 20


def check_memory_usage():
    """This function will check if Available memory is less than 500MB"""
    # using the psutil command and converting it to dictionary and getting the available memory
    memory = dict(psutil.virtual_memory()._asdict())['available']
    # converting available memory to mb
    available_memory = (memory / 1024) / 1024
    return available_memory > 500


def resolve_hostname():
    """This function will check if localhost cannot be resolved to 127.0.0.1"""
    hostname = socket.gethostbyname('localhost')
    return hostname == '127.0.0.1'


def check_error():
    """This function will return subject according to the conditions met"""
    if not check_disk_usage('/'):
        subject = 'Error - Available disk space is less than 20%'
        return subject
    elif not check_cpu_usage(1):
        subject = 'Error - CPU usage is over 80%'
        return subject
    elif not check_memory_usage():
        subject = 'Error - Available memory is less than 500MB'
        return subject
    elif not resolve_hostname():
        subject = 'Error - localhost cannot be resolved to 127.0.0.1'
        return subject
    # Here we are returning none, so that we can use it later to compare it in email subject
    else:
        return None


if __name__ == "__main__":
    # To ge the username from environment variable
    USER = os.getenv('USER')
    # Running the check error function to fetch subject line
    new_subject = check_error()
    # If we found None as return value do nothing, otherwise send email
    if new_subject is not None:
        # body line give in assignment for email
        new_body = 'Please check your system and resolve the issue as soon as possible.'
        # structuring email and attaching the file. Then sending the email, using the custom module.
        msg = email_generate("automation@example.com", "{}@example.com".format(USER),
                             new_subject, new_body, "")
        email_send(msg)
