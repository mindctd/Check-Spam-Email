import email
from email.header import decode_header
import os
import imaplib
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import logging

# ตั้งค่า Logging สำหรับ Debugging
logging.basicConfig(level=logging.INFO)

SCOPES = ['https://mail.google.com/']

# ฟังก์ชันสำหรับการรับรองสิทธิ์ Gmail
def authenticate_gmail():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=24500)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

# ฟังก์ชันเชื่อมต่อ IMAP
def connect_imap():
    creds = authenticate_gmail()
    IMAP_SERVER = "imap.gmail.com"
    IMAP_PORT = 993
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        user_email = "mindstory483@gmail.com"  # เปลี่ยนเป็นอีเมลจริง
        auth_string = f"user={user_email}\1auth=Bearer {creds.token}\1\1"
        mail.authenticate("XOAUTH2", lambda x: auth_string.encode('utf-8'))
        logging.info("เชื่อมต่อ IMAP สำเร็จ!")
        return mail
    except imaplib.IMAP4.error as e:
        logging.error(f"ข้อผิดพลาดในการเชื่อมต่อ IMAP: {e}")
        return None

# ฟังก์ชันดึงอีเมลล่าสุด
def fetch_latest_email(mail, num_emails=1):
    mail.select("inbox")
    status, email_ids = mail.search(None, "ALL")
    email_ids = email_ids[0].split()[-num_emails:]  # ดึงอีเมลล่าสุด
    emails = []

    for email_id in email_ids:
        status, data = mail.fetch(email_id, "(RFC822)")
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8", errors="replace")
        body = None
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode("utf-8", errors="replace")
                    break
        else:
            body = msg.get_payload(decode=True).decode("utf-8", errors="replace")
        emails.append({"subject": subject, "body": body})
    return emails[0] if emails else {"subject": "ไม่มีอีเมล", "body": None}
