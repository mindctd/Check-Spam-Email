# import time
# from imapclient import IMAPClient
# from Accuracy import vectorizer, model  # โหลดโมเดลที่ฝึกไว้
# from GmailConnect import connect_imap, fetch_latest_email  # ใช้เชื่อมต่อ Gmail
# from Popup import create_gui  # ใช้แสดง Popup แจ้งเตือน

# # ตรวจสอบว่าโมเดลโหลดสำเร็จหรือไม่
# if model and vectorizer:
#     print("✅ โมเดลและ Vectorizer โหลดสำเร็จ!")
# else:
#     print("❌ โหลดโมเดลไม่สำเร็จ! ตรวจสอบไฟล์ Accuracy.py")
#     exit()

# def predict_spam(email_text):
#     """ใช้โมเดลที่ฝึกไว้ทำนายว่าอีเมลเป็นสแปมหรือไม่"""
#     X_new = vectorizer.transform([email_text])
#     prediction = model.predict(X_new)[0]  # 1 = Spam, 0 = Not Spam
#     return prediction

# def check_email(mail):
#     """เช็คอีเมลใหม่และตรวจสอบว่าเป็น Spam หรือไม่"""
#     email_data = fetch_latest_email(mail)  # ดึงอีเมลล่าสุด
#     if not email_data:
#         return
    
#     email_body = email_data.get("body", "")
#     email_subject = email_data.get("subject", "")
    
#     if email_body:
#         is_spam = predict_spam(email_body)
#         if is_spam:
#             print("❌ พบอีเมลสแปม!")
#             print("📌 หัวข้อ:", email_subject)
#             print("📄 เนื้อหา (บางส่วน):", email_body[:500])  # แสดง 500 ตัวอักษรแรก
#             create_gui()  # แสดง Popup แจ้งเตือน
#         else:
#             print("✅ อีเมลปกติ")
#     else:
#         print("⚠️ ไม่พบเนื้อหาอีเมล")

# def listen_for_new_emails():
#     """ระบบจะเช็คอีเมลใหม่โดยอัตโนมัติเมื่อมีการส่งอีเมลเข้ามา"""
#     with IMAPClient('imap.gmail.com') as client:
#         client.login('mindstory483@gmail.com', 'ccccccccx483')
#         client.select_folder('INBOX')

#         print("[ระบบ] รออีเมลใหม่เข้ามา...")
#         client.idle()

#         while True:
#             try:
#                 responses = client.idle_check(timeout=60)  # รอการแจ้งเตือนการมีอีเมลใหม่
#                 if responses:
#                     check_email(client)  # ตรวจสอบอีเมลที่เข้ามาใหม่
#             except Exception as e:
#                 print(f"❌ เกิดข้อผิดพลาด: {e}")
#                 break

# if __name__ == "__main__":
#     listen_for_new_emails()

# import time
# import pickle
# from GmailConnect import connect_imap, fetch_latest_email  # ใช้เชื่อมต่อ Gmail
# from Popup import create_gui  # ใช้แสดง Popup แจ้งเตือน

# # --- โหลดโมเดลที่ฝึกจาก updated_data.csv ---
# with open("spam_model.pkl", "rb") as model_file:
#     model, vectorizer = pickle.load(model_file)

# print("✅ โมเดลจาก updated_data.csv โหลดสำเร็จ!")

# def predict_spam(email_text):
#     """ใช้โมเดลที่ฝึกไว้ทำนายว่าอีเมลเป็นสแปมหรือไม่"""
#     X_new = vectorizer.transform([email_text])
#     prediction = model.predict(X_new)[0]  # 1 = Spam, 0 = Not Spam
#     return prediction

# def check_email():
#     """เช็คอีเมลใหม่และตรวจสอบว่าเป็น Spam หรือไม่"""
#     mail = connect_imap()  # เชื่อมต่อ Gmail
#     if not mail:
#         print("❌ ไม่สามารถเชื่อมต่อ Gmail ได้!")
#         return
    
#     email_data = fetch_latest_email(mail)  # ดึงอีเมลล่าสุด
#     email_body = email_data.get("body", "")
#     email_subject = email_data.get("subject", "")
    
#     if email_body:
#         is_spam = predict_spam(email_body)
#         if is_spam:
#             print("❌ พบอีเมลสแปม!")
#             print("📌 หัวข้อ:", email_subject)
#             print("📄 เนื้อหา (บางส่วน):", email_body[:500])  # แสดง 500 ตัวอักษรแรก
#             create_gui()  # แสดง Popup แจ้งเตือน
#         else:
#             print("✅ อีเมลปกติ")
#     else:
#         print("⚠️ ไม่พบเนื้อหาอีเมล")

# def auto_check():
#     """ระบบตรวจสอบอีเมลอัตโนมัติทุก 5 นาที"""
#     while True:
#         print("\n[ระบบ] กำลังตรวจสอบอีเมลใหม่...")
#         check_email()
#         time.sleep(300)  # รอ 5 นาทีแล้วตรวจใหม่

# if __name__ == "__main__":
#     auto_check()

import time
import pickle
import imaplib
import email
from GmailConnect import connect_imap  # ใช้เชื่อมต่อ Gmail
from Popup import create_gui  # ใช้แสดง Popup แจ้งเตือน

# --- โหลดโมเดลที่ฝึกจาก updated_data.csv ---
with open("spam_model.pkl", "rb") as model_file:
    model, vectorizer = pickle.load(model_file)

print("✅ โมเดลจาก updated_data.csv โหลดสำเร็จ!")

def predict_spam(email_text):
    """ใช้โมเดลที่ฝึกไว้ทำนายว่าอีเมลเป็นสแปมหรือไม่"""
    X_new = vectorizer.transform([email_text])
    prediction = model.predict(X_new)[0]  # 1 = Spam, 0 = Not Spam
    return prediction

def fetch_new_email(mail):
    """ดึงอีเมลใหม่ล่าสุด"""
    mail.select("inbox")  # เลือกกล่องจดหมายเข้า
    result, data = mail.search(None, "UNSEEN")  # ค้นหาอีเมลที่ยังไม่ได้อ่าน
    
    if result == "OK" and data[0]:
        latest_email_id = data[0].split()[-1]  # ดึง ID ของอีเมลล่าสุด
        result, msg_data = mail.fetch(latest_email_id, "(RFC822)")  # ดึงข้อมูล
        
        if result == "OK":
            raw_email = msg_data[0][1]  # ดึงข้อมูลเมลดิบ
            msg = email.message_from_bytes(raw_email)  # แปลงเป็น object
            
            subject = msg["subject"] if msg["subject"] else "(No Subject)"
            body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
            else:
                body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

            return {"subject": subject, "body": body}

    return None  # ไม่มีอีเมลใหม่

def listen_for_new_email():
    """ใช้ IMAP IDLE เพื่อฟังอีเมลใหม่ และแจ้งเตือนทันที"""
    mail = connect_imap()  # เชื่อมต่อ Gmail
    if not mail:
        print("❌ ไม่สามารถเชื่อมต่อ Gmail ได้!")
        return
    
    print("🔄 ระบบกำลังรออีเมลใหม่... (IMAP IDLE)")

    while True:
        mail.select("inbox")
        mail.send(b"IDLE\r\n")  # เข้าโหมดรอแจ้งเตือน
        time.sleep(1)  # รอการแจ้งเตือน

        email_data = fetch_new_email(mail)  # ดึงอีเมลใหม่
        if email_data:
            email_body = email_data["body"]
            email_subject = email_data["subject"]
            
            is_spam = predict_spam(email_body)
            if is_spam:
                print("❌ พบอีเมลสแปม!")
                print("📌 หัวข้อ:", email_subject)
                print("📄 เนื้อหา (บางส่วน):", email_body[:500])  # แสดง 500 ตัวอักษรแรก
                create_gui()  # แสดง Popup แจ้งเตือน
            else:
                print("✅ อีเมลปกติ:", email_subject)

if __name__ == "__main__":
    listen_for_new_email()
