from datasets import load_dataset
import pandas as pd
import os

# Tạo thư mục nếu chưa có
os.makedirs("dataset/raw", exist_ok=True)

# Load dataset từ Hugging Face
dataset = load_dataset("uitnlp/vietnamese_students_feedback")

# Chuyển từng split sang DataFrame
train_df = pd.DataFrame(dataset["train"])
valid_df = pd.DataFrame(dataset["validation"])
test_df = pd.DataFrame(dataset["test"])

# Lưu riêng từng file
train_df.to_csv("dataset/raw/train.csv", index=False)
valid_df.to_csv("dataset/raw/valid.csv", index=False)
test_df.to_csv("dataset/raw/test.csv", index=False)

print("Dataset saved successfully!")