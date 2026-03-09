---Bài 2.1 Sử dụng Frequency Analysis
Logic: Lấy tần suất của từ xuất hiện nhiều nhất trong input - tần suất xuất hiện từ trong tiếng anh từ lớn tới thấp để + 26 % 26. Xét từng trường hợp để xem đoạn text nào có ý nghĩa nhất thì dừng chương trình

---Bai2.4 Fairplay
Logic:
- Tạo matrix key bằng cách thêm key vào 1 string và đánh dấu từng chữ cái đã xuất hiện vào 1 set, sau đó đẩy các chữ cái còn lại vào đồng thời kiểm tra chữ cái đó đã xuất hiện chưa. Cuối cùng đẩy vào mảng 5x5
- Tạo pair bằng cách lọc qua text nếu có chữ cái trùng thì thêm X vào giữa 2 chữ đó. Đến cuối nếu text length = lẻ thì thêm X vào cuối
-Tạo cipher text bằng cách xét 3 trường hợp nếu cùng hàng thì lấy bên phải, cùng cột thì lấy bên dưới (nếu lớn hơn 5 thì %5). Nếu không thuộc 2 trường hợp trên thì đổi chỉ số cột trong matrix của 2 kí tự cho nhau