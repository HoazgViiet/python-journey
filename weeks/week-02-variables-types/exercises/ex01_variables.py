"""
Bài tập 01: Biến trong Python 📦
=================================
Mục tiêu: Hiểu cách khai báo và sử dụng biến
"""

# TODO 1: Tạo 4 biến lưu thông tin cá nhân
ten = "Nguyen Van An"       # str
tuoi = 20                   # int
diem_tb = 8.5               # float
dang_hoc = True             # bool

print(f"ten = {ten}, type = {type(ten).__name__}")
print(f"tuoi = {tuoi}, type = {type(tuoi).__name__}")
print(f"diem_tb = {diem_tb}, type = {type(diem_tb).__name__}")
print(f"dang_hoc = {dang_hoc}, type = {type(dang_hoc).__name__}")


# TODO 2: Hoán đổi giá trị 2 biến KHÔNG dùng biến tạm
a = 10
b = 20
a, b = b, a
print(f"Sau hoán đổi: a = {a}, b = {b}")


# TODO 3: Augmented assignment
# Cho x = 100. Dùng +=, -=, *=, //= để biến đổi x qua 4 bước
x = 100
x += 20
print(f"Sau += 20: {x}")
x -= 10
print(f"Sau -= 10: {x}")
x *= 2
print(f"Sau *= 2: {x}")
x //= 5
print(f"Sau //= 5: {x}")


# TODO 4 (Thử thách): Multiple assignment
ho, ten_dem_va_ten, tuoi = "Nguyen", "Van An", 20
print(f"Họ tên: {ho} {ten_dem_va_ten}, {tuoi} tuổi")
