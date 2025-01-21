import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# --- ฟังก์ชันสำหรับโหลดข้อมูล ---
def load_cleaned_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("ข้อมูลที่โหลดมา:")
        print(data.head())
        return data
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการโหลดไฟล์: {e}")
        return None

# --- ฟังก์ชันสำหรับ Tokenization และ Bag-of-Words ---
def tokenize_and_add_bow(data, text_column):
    print("\n--- แปลงข้อความเป็น Bag-of-Words ---")
    vectorizer = CountVectorizer()
    bow_matrix = vectorizer.fit_transform(data[text_column])

    # แปลง Matrix เป็น DataFrame
    bow_df = pd.DataFrame(bow_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    print("Bag-of-Words DataFrame:")
    print(bow_df.head())

    # รวมคอลัมน์ใหม่กลับเข้า DataFrame เดิม
    data = pd.concat([data.reset_index(drop=True), bow_df.reset_index(drop=True)], axis=1)
    return data

# --- ฟังก์ชันสำหรับ Tokenization และ TF-IDF ---
def tokenize_and_add_tfidf(data, text_column):
    print("\n--- แปลงข้อความเป็น TF-IDF ---")
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(data[text_column])

    # แปลง Matrix เป็น DataFrame
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    print("TF-IDF DataFrame:")
    print(tfidf_df.head())

    # รวมคอลัมน์ใหม่กลับเข้า DataFrame เดิม
    data = pd.concat([data.reset_index(drop=True), tfidf_df.reset_index(drop=True)], axis=1)
    return data

# --- ฟังก์ชันสำหรับบันทึกข้อมูล ---
def save_updated_data(data, output_path):
    try:
        data.to_csv(output_path, index=False)
        print(f"\nบันทึกข้อมูลที่อัปเดตแล้วที่: {output_path}")
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการบันทึกไฟล์: {e}")

# --- การเรียกใช้งาน ---
if __name__ == "__main__":
    # ระบุไฟล์ที่ Clean แล้ว
    cleaned_file = "cleaned_data.csv"  # ไฟล์ต้นฉบับที่ Clean แล้ว
    updated_file = "updated_data.csv"  # ไฟล์ปลายทางหลังอัปเดต

    # โหลดข้อมูล
    df_cleaned = load_cleaned_data(cleaned_file)

    if df_cleaned is not None:
        # เพิ่มข้อมูล Bag-of-Words
        df_with_bow = tokenize_and_add_bow(df_cleaned, 'text')

        # เพิ่มข้อมูล TF-IDF
        df_with_tfidf = tokenize_and_add_tfidf(df_cleaned, 'text')

        # บันทึกข้อมูลที่อัปเดตแล้ว
        save_updated_data(df_with_tfidf, updated_file)
