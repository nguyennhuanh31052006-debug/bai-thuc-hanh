# Nguyễn Nhu Anh, mssv 245752021610144
"""3. Chỉnh sửa ví dụ ở bài 1: hãy các kí tự ở dạng IN HOA. """
S = input('nhap chuoi: ')
for ch in S:
    if ch not in [' ', '\t']:
        ch = ch.upper() #lệnh .upper là lệnh chuyển snag chữ in hoa
        print(ch)

        
