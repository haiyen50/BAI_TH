# Đường dẫn tới file companies.csv
# companies_path = os.path.join(data_dir, "companies.csv")
import pandas as pd

# 1. Đọc file companies.csv vào DataFrame companies
companies = pd.read_csv(r'D:\DHKL17A3HN\lab 3\companies.csv')

stocks1 = pd.read_csv("D:\DHKL17A3HN\lab 3\stocks1.csv")
# 1. Đọc file stocks2.csv vào DataFrame stocks2
stocks2 = pd.read_csv(r"D:\DHKL17A3HN\lab 3\stocks2.csv")

# 2. Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks = pd.concat([stocks1, stocks2], ignore_index=True)
# 2. Hiển thị 5 dòng đầu tiên của companies
print("5 dòng đầu tiên của companies:")
print(companies.head())

# 3. Kết hợp stocks và companies dựa trên cột chung là symbol
merged_data = pd.merge(stocks, companies, left_on="symbol", right_on="name")

# 4. Tính giá đóng cửa (close) trung bình cho mỗi công ty
average_close = merged_data.groupby("symbol")["close"].mean()

# 5. Hiển thị kết quả cho 5 công ty đầu tiên
print("\nGiá đóng cửa trung bình cho 5 công ty đầu tiên:")
print(average_close.head())
