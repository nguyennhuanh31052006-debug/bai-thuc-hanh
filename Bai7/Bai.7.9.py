import os

source_file = "students.txt"
destination_file = "students_copy.txt"

## BƯỚC 1: KIỂM TRA SỰ TỒN TẠI CỦA FILE NGUỒN
if not os.path.exists(source_file):
    print(f"⚠️ Cảnh báo: File nguồn '{source_file}' không tồn tại. Đang tạo file mẫu...")
    
    # Tạo file mẫu với nội dung đơn giản
    try:
        with open(source_file, 'w', encoding='utf-8') as f_sample:
            f_sample.write("Mã sinh viên, Tên sinh viên\n")
            f_sample.write("SV001, Nguyễn Văn A\n")
            f_sample.write("SV002, Lê Thị B\n")
        print(f"✅ Đã tạo file '{source_file}' thành công.")
    except IOError as e:
        print(f"❌ Lỗi khi tạo file '{source_file}': {e}")
        # Dừng chương trình nếu không thể tạo file nguồn
        exit() 

## BƯỚC 2: SAO CHÉP NỘI DUNG (Phần code của bạn)
try:
    with open(source_file, "r", encoding="utf-8") as src, open(destination_file, "w", encoding="utf-8") as dest:
        content = src.read()
        dest.write(content)
        
    print(f"\n✅ Đã sao chép nội dung từ '{source_file}' sang '{destination_file}' thành công.")
    print("Nội dung trong tệp sao chép:")
    
    # In nội dung file đích (destination_file)
    with open(destination_file, "r", encoding="utf-8") as f:
        print(f.read())
        
except Exception as e:
    print(f"❌ Lỗi trong quá trình sao chép: {e}")
