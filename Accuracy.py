import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

# --- 1. โหลดข้อมูลจาก updated_data.csv ---
df = pd.read_csv("updated_data.csv")
df['spam'] = df['spam'].astype(int)

# --- 2. แปลงข้อความเป็น TF-IDF ---
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['text'])
y = df['spam']

# --- 3. แบ่งข้อมูลเป็น 80% Train และ 20% Test ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# --- 4. สร้างและฝึกโมเดล Logistic Regression ---
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train, y_train)
print("✅ โมเดลฝึกเสร็จแล้ว")

# --- 5. บันทึกโมเดลหลังฝึกด้วย updated_data.csv ---
with open("spam_model.pkl", "wb") as model_file:
    pickle.dump((model, vectorizer), model_file)
print("✅ บันทึกโมเดลสำเร็จ: spam_model.pkl")

# --- 6. ฟังก์ชันทดสอบข้อความ ---
def predict_spam(text):
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)[0]
    return "Spam 🚨" if prediction == 1 else "Not Spam ✅"

# --- ทดสอบข้อความจาก updated_data.csv พร้อมบอกลำดับแถว ---
not_spam_samples = df[df['spam'] == 0].sample(3, random_state=42)
spam_samples = df[df['spam'] == 1].sample(3, random_state=42)

print("\n--- 🧪 ทดสอบโมเดลกับข้อความที่เป็น Not Spam (0) ---")
for idx, row in not_spam_samples.iterrows():
    print(f"📂 แถวที่: {idx}")
    print(f"📩 ข้อความ: {row['text']}")
    print(f"📢 ผลการทำนาย: {predict_spam(row['text'])}\n")

print("\n--- 🧪 ทดสอบโมเดลกับข้อความที่เป็น Spam (1) ---")
for idx, row in spam_samples.iterrows():
    print(f"📂 แถวที่: {idx}")
    print(f"📩 ข้อความ: {row['text']}")
    print(f"📢 ผลการทำนาย: {predict_spam(row['text'])}\n")
