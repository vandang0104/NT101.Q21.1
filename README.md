---Bài 2.1 Sử dụng Frequency Analysis
Logic: Lấy tần suất của từ xuất hiện nhiều nhất trong input - tần suất xuất hiện từ trong tiếng anh từ lớn tới thấp để + 26 % 26. Xét từng trường hợp để xem đoạn text nào có ý nghĩa nhất thì dừng chương trình

--- Bài 2.2  mono-alphabetic substitution cipher
Ý tưởng :  Sử dụng pp Phân Tích tần suất thay vì brute force. Ta thống kê các chữ cái xuất hiện nhiều nhất trong bản mã và so sánh với từ xuất hiện nhiều nhất trong từ điển tiếng anh cứ thế giảm dần theo tần suất trong từ điển, đến khi gặp đoạn text đọc được thì dừng lại
---Bai2.4 Fairplay
Logic:
- Tạo matrix key bằng cách thêm key vào 1 string và đánh dấu từng chữ cái đã xuất hiện vào 1 set, sau đó đẩy các chữ cái còn lại vào đồng thời kiểm tra chữ cái đó đã xuất hiện chưa. Cuối cùng đẩy vào mảng 5x5
- Tạo pair bằng cách lọc qua text nếu có chữ cái trùng thì thêm X vào giữa 2 chữ đó. Đến cuối nếu text length = lẻ thì thêm X vào cuối
-Tạo cipher text bằng cách xét 3 trường hợp nếu cùng hàng thì lấy bên phải, cùng cột thì lấy bên dưới (nếu lớn hơn 5 thì %5). Nếu không thuộc 2 trường hợp trên thì đổi chỉ số cột trong matrix của 2 kí tự cho nhau
--- Bài 2.5 mã hóa  Vigenère
Logic : là sự mở rộng của mã hóa Caesar, nhưng thay vì dùng một độ dời cố định, chúng ta dùng một chuỗi độ dời - khóa lặp lại
B1 : Làm sạch input
- Xóa các dấu câu và khoảng trắng
- Viết hoa toàn bộ
B2 : Logic lặp khóa
-	 Sử dụng phép toán chia lấy dư với độ dài khóa m
-	Công thức: key x [i % m]. Khi chỉ số i tăng vượt quá độ dài khóa, phép % m sẽ đưa nó quay lại từ đầu , giúp khóa tự động lặp lại cho đến khi hết văn bản
B3: Hàm mã hóa và giải mã
-	Xoay vòng khóa: Dùng phép toán % để lặp lại khóa cho đến khi hết văn bản.
-	Biến đổi số: Đưa chữ cái về dạng số (0-25) rồi thực hiện phép tính:
+Mã hóa: Cộng giá trị bản rõ với khóa.
+Giải mã: Trừ giá trị khóa khỏi bản mã (cộng thêm 26 để tránh số âm).
-	Kết quả: Lấy dư cho 26 để kết quả luôn nằm trong bảng chữ cái và chuyển ngược lại thành ký tự.
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

---Bai2.7 Encrypt và Decrypt bằng Affine Encryption
Logic: 
Mã hóa plaintext theo công thức
    E(x) = (a * x + b) mod 26
    Với K(a,b) là key trong đó a là số có ước chung lớn nhất với 26 = 1 
    x là chữ cái

Giải mã cipher text theo công thức 
    D(y) = a^-1 * (y - b) mod 26
    Với K(a,b) là key trong đó a là số có ước chung lớn nhất với 26 = 1 
    y là chữ cái

Các bước thực thi:
* B1: Chọn key 
Giả sử chọn K(5,8)
- Kiểm tra gcd(5,26) = 1 hợp lệ 
- Tìm nghịch đảo của a module cho 26 là 21 
Vì sao lại chọn là 21 với a là 5 vì theo công thức 
nếu theo toán học bình thường để 1/5 thì sẽ không giải mã được vì nó là số thập phân

mà theo công thức D(y) = a^-1 * (y - b) mod 26
<=> D(y) = a^-1 * ((a * x + b) - b) mod 26
<=> D(y) = (a^-1 * a) * x mod 26
cần tìm (a^-1 * a) mod 26 = 1 thì mới thỏa x = x 
nên ta duyệt từ 1 với 26 để tìm ra số thỏa là được 
* B2: Mã hóa
Lấy chỉ số của từng chữ cái thay vào công thức tìm ra chỉ số của chữ cái sau khi mã hóa
* B3: Giải mã
Lấy chỉ số của từng chữ cái thay vào công thức tìm ra chỉ số của chữ cái sau khi giải mã (nên nhớ phải tìm a^-1 trước bằng hàm modInverse)
