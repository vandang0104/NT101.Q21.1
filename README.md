---Bài 2.1 Sử dụng Frequency Analysis
Logic: Lấy tần suất của từ xuất hiện nhiều nhất trong input - tần suất xuất hiện từ trong tiếng anh từ lớn tới thấp để + 26 % 26. Xét từng trường hợp để xem đoạn text nào có ý nghĩa nhất thì dừng chương trình

---Bai2.4 Fairplay
Logic:
- Tạo matrix key bằng cách thêm key vào 1 string và đánh dấu từng chữ cái đã xuất hiện vào 1 set, sau đó đẩy các chữ cái còn lại vào đồng thời kiểm tra chữ cái đó đã xuất hiện chưa. Cuối cùng đẩy vào mảng 5x5
- Tạo pair bằng cách lọc qua text nếu có chữ cái trùng thì thêm X vào giữa 2 chữ đó. Đến cuối nếu text length = lẻ thì thêm X vào cuối
-Tạo cipher text bằng cách xét 3 trường hợp nếu cùng hàng thì lấy bên phải, cùng cột thì lấy bên dưới (nếu lớn hơn 5 thì %5). Nếu không thuộc 2 trường hợp trên thì đổi chỉ số cột trong matrix của 2 kí tự cho nhau

---Bai2.6 Decrypt VIGENERE Encryption
Logic:
B1: Làm sạch input
- Xóa các dấu câu và khoảng trắng
- Viết hoa toàn bộ
B2: Tìm key (dùng IoC)
- Chương trình giả định độ dài khóa L từ 1 - 20
- Với mỗi L, cắt bản mã thành L cột
- Tính IoC trung bình của các cột
- Chọn L cho giá trị IoC gần với 0.065 nhất
B3: Tìm từng chữ cái của khóa
- Dùng lại cách chia thành L cột như bước 2
- Với mỗi cột, chương trình dịch chuyển chữ cái 26 lần
- TÍnh điểm X^2 để so sánh tuần xuất chữ cái của cột sau khi dịch với tần suất chuẩn của tiếng anh
- Độ dịch chuyển có X^2 min là chữ cái đúng của cột đó. Ghép L chữ cái tại, ta có Key
B4: Giải mã
- Lấy khóa vừa tìm được áp dụng giải thuật Vigenere tìm ra plaintext