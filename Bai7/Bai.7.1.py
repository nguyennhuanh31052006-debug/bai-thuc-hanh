file_path = 'a.txt'  

content = """Hello
Python
GPT
   trailing space   
"""


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Đã tạo file ví dụ tại:", file_path)
print("Nội dung file:")
print(content)
print("="*40)
