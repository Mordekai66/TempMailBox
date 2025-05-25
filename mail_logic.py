from mailtm import Email

email = Email()
current_email = None

def get_domain():
    return email.domain

def generate_new_email():
    global current_email
    email.register()
    current_email = str(email.address)
    return current_email

def start_listening(callback):
    email.start(callback)