import pandas as pd

stocks1 = pd.read_csv("D:\DHKL17A3HN\lab 3\stocks1.csv")

# 1. Kiểm tra xem trong stocks1 có dữ liệu Null nào không
print("\nKiểm tra dữ liệu Null trong stocks1:")
print(stocks1.isnull().sum())

# 2. Thay thế dữ liệu Null ở cột 'high' bằng giá trị trung bình của cột 'high'
if stocks1['high'].isnull().sum() > 0:
    mean_high = stocks1['high'].mean()
    stocks1['high'].fillna(mean_high, inplace=True)

# 3. Thay thế dữ liệu Null ở cột 'low' bằng giá trị trung bình của cột 'low'
if stocks1['low'].isnull().sum() > 0:
    mean_low = stocks1['low'].mean()
    stocks1['low'].fillna(mean_low, inplace=True)

# 4. Hiển thị thông tin tổng quan để xác nhận không còn dữ liệu Null
print("\nThông tin tổng quan sau khi xử lý dữ liệu Null:")
stocks1.info()
