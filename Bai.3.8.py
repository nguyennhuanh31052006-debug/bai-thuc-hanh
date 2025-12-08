# Nguyễn Nhu Anh, mssv 245752021610144
"""8. Một Robot di chuyển trong mặt phẳng bắt đầu từ điểm đầu tiên (0,0). Robot có thể
di chuyển theo hướng UP, DOWN, LEFT và RIGHT với những bước nhất định.
Dấu di chuyển của robot được đánh hiển thị như sau:
UP 5        # lên
DOWN 3      # xuống
LEFT 3      # trái
RIGHT 3     # phải
Các con số sau phía sau hướng di chuyển chính là số bước đi. Hãy viết chương
trình để tính toán khoảng cách từ vị trí hiện tại đến vị trí đầu tiên, sau khi robot đã
di chuyển một quãng đường. Nếu khoảng cách là một số thập phân chỉ cần in só
nguyên gần nhất."""

import math

# Khởi tạo vị trí ban đầu
pos = [0, 0]  # pos[0] = x, pos[1] = y

while True:
    s = input("Nhập lệnh di chuyển (ENTER để kết thúc): ")
    if not s:  # nếu người dùng chỉ nhấn Enter → dừng vòng lặp
        break

    movement = s.split()  # tách chuỗi thành ["UP", "5"]
    if len(movement) != 2:
        print("Lệnh không hợp lệ, hãy nhập dạng: DIRECTION steps")
        continue

    direction = movement[0].upper()  # chuyển sang chữ hoa để tránh lỗi
    try:
        steps = int(movement[1])
    except ValueError:
        print("Số bước phải là số nguyên!")
        continue

    # Cập nhật vị trí
    if direction == "UP":
        pos[1] += steps
    elif direction == "DOWN":
        pos[1] -= steps
    elif direction == "LEFT":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[0] += steps
    else:
        print("Hướng di chuyển không hợp lệ! Chỉ UP, DOWN, LEFT, RIGHT được phép.")

# Tính khoảng cách tới điểm gốc (0,0)
distance = math.sqrt(pos[0]**2 + pos[1]**2)

# In kết quả làm tròn số nguyên gần nhất
print("Khoảng cách tới điểm bắt đầu:", int(round(distance)))
