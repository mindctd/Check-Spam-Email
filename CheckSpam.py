# import pandas as pd

# df = pd.read_csv("cleaned_data.csv")

# # ตรวจสอบคอลัมน์ที่มีอยู่
# print("📝 คอลัมน์ที่มีอยู่ใน cleaned_data.csv:", df.columns)

# # ตรวจสอบค่าของคอลัมน์ spam
# print("\n📊 จำนวนแต่ละคลาสใน `spam ำeiei`:")
# print(df["spam"].value_counts())
 
# import pandas as pd

# df = pd.read_csv("updated_data.csv")
# print("📝 คอลัมน์ที่มีใน updated_data.csv:", df.columns.tolist())
# print("\n📊 ตัวอย่างข้อมูล 5 แถวแรก:")
# print(df.head())
# print("\n📊 จำนวนแต่ละคลาสใน `spam`:")
# print(df['spam'].value_counts())

import pandas as pd

df = pd.read_csv("cleaned_data.csv")
print("📊 จำนวนแต่ละคลาสใน `spam` จาก cleaned_data.csv:")
print(df['spam'].value_counts())
