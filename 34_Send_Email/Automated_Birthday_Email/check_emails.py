# Test email addresses
import requests

def check_email_domain(email):
    domain = email.split('@')[1]
    print(f"Email: {email}")
    print(f"Domain: {domain}")
    
    # Try to check if domain exists (basic check)
    try:
        import socket
        socket.gethostbyname(domain)
        print(f"✅ Domain {domain} exists")
    except socket.gaierror:
        print(f"❌ Domain {domain} doesn't exist or unreachable")
    print("-" * 50)

emails = [
    "johndoeforpython@eyopmail.com",
    "janedoeforpython@eyopmail.com", 
    "aliceforpython@yopmail.com"
]

for email in emails:
    check_email_domain(email)