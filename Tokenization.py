import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# --- ฟังก์ชันตรวจสอบและแสดงข้อมูล Dataset ---
def inspect_dataset(data):
    print(f"\n📂 ข้อมูลตัวอย่างจากไฟล์ {cleaned_file}:")
    print(data.head())
    print("\n📊 สรุปข้อมูล:")
    print(data.info())
    print("\n📈 ค่าที่ไม่ซ้ำในคอลัมน์ 'spam':", data['spam'].unique())

# --- ฟังก์ชันปรับสมดุลข้อมูล ---
def balance_data(data):
    inspect_dataset(data)

    if data.empty or 'spam' not in data.columns:
        raise ValueError("❌ ไม่มีข้อมูลหรือไม่มีคอลัมน์ 'spam'")

    spam_data = data[data['spam'] == 1]
    not_spam_data = data[data['spam'] == 0]

    if spam_data.empty or not_spam_data.empty:
        print("⚠️ พบข้อมูลขาดคลาส จะทำ Oversampling")
        if spam_data.empty:
            spam_data = not_spam_data.sample(n=1, replace=True, random_state=42)
        if not_spam_data.empty:
            not_spam_data = spam_data.sample(n=1, replace=True, random_state=42)

    min_count = min(len(spam_data), len(not_spam_data))
    spam = spam_data.sample(n=min_count, random_state=42)
    not_spam = not_spam_data.sample(n=min_count, random_state=42)

    balanced_data = pd.concat([spam, not_spam]).sample(frac=1, random_state=42).reset_index(drop=True)
    print("\n📊 จำนวนแต่ละคลาสหลังปรับสมดุล:")
    print(balanced_data['spam'].value_counts())
    return balanced_data

# --- การเรียกใช้งาน ---
if __name__ == "__main__":
    cleaned_file = "cleaned_data.csv"
    updated_file = "updated_data.csv"

    try:
        df_cleaned = pd.read_csv(cleaned_file)
    except FileNotFoundError:
        print(f"❌ ไม่พบไฟล์ '{cleaned_file}'")
        exit(1)

    print("📋 ข้อมูลใน df_cleaned ก่อนการตรวจสอบ:")
    print(df_cleaned.head())
    print("\n📊 ค่าที่ไม่ซ้ำในคอลัมน์ 'spam':", df_cleaned['spam'].unique())

    # กรองข้อมูลให้เหลือเฉพาะค่า 0 หรือ 1
    df_cleaned = df_cleaned[df_cleaned['spam'].isin(['0', '1'])]
    df_cleaned['spam'] = df_cleaned['spam'].astype(int)
    print("\n📊 ค่าที่ไม่ซ้ำหลังการแปลงเป็นตัวเลข:")
    print(df_cleaned['spam'].unique())

    df_balanced = balance_data(df_cleaned)
    print("✅ ปรับสมดุลข้อมูลสำเร็จ")

# --- บันทึกข้อมูลล่าสุดที่อัปเดตเป็นไฟล์ CSV ---
df_balanced.to_csv("updated_data.csv", index=False)
print("✅ บันทึกไฟล์ข้อมูลล่าสุดสำเร็จ: updated_data.csv")