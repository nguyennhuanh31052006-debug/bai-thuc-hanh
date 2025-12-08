# Nguyễn Nhu Anh, mssv 245752021610144
"""11.Biết lãi suất tiết kiệm là t%/tháng (nhập t từ bàn phím). Nhập số vốn ban đầu n và
số tháng gửi k. Tính số tiền nhận được sau k tháng sử dụng cấu trúc hàm
def benefit(t,n,k):
"""

def benefit(t, n, k):
    return n * (1 + t/100) **k
t = float(input('nhập lãi suất (%/tháng): '))
n = float(input('nhập số vốn ban đầu: '))
k = int(input('nhập số tháng gửi: '))

tong_tien = benefit(t, n, k)
print('số tiền nhận được sau {k} tháng là: ', float(tong_tien))
