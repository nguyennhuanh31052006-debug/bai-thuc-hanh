# Nguyễn Nhu Anh, mssv 245752021610144
# bài 14: Sắp xếp các phần tử trong list

# dùng để sắp xếp chữ cái
ds = input('nhập danh sách: ').split()
# Hàm .sort()dùng để sắp xếp trực tiếp các phần tử trong list theo thứ tự tăng dần
ds.sort()
for kc in ds:
    print(kc)

    # sắp xếp số
ds_so = input('nhập số cách nhau bằng dấu cách: ').split()
ds_so_moi = []
for i in ds_so:
    ds_so = int(i)
    ds_so_moi.append(ds_so)
ds_so_moi.sort()
for e in ds_so_moi:
    print(e)
