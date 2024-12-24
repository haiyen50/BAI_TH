
import pandas as pd

# 1. Đọc file stocks1.csv vào DataFrame stocks1
stocks1 = pd.read_csv("D:\DHKL17A3HN\lab 3\stocks1.csv")

# 2. Hiển thị 5 dòng đầu tiên của stocks1
print("5 dòng đầu tiên của stocks1:")
print(stocks1.head())

# 3. Hiển thị kiểu dữ liệu (dtype) của mỗi cột trong stocks1
print("\nKiểu dữ liệu (dtype) của mỗi cột trong stocks1:")
print(stocks1.dtypes)

# 4. Xem thông tin tổng quan (info) của stocks1
print("\nThông tin tổng quan (info) của stocks1:")
stocks1.info()




