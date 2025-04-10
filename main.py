import pandas as pd
import pickle
import time
import imaplib
import email
from GmailConnect import connect_imap
from Popup import create_gui

# -----------------------------
# โหลดโมเดล
# -----------------------------
with open("spam_model.pkl", "rb") as model_file:
    model, vectorizer = pickle.load(model_file)

print("✅ โหลดโมเดลสำเร็จ!")


def predict_spam(email_text):
    X_new = vectorizer.transform([email_text])
    prediction = model.predict(X_new)[0]
    return prediction


# -----------------------------
# ทดสอบโมเดลกับ updated_data.csv พร้อมแสดงแถว
# -----------------------------
def test_model_with_updated_data():
    print("\n🧪 ทดสอบโมเดลกับข้อมูลจาก updated_data.csv")

    try:
        df = pd.read_csv("updated_data.csv")
        print("✅ โหลดไฟล์ updated_data.csv สำเร็จ")

        # ตรวจสอบจำนวน label
        print("\n🧮 จำนวน label ใน updated_data.csv:")
        print(df["spam"].value_counts())

        if df[df["spam"] == 0].shape[0] < 3 or df[df["spam"] == 1].shape[0] < 3:
            print("⚠️ ไม่พบข้อมูล label=0 หรือ label=1 เพียงพอในการสุ่ม")
            return

        non_spam = df[df["spam"] == 0].sample(3)
        spam = df[df["spam"] == 1].sample(3)

        print("\n📧 ทดสอบ Non-Spam:")
        for idx, row in non_spam.iterrows():
            text = row["text"]
            pred = predict_spam(text)
            print(f"🟢 Row: {idx}")
            print(f"✅ [label=0] → {'Spam ❌' if pred == 1 else 'Not Spam ✅'}")
            print(f"   ตัวอย่างข้อความ: {text[:100]}...\n")

        print("📧 ทดสอบ Spam:")
        for idx, row in spam.iterrows():
            text = row["text"]
            pred = predict_spam(text)
            print(f"🔴 Row: {idx}")
            print(f"❌ [label=1] → {'Spam ✅' if pred == 1 else 'Not Spam ❌'}")
            print(f"   ตัวอย่างข้อความ: {text[:100]}...\n")

    except FileNotFoundError:
        print("❌ ไม่พบไฟล์ updated_data.csv")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")


# -----------------------------
# ฟังอีเมลจาก Gmail (เปิดใช้เมื่อพร้อม)
# -----------------------------
def fetch_new_email(mail):
    mail.select("inbox")
    result, data = mail.search(None, "UNSEEN")

    if result == "OK" and data[0]:
        latest_email_id = data[0].split()[-1]
        result, msg_data = mail.fetch(latest_email_id, "(RFC822)")

        if result == "OK":
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)
            subject = msg["subject"] if msg["subject"] else "(No Subject)"
            body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode("utf-8", errors="ignore")
            else:
                body = msg.get_payload(decode=True).decode("utf-8", errors="ignore")

            return {"subject": subject, "body": body}

    return None


def listen_for_new_email():
    mail = connect_imap()
    if not mail:
        print("❌ ไม่สามารถเชื่อมต่อ Gmail ได้!")
        return

    print("🔄 ระบบกำลังรออีเมลใหม่... (IMAP IDLE)")

    while True:
        mail.select("inbox")
        mail.send(b"IDLE\r\n")
        time.sleep(1)

        email_data = fetch_new_email(mail)
        if email_data:
            email_body = email_data["body"]
            email_subject = email_data["subject"]

            is_spam = predict_spam(email_body)
            if is_spam:
                print("❌ พบอีเมลสแปม!")
                print("📌 หัวข้อ:", email_subject)
                print("📄 เนื้อหา (บางส่วน):", email_body[:500])
                create_gui()
            else:
                print("✅ อีเมลปกติ:", email_subject)


# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    # test_model_with_updated_data()     # ✅ ทดสอบ model พร้อม row
    listen_for_new_email()          # 🔄 เปิดเมื่อจะใช้กับอีเมลจริง

