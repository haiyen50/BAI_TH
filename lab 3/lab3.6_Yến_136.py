# import pandas as pd

# stocks1 = pd.read_csv("D:\DHKL17A3HN\lab 3\stocks1.csv")
# # 1. Đọc file stocks2.csv vào DataFrame stocks2
# stocks2 = pd.read_csv(r"D:\DHKL17A3HN\lab 3\stocks2.csv")

# # 2. Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
# stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# # 1. Tạo Pivot Table từ DataFrame stocks với date làm chỉ mục, symbol làm cột, và giá trị trung bình của close làm giá trị
# pivot_table = stocks.pivot_table(values='close', index='date', columns='symbol', aggfunc='mean')

# # 2. Tính tổng volume giao dịch cho mỗi mã chứng khoán (symbol) và thêm cột này vào Pivot Table
# total_volume = stocks.groupby('symbol')['volume'].sum()

# # 3. Ánh xạ total_volume vào Pivot Table bằng cách sử dụng `pivot_table.columns`
# pivot_table['total_volume'] = pivot_table.columns.map(total_volume)

# # 4. Sắp xếp Pivot Table dựa trên tổng volume giao dịch, từ cao xuống thấp
# pivot_table_sorted = pivot_table.sort_values(by='total_volume', axis=1, ascending=False)

# # 5. Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất
# print("5 mã chứng khoán có tổng volume giao dịch cao nhất:")
# print(pivot_table_sorted.head())

import pandas as pd

# Đọc dữ liệu từ file
stocks1 = pd.read_csv("D:\\DHKL17A3HN\\lab 3\\stocks1.csv")
stocks2 = pd.read_csv(r"D:\\DHKL17A3HN\\lab 3\\stocks2.csv")

# Gộp hai DataFrame lại thành một
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# Tạo Pivot Table
pivot_table = stocks.pivot_table(values='close', index='date', columns='symbol', aggfunc='mean')

# Tính tổng volume cho mỗi mã chứng khoán
total_volume = stocks.groupby('symbol')['volume'].sum()

# Thêm tổng volume vào như một dòng trong Pivot Table
pivot_table.loc['total_volume'] = pivot_table.columns.map(total_volume)

# Sắp xếp các cột của Pivot Table theo tổng volume giao dịch giảm dần
pivot_table_sorted = pivot_table.sort_values(by='total_volume', axis=1, ascending=False)

# Hiển thị kết quả 5 mã chứng khoán có tổng volume giao dịch cao nhất
print("5 mã chứng khoán có tổng volume giao dịch cao nhất:")
print(pivot_table_sorted.head())

