import tkinter as tk
from tkinter import messagebox
import webbrowser
from GmailConnect import connect_imap, fetch_latest_email

# ฟังก์ชันเปิด Gmail ในเบราว์เซอร์
def open_gmail():
    webbrowser.open("https://mail.google.com")

# ฟังก์ชันแสดงอีเมลล่าสุด
def show_email_content():
    mail = connect_imap()  # เรียกใช้ฟังก์ชัน connect_imap จาก GmailConnect.py
    if not mail:
        messagebox.showerror("ข้อผิดพลาด", "ไม่สามารถเชื่อมต่อกับ Gmail ได้!")
        return

    email_data = fetch_latest_email(mail)  # เรียกใช้ฟังก์ชัน fetch_latest_email
    subject = email_data["subject"]
    body = email_data["body"]

    if body:
        messagebox.showinfo("หัวข้ออีเมลล่าสุด", f"{subject}\n\n{body}")
    else:
        messagebox.showwarning("แจ้งเตือน", subject)

# ฟังก์ชันสร้าง GUI ด้วย Tkinter
def create_gui():
    root = tk.Tk()
    root.title("XSPAM")

    tk.Label(root, text="FOUND SPAM EMAIL !!!", font=("Arial", 16)).pack(pady=30)

    tk.Button(root, text="CHECK THE LAST EMAIL", command=show_email_content, width=20).pack(pady=5)
    tk.Button(root, text="OPEN Gmail", command=open_gmail, width=20).pack(pady=5)
    tk.Button(root, text="EXIT", command=root.quit, width=20).pack(pady=5)

    root.mainloop()

# เรียกใช้งาน GUI
if __name__ == "__main__":
    create_gui()
