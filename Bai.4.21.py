# Nguyễn Nhu Anh, mssv 245752021610144
"""21.Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân
tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không. Sau đó in các số
chia hết cho 5 thành dãy phân tách bởi dấu phẩy"""
# Nhập chuỗi nhị phân, ví dụ: 0100,0011,1010,1001

chuoi = input("Nhập các số nhị phân 4 chữ số, cách nhau bằng dấu phẩy: ")
# Tách chuỗi thành danh sách
ds = chuoi.split(',')
# Tạo danh sách để chứa các số chia hết cho 5
chia_het_5 = []
# Duyệt từng phần tử trong danh sách
for so_nhi_phan in ds:
    # Chuyển nhị phân ",2" cốt lõi
    gia_tri = int(so_nhi_phan, 2)
    
    # Kiểm tra chia hết cho 5
    if gia_tri % 5 == 0:
        chia_het_5.append(so_nhi_phan)

# In ra kết quả (nối bằng dấu phẩy)
print(','.join(chia_het_5))
