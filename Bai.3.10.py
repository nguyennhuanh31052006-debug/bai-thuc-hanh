# Nguyễn Nhu Anh, mssv 245752021610144
"""10. Viết hàm “def Tinh(R):” tính chu vi và diện tích hình tròn, với bán kính R được
nhập từ bàn phím, và kiểm tra giá trị bán kính đầu vào là hợp lệ.
Gợi ý: sử dụng thư viện “import math” và math.pi cho số pi nếu cần"""
import math
def Tinh_ChuVi_DienTich():
    # 1. Nhập và kiểm tra tính hợp lệ của bán kính R
    while True:
            # Nhận giá trị nhập từ bàn phím
            R_input = input("Nhập bán kính R của hình tròn: ")
            # Chuyển đổi sang số thực (float)
            R = float(R_input)
            # Kiểm tra R phải là số dương
            if R <= 0:
                print("Lỗi: Bán kính phải là số dương.")
                continue 
            break   
    # Công thức Chu vi: C = 2 * pi * R
    chu_vi = 2 * math.pi * R    
    # Công thức Diện tích: S = pi * R^2
    dien_tich = math.pi * (R ** 2)   
    print('chu vi hinh tron la: ', round(chu_vi)) # round làm tròn đến số dương gần nhất
    print('dien tich hin tron la: ', round(dien_tich)) 
Tinh_ChuVi_DienTich()
