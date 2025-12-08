# Nguyễn Nhu Anh, mssv 245752021610144
"""3. Tìm và sửa lỗi chương trình
def say_hello():
 a = "Hello"
 print(a)
print(a)
"""
# chương trình trên a nằm bên trong hàm nên a là biến cục bộ
# vì thế câu lệnh bên ngoài là print(a) là sai vì a ko tồn tại bên ngoài hàm
# ==> sửa

def say_hello():
    a = "Hello"
    print(a)

say_hello()
