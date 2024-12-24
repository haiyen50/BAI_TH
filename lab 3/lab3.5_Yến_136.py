import pandas as pd

stocks1 = pd.read_csv("D:\DHKL17A3HN\lab 3\stocks1.csv")
# 1. Đọc file stocks2.csv vào DataFrame stocks2
stocks2 = pd.read_csv(r"D:\DHKL17A3HN\lab 3\stocks2.csv")

# 2. Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks = pd.concat([stocks1, stocks2], ignore_index=True)


# 1. Tạo MultiIndex cho DataFrame stocks bằng cột date và symbol làm chỉ mục
stocks.set_index(['date', 'symbol'], inplace=True)

# 2. Sử dụng GroupBy để tính giá trung bình (open, high, low, close) và volume trung bình
grouped_stocks = stocks.groupby(['date', 'symbol']).mean()

# 3. Sắp xếp dữ liệu theo ngày và mã chứng khoán
grouped_stocks.sort_index(level=['date', 'symbol'], inplace=True)

# 4. Hiển thị kết quả cho 5 ngày đầu tiên
print("Kết quả cho 5 ngày đầu tiên:")
print(grouped_stocks.head())
