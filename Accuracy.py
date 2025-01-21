from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd
from sklearn.preprocessing import LabelEncoder  # เพิ่มการใช้ LabelEncoder

# --- 1. โหลดข้อมูล ---
df = pd.read_csv("cleaned_data.csv")

# --- 2. แปลงข้อความเป็น TF-IDF ---
vectorizer = TfidfVectorizer(max_features=5000)  # จำกัด Features สูงสุดที่ 5000
X = vectorizer.fit_transform(df['text'])  # ใช้คอลัมน์ 'text' ในการแปลง

# --- 3. แปลงค่าในคอลัมน์ 'spam' ให้เป็นตัวเลข (0 และ 1) ---
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['spam'])  # แปลงค่าของ 'spam' เป็น 0 และ 1

# --- 4. แบ่งข้อมูลเป็น 80% Train และ 20% Test ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 5. สร้างโมเดล Logistic Regression ---
model = LogisticRegression()

# --- 6. ฝึกโมเดลด้วยข้อมูล Train ---
model.fit(X_train, y_train)

# --- 7. ทำนายผลด้วยข้อมูล Test ---
y_pred = model.predict(X_test)

# --- 8. ประเมินผลการทำงานของโมเดล ---
print("ผลการประเมินโมเดล:")
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")  # การคำนวณความแม่นยำ
print(classification_report(y_test, y_pred))  # รายงานการจำแนกประเภท

# --- 9. เปรียบเทียบค่าทำนายกับค่าจริง ---
comparison_df = pd.DataFrame({
    'True Label': y_test,
    'Predicted Label': y_pred
})

# แสดงผลลัพธ์การเปรียบเทียบ
print("\n--- ผลการเปรียบเทียบค่าทำนายกับค่าจริง ---")
print(comparison_df.head())  # แสดง 5 แถวแรกของการเปรียบเทียบ
