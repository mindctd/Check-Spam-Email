import pandas as pd

# --- ฟังก์ชันสำหรับโหลดไฟล์ CSV ---
def load_csv(file_path):
    try:
        # อ่านไฟล์ CSV
        data = pd.read_csv(file_path, encoding="utf-8", sep=",")  # ตัวคั่นเป็น ',' และ Encoding แบบ UTF-8
        print("ข้อมูลที่โหลดมา (ต้นฉบับ):")
        print(data.head())  # แสดงข้อมูล 5 แถวแรก
        return data
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการโหลดไฟล์: {e}")
        return None

# --- ฟังก์ชันสำหรับ Clean ข้อมูล ---
def clean_data(data):
    print("\n--- เริ่มกระบวนการ Clean ข้อมูล ---")
    
    # 1. ตรวจสอบค่าที่หายไป
    print("\nค่าที่หายไปในแต่ละคอลัมน์ (ก่อน Clean):")
    print(data.isnull().sum())

    # 2. ลบคอลัมน์ที่ไม่มีข้อมูล (ข้อมูลว่างเกือบทั้งหมด)
    print("\nลบคอลัมน์ที่มีข้อมูลน้อยกว่า 1%:")
    data_cleaned = data.dropna(axis=1, thresh=0.01 * len(data))  # เก็บเฉพาะคอลัมน์ที่มีข้อมูลอย่างน้อย 1%
    print(f"เหลือจำนวนคอลัมน์: {data_cleaned.shape[1]}")

    # 3. ลบแถวที่ไม่มีข้อมูลในทุกคอลัมน์
    print("\nลบแถวที่ไม่มีข้อมูลเลย:")
    data_cleaned = data_cleaned.dropna(how="all")
    print(f"เหลือจำนวนแถว: {data_cleaned.shape[0]}")

    # 4. เติมค่าที่หายไปในคอลัมน์ที่สำคัญ
    if 'spam' in data_cleaned.columns:
        data_cleaned['spam'] = data_cleaned['spam'].fillna(data_cleaned['spam'].mode()[0])  # เติมค่าที่พบบ่อยที่สุด (mode)

    # 5. จัดการค่าผิดปกติ (Outliers)
    if 'จำนวน' in data_cleaned.columns:
        print("\nจัดการค่าผิดปกติในคอลัมน์ 'จำนวน':")
        q1 = data_cleaned['จำนวน'].quantile(0.25)
        q3 = data_cleaned['จำนวน'].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        data_cleaned = data_cleaned[(data_cleaned['จำนวน'] >= lower_bound) & (data_cleaned['จำนวน'] <= upper_bound)]
        print(f"ข้อมูลหลังจัดการค่าผิดปกติ: {data_cleaned.shape[0]} แถว")

    # 6. สรุปผลหลัง Clean
    print("\nข้อมูลหลังการ Clean:")
    print(data_cleaned.info())
    print("\nค่าที่หายไปหลังการ Clean:")
    print(data_cleaned.isnull().sum())

    return data_cleaned

# --- ฟังก์ชันสำหรับบันทึกข้อมูล ---
def save_cleaned_data(data, output_path):
    try:
        data.to_csv(output_path, index=False)
        print(f"\nบันทึกข้อมูลที่ Clean แล้วที่: {output_path}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการบันทึกไฟล์: {e}")

# --- การเรียกใช้งาน ---
if __name__ == "__main__":
    # ใส่ชื่อไฟล์ CSV ที่ต้องการ
    input_file = "data.csv"  # ระบุไฟล์ CSV ต้นทาง
    output_file = "cleaned_data.csv"  # ระบุไฟล์ปลายทาง

    # โหลดข้อมูล
    df = load_csv(input_file)

    if df is not None:
        # Clean ข้อมูล
        cleaned_df = clean_data(df)

        # บันทึกข้อมูลที่ Clean แล้ว
        save_cleaned_data(cleaned_df, output_file)
