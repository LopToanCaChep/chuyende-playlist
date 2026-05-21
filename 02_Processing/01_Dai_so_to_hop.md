## PHẦN A. KIẾN THỨC CẦN NHÓ́

## 1. Quy tắc cộng

Nếu một công việc nào đó có thể thực hiện theo $n$ hướng khác nhau, trong đó:
Hướng thứ 1 có $m_{1}$ cách thực hiện;
Hướng thứ 2 có $m_{2}$ cách thực hiện;
$\_\_\_\_$
Hướng thứ $n$ có $m_{n}$ cách thực hiện.
Khi đó, ta có $m_{1}+m_{2}+\ldots+m_{n}$ cách để hoàn thành công việc đã cho.

## 2. Quy tắc nhân

Nếu một công việc nào đó phải hoàn thành qua $n$ giai đoạn liên tiếp, trong đó:
Giai đoạn 1 có $m_{1}$ cách thực hiện;
Giai đoạn 2 có $m_{2}$ cách thực hiện;
$\_\_\_\_$
Giai đoạn $n$ có $m_{n}$ cách thực hiện.
Khi đó, ta có $m_{1} \cdot m_{2} \cdot \cdots \cdot m_{n}$ cách để hoàn thành công việc đã cho.

## 3. Hoán vị

Cho tập hợp $A$ gồm $n$ phần tử $\left(n \in \mathbb{N}^{*}\right)$.
Mỗi kết quả của sự sắp xếp thứ tự $n$ phần tử của tập hợp $A$ được gọi là một hoán vị của n phần tủ đó.

Kí hiệu $P_{n}$ là số các hoán vị của $n$ phần tử. Ta có: $P_{n}=n(n-1) \ldots 2 \cdot 1=n$ !.

## 4. Chỉnh họp

Cho tập hợp $A$ gồm $n$ phần tử và một số nguyên $k$ với $1 \leq k \leq n$.
Mỗi kết quả của việc lấy $k$ phần tử từ $n$ phần tử của tập hợp $A$ và sắp xếp chúng theo một thứ tự nào đó được gọi là một chỉnh hợp chập $k$ của $n$ phần tử đã cho.

Kí hiệu $A_{n}^{k}$ là số các chỉnh hợp chập $k$ của $n$ phần tử.
Ta có: $A_{n}^{k}=n(n-1) \ldots(n-k+1)$.

## 5. Tổ hợp

Cho tập hợp $A$ gồm $n$ phần tử và một số nguyên $k$ với $1 \leq k \leq n$.
Mỗi tập con gồm $k$ phần tử được lấy ra từ $n$ phần tử của $A$ được gọi là một tổ hợp chập $k$ của $n$ phần tử đó.

Kí hiệu $C_{n}^{k}$ là số tổ hợp chập $k$ của $n$ phần tử với $1 \leq k \leq n$. Ta có: $C_{n}^{k}=\frac{A_{n}^{k}}{k \text { ! }}$.

Quy ước: $0!=1 ; C_{n}^{0}=1$.
Với những quy ước trên, ta có: $C_{n}^{k}=\frac{n!}{k!(n-k)!}$ với $0 \leq k \leq n$.
Tính chất: $C_{n}^{k}=C_{n}^{n-k}(0 \leq k \leq n)$ và $C_{n-1}^{k-1}+C_{n-1}^{k}=C_{n}^{k}(1 \leq k<n)$.

Lưu ý:

1. Hoán vị $\left(\mathrm{P}_{\mathrm{n}}=\mathrm{n}!\right)$ dùng khi đề bài yêu cầu "sắp xếp tất cả" các phần tử
2. Chỉnh hợp $\left(A_{n}^{k}\right)$ dùng khi đề bài yêu cầu "chọn 1 phần nhỏ trong 1 tập hợp lớn" có quan trọng vai trò, thứ tự
3. Tổ hợp ( $C_{n}^{k}$ ) dùng khi đề bài yêu cầu "chọn 1 phần nhỏ trong 1 tập hợp lớn"

## PHẤN C. BÀI TẬP TRẮC NGHIỆM

## DÀNH CHO HỌC SINH TRUNG BİNH

Câu 1. Một công việc được hoàn thành bởi một trong hai hành động. Nếu hành động thứ nhất có $a$ cách thực hiện, hành động thứ hai có $b$ cách thực hiện (các cách thực hiện của cả hai hành động là khác nhau đôi một) thì số cách để hoàn thành công việc đó là:
A. $a b$.
B. $a+b$.
C. 1 .
D. $a-b$.

## Lời giải

Công việc được hoàn thành bởi một trong hai hành động độc lập. Theo quy tắc cộng, ta có $a + b$ cách để hoàn thành.

## Chọn B

Câu 2. Một công việc được hoàn thành bởi hai hành động liên tiếp. Nếu hành động thứ nhất có $a$ cách thực hiện và ứng với mỗi cách thực hiện hành động thứ nhất có $b$ cách thực hiện hành động thứ hai thì số cách để hoàn thành công việc đó là:
A. $a b$.
B. $a+b$.
C. $a b+1$.
D. $a+b+1$.

## Lời giải

Công việc phải trải qua 2 hành động liên tiếp. Theo quy tắc nhân, ta có $a \cdot b$ cách để hoàn thành.

## Chọn A

Câu 3. Bạn An đến thư viện trường để mượn một quyển sách Toán học hoặc Vật lí để đọc. Tại đó có 100 quyển sách Toán học và 120 quyển sách Vật lí. Bạn An có số cách chọn sách là:
A. 100 .
B. 120 .
C. 12000 .
D. 220 .

## Lời giải

Vì bạn An chỉ mượn 1 quyển sách nên có thể mượn sách Toán hoặc Vật lí. Theo quy tắc cộng, An có $100 + 120 = 220$ cách chọn.

## Chọn D

Câu 4. Cho $k, n$ là các số nguyên dương thoả mãn $n \geq k$. Trong các phát biểu sau, phát biểu nào đúng?
A. $A_{n}^{k} = n(n-1) \ldots(n-k+1)$.
B. $A_{n}^{k}=n(n-1) \ldots k$.
C. $A_{n}^{k}=\frac{n!}{(n-k)!k!}$.
D. $A_{n}^{k}=\frac{n!}{k!}$.

## Lời giải

Theo công thức tính số chỉnh hợp chập $k$ của $n$ phần tử, ta có: $A_{n}^{k} = \frac{n!}{(n-k)!} = n(n-1) \ldots(n-k+1)$.

## Chọn A

Câu 5. Cho tập hợp $A$ có $n$ phần tử ( $n \geq 1$ ) và số nguyên dương $k$ thoả mãn $k \leq n$. Một tổ hợp chập $k$ của $n$ phần tử là:
A. Tất cả kết quả của việc lấy $k$ phần tử từ $n$ phần tử của tập hợp $A$ và sắp xếp chúng theo một thứ tự nào đó.
B. Tất cả tập con gồm $k$ phần tử được lấy ra từ $n$ phần tử của tập hợp $A$.
C. Mỗi kết quả của việc lấy $k$ phần tử từ $n$ phần tử của tập hợp $A$ và sắp xếp chúng theo một thứ tự nào đó.
D. Mỗi tập con gồm $k$ phần tử được lấy ra từ $n$ phần tử của tập hợp $A$.

## Lời giải

Tổ hợp chập $k$ của $n$ phần tử là một tập con gồm $k$ phần tử được lấy ra từ $n$ phần tử của tập hợp $A$ (không phân biệt thứ tự).

## Chọn D

Câu 6. Cho $k, n$ là các số nguyên dương thoả mãn $n>k$. Trong các mệnh đề sau, phát biểu nào sai?
A. $C_{n}^{k}=C_{n}^{n-k}$.
B. $C_{n}^{k}=\frac{n!}{(n-k)!}$.
C. $C_{n}^{k}=\frac{n!}{(n-k)!k!}$
D. $C_{n}^{k}=C_{n-1}^{k-1}+C_{n-1}^{k}$

## Lời giải

Khẳng định sai là B. Công thức đúng của tổ hợp là $C_{n}^{k}=\frac{n!}{(n-k)!k!}$. Công thức ở đáp án B thực chất là của chỉnh hợp.

## Chọn B

Câu 7. Một đề thi trắc nghiệm có 10 câu hỏi, mỗi câu có 1 đáp án đúng trong 4 đáp án. Giả sử các đáp án được chọn ngẫu nhiên. Số khả năng làm đúng 4 câu trên 10 câu của đề thi đó là:
A. $C_{10}^{10}$.
B. $C_{10}^{4}$.
C. $3^{6} C_{10}^{4}$.
D. $3^{6} A_{10}^{4}$.

## Lời giải

## Chọn C

Mô̂i cách chọn 4 câu làm đúng trong 10 câu là một tổ hợp chập 4 của 10 phần tử nên số cách chọn là $C_{10}^{4}$.

Vì 6 câu còn lại làm sai mà có 3 đáp án sai mỗi câu nên số khả năng làm đúng 4 câu trên 10 câu của đề thi đó là $3 \cdot 3 \cdot 3 \cdot 3 \cdot 3 \cdot 3 \cdot C_{10}^{4}=3^{6} C_{10}^{4}$.

Câu 8. Có 5 nhà xe vận chuyển hành khách giữa Hà Nội và Hải Phòng. Số cách để một người đi từ Hà Nội tới Hải Phòng rồi sau đó quay lại Hà Nội bằng hai nhà xe khác nhau là
A. 5 .
B. 10 .
C. 15 .
D. 20 .

## Lời giải

Phân tích: Từ Hà Nội tới Hải Phòng, một hành khác có 5 cách chọn nhà xe. Để quay lại Hà Nội bằng một nhà xe khác thì hành khách có $5-1=4$ cách chọn. Như vậy, theo quy tắc nhân thì số cách đi là $5 \cdot 4=20$ (cách).

Chọn D
Câu 9. Số các số tự nhiên chẵn có ba chữ số, các chữ số đôi một khác nhau, được tạo thành từ các chữ số 1;2;3;4;5;6;7;8;9 là
A. 224 .
B. 280 .
C. 324 .
D. Không số nào trong các số đó.

## Lời giải

Phân tích: Một số có ba chữ số như vậy có dạng $\overline{a b c}$, với $a, b, c$ khác nhau, được chọn từ các chữ số $1 ; 2 ; 3 ; 4 ; 5 ; 6 ; 7 ; 8 ; 9$ và $c$ chỉ nhận một trong các giá trị $2 ; 4 ; 6 ; 8$. Ta có thể xây dựng một
số như vậy bằng cách trước hết chọn $c$, sau đó chọn ra hai chữ số có sắp thứ tự $a, b$ từ các chữ số còn lại. Có 4 cách chọn $c$. Sau đó, có $A_{8}^{2}=8 \cdot 7=56$ cách chọn $a, b$. Vì thế, theo quy tắc nhân, số các số có tính chất của bài toán là: $4 \cdot 56=224$ (số)

Chọn A
Câu 10. Số các số tự nhiên trong khoảng từ 3000 đến 4000 , chia hết cho 5 , các chữ số đôi một khác nhau, được tạo thành từ các chữ số $1 ; 2 ; 3 ; 4 ; 5 ; 6$ là
A. $C_{4}^{2}$.
B. $A_{4}^{2}$.
C. $A_{5}^{2}$.
D. $C_{6}^{4}$.

## Lời giải

Phân tích: Một số tự nhiên nằm trong khoảng từ 3000 đến 4000 và chia hết cho 5 và có các chữ số được tạo thành từ các chữ số $1 ; 2 ; 3 ; 4 ; 5 ; 6$ phải có chữ số hàng đơn vị là 5 và chữ số hàng nghìn là 3 . Như vậy các số thoả mãn yêu cầu của bài toán có dạng $\overline{3 a b 5}$, trong đó $a, b$ là 2 chữ số khác nhau chọn trong các chữ số $1 ; 2 ; 4 ; 6$. Số các bộ hai số khác nhau, có sắp thứ tự, lấy ra từ 4 số đó là $A_{4}^{2}$.

Chọn B
Câu 11. Cho số nguyên dương $n \geq 4$. Người ta đánh dấu $n$ điểm phân biệt trên một đường tròn. Biết rằng số các hình tam giác với các đỉnh là các điểm được đánh dấu thì bằng số các tứ giác với các đỉnh là các điểm được đánh dấu. Giá trị của $n$ là
A. 4 .
B. 6 .
C. 7 .
D. 9 .

## Lời giải

Phân tích: Mỗi tam giác cần đếm có 3 đỉnh là các điểm được đánh dấu. Đảo lại, mỗi bộ ba điểm được đánh dấu xác định một tam giác. Như vậy, số các tam giác với các điểm được đánh dấu bằng $C_{n}^{3}$.

Tương tự, số các tứ giác với các điểm được đánh dấu bằng $C_{n}^{4}$. Suy ra $C_{n}^{3}=C_{n}^{4}$, nghĩa là $\frac{n(n-1)(n-2)}{3 \cdot 2 \cdot 1}=\frac{n(n-1)(n-2)(n-3)}{4 \cdot 3 \cdot 2 \cdot 1}$. Điều này dẫn đến $n-3=4$, hay $n=7$.

Chọn C
Câu 12. Có 3 ứng viên cho 1 vị trí làm việc. Hội đồng tuyển dụng có 5 người, mỗi người bầu cho đúng 1 ứng viên. Số cách bầu của hội đồng là
A. $C_{5}^{3}$.
B. $5^{3}$.
C. $3^{5}$.
D. Không số nào trong các số đó.

## Lời giải

Phân tích: Mỗi thành viên của hội đồng có 3 cách bầu khác nhau. Số thành viên của hội đồng là 5. Như vậy, theo quy tắc nhân thì số cách bầu là $3 \cdot 3 \cdot 3 \cdot 3 \cdot 3=3^{5}$.

Chọn C
Câu 13. Các tỉnh $A, B, C, D$ được nối với nhau bởi các con đường như hình vẽ. Hỏi có bao nhiêu cách đi từ tỉnh $A$ đến $D$, mà chỉ qua $B$ và $C$ một lần?
![](https://cdn.mathpix.com/cropped/616b3f3c-0299-400e-94a4-204f36f4a211-04.jpg?height=145&width=714&top_left_y=2531&top_left_x=358)
A. 24 .
B. 36 .
C. 18 .
D. 28 .

## Lời giải

## Chọn C

Có 3 cách đi từ $A$ đến $B$.
Có 2 cách đi từ $B$ đến $C$.
Có 3 cách đi từ $C$ đến $D$.
Áp dụng quy tắc nhân ta có số cách đi từ tỉnh $A$ đến $D$, mà chỉ qua $B$ và $C$ một lần là 3.2.3 $=18$ (cách).

Câu 14. Có 3 kiểu đồng hồ đeo tay (vuông, tròn, elip) và 4 kiểu dây (kim loại, da, vải, nhựa). Hỏi có bao nhiêu cách chọn một chiếc đồng hồ gồm một mặt và một dây?
A. 4 .
B. 7 .
C. 12 .
D. 16 .

## Lời giải

## Chọn C

Áp dụng quy tắc nhân ta có số chọn một chiếc đồng hồ gồm một mặt và một dây là:
$3.4=12$ (cách).
Câu 15. Trên bàn có 8 cây bút chì khác nhau, 6 cây bút bi khác nhau và 10 cuốn tập khác nhau. Một học sinh muốn chọn một đồ vật duy nhất hoặc một cây bút chì hoặc một cây bút bi hoặc một cuốn tập thì số cách chọn khác nhau là
A. 480 .
B. 24 .
C. 48 .
D. 60 .

## Lời giải

## Chọn B

Áp dụng quy tắc cộng, số cách chọn một đồ vật duy nhất hoặc một cây bút chì hoặc một cây bút bi hoặc một cuốn tập thì số cách chọn khác nhau là: $8+6+10=24$

Câu 16. Một người vào cửa hàng ăn, người đó chọn thực đơn gồm một món ăn trong năm món, một loại quả tráng miệng trong năm loại quả tráng miệng và một nước uống trong ba loại nước uống. Có bao nhiêu cách chọn thực đơn.
A. 25 .
B. 75 .
C. 100 .
D. 15 .

## Lời giải

## Bhọn B

Chọn món ăn có 5 cách chọn.
Chọn quả tráng miệng có 5 cách chọn.
Chọn nước uống có 3 cách chọn.
Theo quy tắc nhân ta có: 5.5.3 = 75 cách chọn thực đơn.
Câu 17. Cửa hàng tiện lợi có bán combo bánh ngọt và đồ uống. Các loại bánh ngọt và đồ uống được mô tả bằng sơ đồ hình cây sau:
![](https://cdn.mathpix.com/cropped/616b3f3c-0299-400e-94a4-204f36f4a211-06.jpg?height=679&width=1066&top_left_y=114&top_left_x=408)

Hãy cho biết có bao nhiêu cách để khách hàng có thể lựa chọn được combo gồm một bánh ngọt và một loại đồ uống?
A. 20 .
B. 12 .
C. 3 .
D. 4 .

## Lời giải

## Chọn A

Số cách chọn 1 loại đồ ngọt và một loại đồ uống là: $C_{5}^{1} \cdot C_{4}^{1}=20$.
Câu 18. Một Ban chấp hành Đoàn trường có 12 người. Hỏi có bao nhiêu cách chọn 3 người vào ba chức vụ bí thư, phó bí thư và ủy viên từ ban chấp hành đó?
A. 1320 .
B. 220 .
C. 36 .
D. 15 .

## Lời giải

## Chọn A

Số cách chọn 3 người vào ba chức vụ bí thư, phó bí thư và ủy viên từ 12 người là $A_{12}^{3}=1320$.
Câu 19. Cho tập hợp $A=\{1 ; 2 ; 3 ; 4 ; 5\}$. Hỏi có bao nhiêu cách lập được số tự nhiên có năm chữ số khác nhau từ các chữ số thuộc tập hợp $A$ ?
A. 12 .
B. 120 .
C. 102 .
D. 210 .

## Lời giải

## Chọn B

Mỗi cách lập số tự nhiên có 5 chữ số khác nhau lấy từ $A$ là một hoán vị của 5 .
Vậy có $5!=120$ số tự nhiên.
Câu 20. Cho hai đường thẳng song song $a$ và $b$. Trên đường thẳng $a$ có 5 điểm phân biệt, trên đường thẳng $b$ có 7 điểm phân biệt. Tính số tam giác có 3 đỉnh lấy từ các điểm trên hai đường thẳng $a$ và $b$.
A. 220 tam giác.
B. 45 tam giác.
C. 350 tam giác.
D. 175 tam giác.

## Lời giải

## Đáp án D

Mỗi tam giác được lâp từ 3 điểm không thẳng hàng. Vì vậy số tam giác được lập là $C_{5}^{2} . C_{7}^{1}+C_{5}^{1} . C_{7}^{2}=175$
Câu 21. Cho hai số tự nhiên $k, n$ thỏa $1 \leq k \leq n$. Mệnh đề nào sau đây đúng?
A. $A_{n}^{k}=\frac{k!(n-k)!}{n!}$.
B. $A_{n}^{k}=\frac{n!}{k!(n-k)!}$.
C. $A_{n}^{k}=\frac{(n-k)!}{n!}$.
D. $A_{n}^{k}=\frac{n!}{(n-k)!}$.

## Lời giải

Theo định nghĩa, số chỉnh hợp chập $k$ của $n$ phần tử được tính bằng công thức: $A_{n}^{k}=\frac{n!}{(n-k)!}$.

## Đáp án $\underline{\mathbf{D}}$

Câu 22. Trường THPT Pleiku được cử một học sinh đi đại hội đoàn. Nhà trường quyết định chọn một đoàn viên 10 A 1 , hoặc lớp 11 A 1 . Hỏi nhà trường có bao nhiêu cách chọn, nếu biết rằng lớp 10 A 1 có 15 đoàn viên, $11 A 1$ có 23 đoàn viên?
A. 345 .
B. 31 .
C. 38 .
D. 70 .

## Lời giải

## Chọn C

Ta có số các chọn 1 đoàn viên đi dự đại hội Đoàn là $15+23=38$.
Câu 23. Một bộ cờ vua có 32 quân cờ. Bạn Nam lấy tất cả các quân cờ đen và tất cả các quân tốt. Số quân cờ Nam lấy ra là
A. 16 .
B. 34 .
C. 14 .
D. 24 .

## Lời giải

## Chọn D

Ta có Nam lấy cờ đen và tất cả các quân tốt là $16+8=24$.
Câu 24. Có 10 cây bút khác nhau và 8 quyển sách giáo khoa khác nhau. Một bạn học sinh cần chọn 1 cây bút và 1 quyển sách. Số cách chọn bạn học sinh đó là
A. 90 .
B. 80 .
C. 60 .
D. 70 .

## Lời giải

## Chọn B

Bài toán có 2 bước:
Bước 1: Chọn 1 cây bút: $C_{10}^{1}$ cách.
Bước 2: Chọn 1 quyển sách: $C_{8}^{1}$ cách.
Vậy $C_{10}^{1} C_{8}^{1}=80$ cách.
Câu 25. Lớp 10 A có 20 nam và 18 nữ. Giáo viên cần chọn ra 9 bạn gồm 5 bạn nam và 4 bạn nữ để lao động. Số cách chọn của giáo viên là
A. $C_{38}^{9}$.
B. $A_{20}^{5} \cdot A_{18}^{4}$.
C. $A_{38}^{9}$.
D. $C_{20}^{5} \cdot C_{18}^{4}$.

## Lời giải

## Dhọn D

Bài toán có 2 bước:
Bước 1: Chọn bạn nam có $C_{20}^{5}$ cách.
Bước 2: Chọn bạn nữ có $C_{18}^{4}$ cách.
Từ đó suy ra có $C_{20}^{5} \cdot C_{18}^{4}$ cách.
Câu 26. Một hộp chứa 3 quả cầu trắng và 5 quả đầu đen. Có bao nhiêu cách chọn ra 2 quả cầu sao cho có đủ hai màu?
A. 15 .
B. 45 .
C. 20 .
D. 56

## Lời giải

## Chọn A

Vì chọn ra 2 quả cầu sao cho có đủ hai màu nên mỗi màu chọn 1 quả.

Số cách chọn 1 quả cầu màu trắng trong 3 quả cầu trắng là $C_{3}^{1}$.
Số cách chọn 1 quả cầu màu đen trong 5 quả cầu đen là $C_{5}^{1}$.
Vậy có $C_{3}^{1} \cdot C_{5}^{1}=15$ cách chọn.
Câu 27. Từ một lớp gồm 16 học sinh nam và 18 học sinh nữ. Có bao nhiêu cách chọn ra 5 học sinh tham gia đội Thanh niên xung kích, trong đó có 2 học sinh nam và 3 học sinh nữ?
A. $C_{16}^{2} \cdot C_{18}^{3}$.
B. $A_{16}^{2} \cdot A_{18}^{3}$.
C. $C_{16}^{3} \cdot C_{18}^{2}$.
D. $A_{16}^{3} \cdot A_{18}^{2}$.

## Lời giải

Chọn 2 nam từ 16 nam có $C_{16}^2$ cách. Chọn 3 nữ từ 18 nữ có $C_{18}^3$ cách. Theo quy tắc nhân, ta có $C_{16}^2 \cdot C_{18}^3$ cách.

## Chọn C

Chọn 2 học sinh nam và 3 học sinh nữ từ 16 HS nam và 18 HS nữ là $C_{16}^{2} \cdot C_{18}^{3}$.
Câu 28. Số cách chia 10 học sinh thành ba nhóm lần lượt có $2,3,5$ học sinh là:
A. $C_{10}^{2} \cdot C_{8}^{3} \cdot C_{5}^{5}$.
B. $C_{10}^{2}+C_{10}^{3}+C_{10}^{5}$.
C. $C_{10}^{5}+C_{5}^{3}+C_{2}^{2}$.
D. $C_{10}^{2}+C_{8}^{3}+C_{5}^{5}$.

## Lời giải

## Chọn $\underline{\mathbf{A}}$

Số cách chọn 2 học sinh từ nhóm có 10 học sinh là $C_{10}^{2}$; số cách chọn 3 bạn từ nhóm gồm 8 bạn còn lại là $C_{8}^{3}$ và có $C_{5}^{5}$ cách chọn 5 bạn từ 5 bạn còn lại.

Số cách chia 10 học sinh thành ba nhóm lần lượt có $2,3,5$ học sinh là: $C_{10}^{2} \cdot C_{8}^{3} \cdot C_{5}^{5}$
Câu 29. Từ bảy chữ số $1,2,3,4,5,6,7$ có thể lập được bao nhiêu số tự nhiên có bốn chữ số khác nhau:
A. $7!.6!.5!.4!$.
B. 7 ! .
C. $7^{4}$.
D. 7.6.5.4.

## Lời giải

## Chọn D

Mô̂i số tự nhiên có bốn chữ số khác nhau lấy từ bảy chữ số trên là một chỉnh hợp chập 4 của bảy phần tử đó.

Số các số tự nhiên có bốn chữ số khác nhau là $A_{7}^{4}=7.6 .5$.4.
Câu 30. Một tổ có 6 học sinh nam và 9 học sinh nữ. Số cách chọn 6 học sinh đi lao động, trong đó có đúng 2 học sinh nam là:
A. $C_{6}^{2} \cdot C_{9}^{4}$.
B. $C_{6}^{2}+C_{9}^{4}$.
C. $A_{6}^{2} \cdot A_{9}^{4}$.
D. $C_{9}^{2} \cdot C_{6}^{4}$.

## Lời giải

## Chọn $\underline{\mathrm{A}}$

Số cách chọn 2 học sinh nam từ 6 học sinh nam là $C_{6}^{2}$.
Ta cần chọn thêm 4 học sinh nữa và 4 học sinh này đều phải là các học sinh nữ nên số cách chọn là $C_{9}^{4}$.

Vậy số cách chọn 6 học sinh đi lao động, trong đó có đúng 2 học sinh nam là $C_{6}^{2} \cdot C_{9}^{4}$.
Câu 31. Số cách sắp xếp 9 học sinh ngồi vào một dãy gồm 9 ghế là
A. 9 !.
B. 9 .
C. 1 .
D. $9^{9}$.

## Lời giải

## Chọn A

Số cách sắp xếp 9 học sinh ngồi vào một dãy gồm 9 ghế là 9 !.
Câu 32. Từ các chữ số $1,2,3,4,5,6$ lập được bao nhiêu số tự nhiên có 4 chữ số đôi một khác nhau và chia hết cho 5 ?
A. $A_{6}^{4}$.
B. $A_{5}^{3}$.
C. $C_{6}^{4}$.
D. $C_{5}^{3}$.

## Lời giải

## Chọn B

Ta lập ra số chia hết cho 5 nên chữ số hàng đơn vị có 1 cách chọn là chữ số 5 .
Để chọn chữ số hàng chục, hàng trăm, hàng nghìn trong 5 chữ số còn lại có $A_{5}^{3}$ cách chọn.
Số cách lập ra số thỏa mãn yêu cầu bài toán là: $1 . A_{5}^{3}=A_{5}^{3}$.
Câu 33. Từ một lớp gồm 16 học sinh nam và 18 học sinh nữ. Có bao nhiêu cách chọn ra 5 học sinh tham gia đội Thanh niên xung kích, trong đó có 2 học sinh nam và 3 học sinh nữ
A. $A_{16}^{2} \cdot A_{18}^{3}$.
B. $C_{16}^{2} \cdot C_{18}^{3}$.
C. $C_{16}^{2}+C_{18}^{3}$.
D. $A_{16}^{2}+A_{18}^{3}$.

## Lời giải

## Bhọn B

Công đoạn 1: Chọn 2 học sinh nam có $C_{16}^{2}$ cách.
Công đoạn 2: Chọn 3 học sinh nữ có $C_{18}^{3}$ cách.
Theo quy tắc nhân có $C_{16}^{2} \cdot C_{18}^{3}$ cách.
Câu 34. Một lớp có 30 học sinh gồm 20 nam và 10 nữ. Hỏi có bao nhiêu cách chọn ra một nhóm 3 học sinh sao cho nhóm đó có ít nhất một học sinh nữ?
A. 1140 .
B. 2920 .
C. 1900 .
D. 900 .

## Lời giải

## Bhọn B

Số cách chọn 3 học sinh tùy ý là: $C_{30}^{3}$
Số cách chọn 3 học sinh không có nữ là: $C_{20}^{3}$
Suy ra số cách chọn 3 học sinh có ít nhất 1 nữ là: $C_{30}^{3}-C_{20}^{3}=2920$.
Câu 35. Có 4 cuốn sách Toán khác nhau và 3 cuốn sách Văn khác nhau. Cần xếp các cuốn sách lên kệ thành một dãy sao cho các cuốn sách cùng loại thì đặt gần nhau. Hỏi có bao nhiêu cách xếp?
A. $4!3!$.
B. $5!3!+4!4!$.
C. $2!4!3!$.
D. 7!.

## Lời giải

## Chọn C

Ta xếp 4 cuôn sách toán khác nhau có 4 !.
Ta xếp 3 cuốn sách Văn khác nhau có 3 !
Ta xếp sách cùng loại thì đặt gần nhau có 2 !
Vậy có $2!4!3$ ! cách sắp xếp.
Câu 36. Một đội văn nghệ có 15 người gồm 7 nam, 8 nữ. Cần chọn ra 3 bạn nam và 3 bạn nữ để tập một tiết mục văn nghệ. Hỏi có bao nhiêu cách chọn?
A. $A_{7}^{3} \cdot A_{8}^{3}$.
B. $C_{7}^{3} \cdot C_{8}^{3}$.
C. $C_{7}^{3}+C_{8}^{3}$.
D. $C_{15}^{6}$.

## Lời giải

## Bhọn B

Cần chọn ra 3 bạn nam trong 7 bạn nam và 3 bạn nữ trong 8 bạn nữ,
Vậy số cách chọn $C_{7}^{3} \cdot C_{8}^{3}$.
Câu 37. Từ các chữ số $1,2,3$ có thể lập được bao nhiêu số tự nhiên có các chữ số khác nhau?
A. 12 .
B. 15 .
C. 27 .
D. 6 .

## Lời giải

## Chọn B

Trường hợp 1: số tự nhiên có 1 chữ số khác nhau có 3 cách chọn
Trưởng hợp 2: số tự nhiên có 2 chữ số khac nhau có $A_{3}^{2}=6$ cách chọn
Trưởng hợp 3: số tự nhiên có 3 chữ số khac nhau có $P=3!=6$ cách chọn
Vậy có tất cả: $3+6+6=15$ cách chọn.
Câu 38. Một lớp học 20 học sinh. Có bao nhiêu cách chọn ra một ban cán sự gồm 1 lớp trưởng, 1 lớp phó và 4 tổ trưởng biết rằng tất cả các học sinh đều có khả năng như nhau và mỗi bạn học sinh chỉ làm một nhiệm vụ.
A. $6 C_{20}^{6}$.
B. $C_{20}^{6}$.
C. $380 C_{20}^{4}$.
D. $A_{20}^{6}$.

## Lời giải

## Dhọn D

Số cách chọn ra một ban cán sự gồm 1 lớp trưởng, 1 lớp phó và 4 tổ trưởng biết rằng tất cả các học sinh đều có khả năng như nhau và mỗi bạn học sinh chỉ làm một nhiệm vụ là $A_{20}^{6}$ cách.

Câu 39. Một nhóm có 10 học sinh gồm 4 nam và 6 nữ. Hỏi có bao nhiêu cách chọn ra 3 học sinh trong đó có cả nam và nữ.
A. 10 .
B. 56 .
C. 336 .
D. 96.

## Lời giải

## Dhọn D

TH1: 2 nam, 1 nữ có $C_{4}^{2} \cdot C_{6}^{1}=36$ ( cách)
TH2: 1 nam, 2 nữ có $C_{4}^{1} \cdot C_{6}^{2}=60$ ( cách)
Vậy có: $30+60=96$ (cách).

## DÀNH CHO HỌC SINH KHÁ GIỎI

Câu 40. Tại một cuộc họp của học sinh các lớp $10 A, 10 B, 10 C, 10 D$ và $10 E$, ban tổ chức đề nghị đại diện của mỗi lớp trình bày một báo cáo. Bạn đại diện của lớp 10 A đề nghị được trình bày báo cáo ngay trước đại diện của lớp $10 B$ và được ban tổ chức đồng ý. Số cách xếp chương trình là
A. 24 .
B. 36 .
C. 48 .
D. 30 .

## Lời giải

Phân tích: Kí hiệu thứ tự các bài báo cáo là $1,2,3,4,5$. Có 4 phương án xếp báo cáo của đại diện của lớp $10 ~ B$ ngay sau báo cáo đại diện của $10 ~ A$ là:

- Phương án $1: 10 \mathrm{~A}$ báo cáo $1,10 B$ báo cáo 2 ;
- Phương án 2: 10A báo cáo $2,10 B$ báo cáo 3 ;
- Phương án 3: 10A báo cáo $3,10 B$ báo cáo 4 ;
- Phương án 4: $10 ~ A$ báo cáo $4,10 ~ B$ báo cáo 5 .

Đối với mỗi phương án, ban tổ chức có thể xếp đại diện của các lớp $10 \mathrm{C}, 10 D$ và $10 E$ theo thứ tự bất kì vào vị trí các báo cáo còn lại. Do đó, với mỗi phương án thì số cách xếp là: $P_{3}=3!=3 \cdot 2 \cdot 1=6($ cách $)$

Như vậy, theo quy tắc cộng thì số cách xếp chương trình là: $6+6+6+6=24$ (cách)
Chọn A
Câu 41. Người ta muốn thành lập một uỷ ban gồm 6 thành viên, trong đó có ít nhất 3 thành viên nữ từ một nhóm đại biểu gồm 6 nam và 4 nữ. Số các cách thành lập uỷ ban như vậy là
A. 100 .
B. 210 .
C. 60 .
D. 95 .

## Lời giải

Phân tích: Do chỉ có 4 đại biểu nữ nên có 2 phương án:

- Phương án 1: uỷ ban gồm 3 nữ và 3 nam;
- Phương án 2: uỷ ban gồm 4 nữ và 2 nam.

Đối với phướng án 1: số cách chọn ra 3 người từ 4 đại biểu nữ là: $C_{4}^{3}=\frac{4 \cdot 3 \cdot 2}{3 \cdot 2 \cdot 1}=4$ (cách)
Số cách chọn ra 3 người từ 6 đại biểu nam là: $C_{6}^{3}=\frac{6 \cdot 5 \cdot 4}{3 \cdot 2 \cdot 1}=20$ (cách)
Như vậy, theo quy tắc nhân thì số cách chọn theo phương án 1 là: $4 \cdot 20=80$ (cách)
Đối với phương án 2: chỉ có duy nhất 1 cách chọn ra 4 người từ 4 đại biểu nữ (nghĩa là cả 4 đại biểu nữ sẽ nằm trong uỷ ban cần lập). Ngoài ra, số cách chọn ra 2 người từ 6 đại biểu nam là:
$C_{6}^{2}=\frac{6 \cdot 5}{2 \cdot 1}=15($ cách $)$
Do đó, có đúng 15 cách chọn theo phương án 2 .
Từ đó, theo quy tắc cộng thì số các cách thành lập uỷ ban là: $80+15=95$ (cách)
Chọn D
Câu 42. Có 3 cặp vợ chồng mua 6 vé xem phim với các chỗ ngồi liên tiếp nhau trên cùng một hàng ghế. Số cách xếp chỗ ngồi sao cho mỗi cặp vợ chồng đều ngồi cạnh nhau là
A. 24 .
B. 36 .
C. 48 .
D. 120 .

## Lời giải

Phân tích: Trước hết, xét mỗi cặp vợ chồng như là một khối. Số cách xếp 3 khối vào 3 vị trí là $P_{3}=3!=3 \cdot 2 \cdot 1=6$. Bây giờ', với mỗi cách xếp như vậy, mỗi cặp vợ chồng (của một khối) có thể đổi chỗ cho nhau để có một cách xếp mới. Như vậy, tổng số cách xếp chỗ cho 6 người với yêu cầu của bài toán là: $6 \cdot 2 \cdot 2 \cdot 2=48$ (cách)

Chọn C
Câu 43. Từ các chữ số $0,1,2,3,4,5,6$ lập các số tự nhiên chia hết cho 5 trong đó mỗi số có 4 chữ số đôi một khác nhau.
A. 120 .
B. 100 .
C. 220.
D. 200 .

## Lời giải

## Chọn C

Gọi số tự nhiên có 4 chữ số là $\overline{a b c d},(a \neq 0)$.
Tổng quát:
+) $d$ có 2 cách chọn.
+) a có 6 cách chọn.
+) $b$ có 5 cách chọn.
+) $c$ có 4 cách chọn.
Quy tắc nhân: 2.6.5.4 = 240 số.
Vi phạm:
+) $a=0$ có 1 cách chọn.
+) $d=5$ có 1 cách chọn.
+) $b$ có 5 cách chọn.
+) $c$ có 4 cách chọn.
Quy tắc nhân: 1.1.5.4 = 20 số.
Số các số cần tìm: $240-20=220$ số.
Câu 44. Một lớp học có 30 học sinh gồm 20 nam và 10 nữ. Hỏi có bao nhiêu cách chọn ra một nhóm 3 học sinh sao cho trong nhóm đó có ít nhất một học sinh nam?
A. 4060 .
B. 23640 .
C. 22920 .
D. 3940.

## Lời giải

## Dhọn D

Chọn ra 3 học sinh bất kì có $C_{30}^{3}$ cách.
Chọn ra 3 học sinh không có học sinh nam nào có $C_{10}^{3}$ cách.
Vậy để chọn ra một nhóm 3 học sinh sao cho trong nhóm đó có ít nhất một học sinh nam có $C_{30}^{3}-C_{10}^{3}=3940$ cách.
Câu 45. Lớp 10 C có 40 học sinh trong đó có 18 nam và 22 nữ. Giáo viên chủ nhiệm cần chọn 3 học sinh để trực an toàn giao thông gồm 2 nam và 1 nữ. Hỏi giáo viên chủ nhiệm có bao nhiêu cách chọn?
A. 175 .
B. 9880 .
C. 3366 .
D. 4158 .

## Lời giải

## Chọn C

Công đoạn 1: Chọn 2 học sinh nam từ 18 học sinh nam: có $C_{18}^{2}$ cách.
Công đoạn 2: Chọn 1 học sinh nam từ 22 học sinh nam: có $C_{22}^{1}$ cách.
Theo quy tắc nhân ta có: $C_{18}^{2} \cdot C_{22}^{1}=3366$ cách.
Câu 46. Cho tập hợp $A=\{1 ; 2 ; 3 ; 4 ; 5 ; 6 ; 7\}$. Hỏi từ tập $A$ có thể lập được bao nhiêu số tự nhiên có 6 chữ số khác nhau và phải có mặt các chữ số $1,2,3$ sao cho chúng không đứng cạnh nhau?
A. 567 .
B. 576 .
C. 5040 .
D. 840 .

## Lời giải

## Chọn B

Lấy ra 3 chữ số khác $1,2,3$ từ tập A có $C_{4}^{3}$ cách.
Xếp 3 chữ số này có 3 ! cách, coi 3 số trên là 3 vách ngăn sẽ tạo ra 4 vị trí xếp 3 chữ số 1, 2, 3 vào 3 trong 4 vị trí đó có $A_{4}^{3}$ cách.

Vậy số các số lập được là: $C_{4}^{3} \cdot 3!\cdot A_{4}^{3}=576$.
Câu 47. Một nhóm học sinh gồm 12 nam và 6 nữ. Người ta muốn chọn từ nhóm ra 5 người để lập thành một đội cờ đỏ sao cho phải có 1 đội trưởng nam, 1 đội phó nam và có ít nhất 1 nữ. Hỏi có bao nhiêu cách lập đội cờ đỏ.
A. 572 .
B. 1028160 .
C. 8568 .
D. 58080 .

## Lời giải

## Chọn D

Số cách chọn nhóm ra 5 người để lập thành một đội cờ đỏ sao cho phải có 1 đội trưởng nam, 1 đội phó nam và 3 người bất kỳ trong 16 người còn lại là $A_{12}^{2} \cdot C_{16}^{3}$ (cách)

Số cách chọn nhóm ra 5 người để lập thành một đội cờ đỏ sao cho phải có 1 đội trưởng nam, 1 đội phó nam và 3 người còn lai không có nữ là $A_{12}^{2} \cdot C_{10}^{3}$ (cách)

Số cách chọn thỏa mãn yêu cầu đầu bài là $A_{12}^{2} \cdot C_{16}^{3}-A_{12}^{2} \cdot C_{10}^{3}=58080$ (cách)
Câu 48. Có 3 cặp vợ chồng mua 6 vé xem phim với các chỗ ngồi liên tiếp nhau trên cùng một hàng ghế. Số cách xếp chỗ ngồi sao cho mỗi cặp vợ chồng đều ngồi cạnh nhau là
A. 24 .
B. 48 .
C. 36 .
D. 120 .

## Lời giải

## Chọn B

Ta coi mỗi cặp vợ chồng là 1 người. Khi đó số cách xếp 3 cặp vợ chồng là 3 ! cách.
Số hoán vị vị trí của mỗi cặp vợ chồng là 2 ! cách.
Số cách xếp thỏa mãn là: $3!\cdot(2!)^{3}=48$ (cách).
Câu 49. Trong một giỏ hoa có 6 bông hồng vàng, 5 bông hồng trắng (các bông hoa coi như đôi một khác nhau). Người ta muốn làm một bó hoa gồm 5 bông được lấy từ giỏ hoa đó. Hỏi có bao nhiêu cách chọn hoa biết bó hoa có đủ 2 loại hoa hồng vàng và hoa hồng trắng?
A. 455 .
B. 7 .
C. 456 .
D. 462 .

## Lời giải

## Ahọn A

Chọn 1 bông vàng và 4 bông trắng $C_{6}^{1} \cdot C_{5}^{4}=30$.
Chọn 2 bông vàng và 3 bông trắng $C_{6}^{2} \cdot C_{5}^{3}=150$.
Chọn 3 bông vàng và 2 bông trắng $C_{6}^{3} \cdot C_{5}^{2}=200$.
Chọn 4 bông vàng và 1 bông trắng $C_{6}^{4} \cdot C_{5}^{1}=75$.

Vây có $30+150+200+75=455$.
Câu 50. Số cách xếp 4 nam sinh và 4 nữ sinh vào một dãy ghế hàng ngang có 8 chỗ ngồi sao cho nam nữ ngồi xen kẽ nhau là
A. $4!+4!$.
B. $8!$.
C. $4!.4!$.
D. $2.4!.4!$.

## Lời giải

## Chọn D

Trường hợp 1: Xếp 4 nam sinh ngồi vào các ghế mang số lẻ và xếp 4 nữ sinh ngồi vào các ghế mang số chẵn có $4!\cdot 4$ ! cách.
Trường hợp 2: Xếp 4 nam sinh ngồi vào các ghế mang số chẵn và xếp 4 nữ sinh ngồi vào các ghế mang số lẻ có 4!.4! cách.

Vậy có tất cả $4!.4!+4!.4!=2.4!\cdot 4$ ! cách
Câu 51. Từ 20 bông hoa gồm có 8 bông màu đỏ, 7 bông màu vàng, 5 bông màu trắng; chọn ngẫu nhiên 4 bông để tạo thành một bó. Có bao nhiêu cách chọn để bó hoa có đủ cả ba màu?
A. 14280 .
B. 4760 .
C. 2381 .
D. 2380 .

## Lời giải

## Dhọn <br> D.

Để lấy được 4 bông hoa có đủ ba màu,
Xét các trường hợp:
Trường hợp 1: 2 bông màu đỏ, 1 bông màu vàng, 1 bông màu trắng ⇒ Có $C_{8}^{2} \cdot 7 \cdot 5$ cách.
Trường hợp 2: 1 bông màu đỏ, 2 bông màu vàng, 1 bông màu trắng $\Rightarrow$ Có $8 . C_{7}^{2} .5$ cách.
Trường hợp 3: 1 bông màu đỏ, 1 bông màu vàng, 2 bông màu trắng $\Rightarrow$ Có 8.7. $C_{5}^{2}$ cách.
Vậy số cách chọn được 1 bó hoa có đủ 3 màu là: $C_{8}^{2} \cdot 7 \cdot 5+8 \cdot C_{7}^{2} \cdot 5+8 \cdot 7 \cdot C_{5}^{2}=2380$
Câu 52. Nếu một đa giác lồi có 44 đường chéo thì đa giác đó có bao nhiêu cạnh?
A. 8 .
B. 10 .
C. 9 .
D. 11 .

## Lời giải

## Chọn <br> D.

Mỗi đoạn thẳng nối hai đỉnh của 1 đa giác lồi $n$ cạnh hoặc là một cạnh hoặc là 1 đường chéo của đa giác đó.
Số đoạn thẳng được tạo thành là $C_{n}^{2}$.
Số cạnh của đa giác là $n$.
Số đường chéo của đa giác đó là $C_{n}^{2}-n$.
Theo bài ra, số đường chéo là 44 nên ta có phương trình $C_{n}^{2}-n=44$.
Giải phương trình $C_{n}^{2}-n=44$
Điều kiện $n \geq 2 ; n \in \mathbb{N}$.
Khi đó $C_{n}^{2}-n=44 \Leftrightarrow \frac{n(n-1)}{2}-n=44 \Leftrightarrow n^{2}-3 n-88=0 \Leftrightarrow\left[\begin{array}{l}n=11 \\ n=-8\end{array}\right.$.

Vậy số cạnh của đa giác bằng 11 .
Câu 53. Để ước tính số tôm chưa biết trong một hồ nuôi tôm, người ta đánh bắt 2500 con, đánh dấu chúng rồi thả lại xuống hồ. Đánh bắt lần thứ hai được 3100 con, thấy trong đó có 450 con có đánh dấu. Khi đó ước tính số tôm trong hồ gần nhất với đáp án nào sau đây.
A. 25370 con.
B. 19450 con.
C. 17223 con.
D. 14780 con.

## Lời giải

## Chọn <br> C.

Gọi $n$ là số lượng tôm ước tính có trong hồ.
Khi đó ta có $\frac{2500}{n}=\frac{450}{3100} \Leftrightarrow n=\frac{2500.3100}{450} \approx 17223$
Câu 54. Có bao nhiêu số tự nhiên có 5 chữ số đôi một khác nhau mà các chữ số đó thuộc tập hợp $$\{1 ; 2 ; 3 ; 4 ; 5\}$$ ?
A. 5!.
B. $5^{5}$.
C. $C_{5}^{5}$.
D. $A_{6}^{5}$.

## Lời giải

## Chọn A

Số cách lập ra số tự nhiên có 5 chữ số đôi một khác nhau mà các chữ số đó thuộc tập hợp \{1;2;3;4;5\} là số hoán vị của 5 phần tử

Vậy có $P 5=5$ ! số tự nhiên có 5 chữ số đôi một khác nhau mà các chữ số đó thuộc tập hợp $$\{1 ; 2 ; 3 ; 4 ; 5\}$$.
Câu 55. Từ các chữ số $0,1,2,3,4,5$ có thể lập được bao nhiêu số tự nhiên chẵn và có 4 chữ số khác nhau?
A. 752 .
B. 156 .
C. 240 .
D. 160 .

## Lời giải

## Chọn B

TH1: Số cần tìm có dạng $\overline{a b c 0}$ với $a, b, c, 0$ đôi một phân biệt được chọn từ $0,1,2,3,4,5$
Lúc này số cách chọn $\overline{a b c}$ bằng $A_{5}^{3}=60$.
TH2: Số cần tìm có dạng $\overline{a b c d}$ với $a, b, c, d$ đôi một phân biệt được chọn từ $0,1,2,3,4,5$ và $d=2$ hoặc $d=4$ đồng thời $a \neq 0$.

Số cách chọn $d$ là 2
Số cách chọn $a$ là 4
Lúc này số cách chọn $b c$ bằng $A_{4}^{2}=12$
Trường hợp này có $2 \cdot 4 \cdot 12=96$.
Vậy có tất cả là $60+96=156$ (số).
Câu 56. Cho hai đường thẳng song song $d_{1}$ và $d_{2}$. Trên $d_{1}$ lấy 17 điểm phân biệt, trên $d_{2}$ lấy 20 điểm phân biệt. Tính số tam giác mà có các đỉnh được chọn từ 37 điểm này.
A. 11900. .
B. 7770..
C. 5950..
D. 5590 .

## Lời giải

## Chọn C

Với 1 điểm thuộc $d_{1}$ kết hợp với 2 điểm thuộc $d_{2}$ hoặc 1 điểm thuộc $d_{2}$ với 2 điểm thuộc $d_{1}$ thì ta có được 1 tam giác.

Vậy số tam giác được lập từ các điểm đã cho là: $C_{17}^{1} \cdot C_{20}^{2}+C_{17}^{2} \cdot C_{20}^{1}=5950$.
Câu 57. Số các số tự nhiên có bẩy chữ số trong đó có hai chữ số 0 , sao cho hai chữ số 0 không đứng cạnh nhau và các chữ số khác chỉ xuất hiện nhiều nhất một lần là
A. 151200
B. 786240 .
C. 846000 .
D. 907200 .

## Lời giải

## Chọn $\underline{\mathrm{A}}$

Để lập các số tự nhiên có bẩy chữ số trong đó có hai chữ số 0 , sao cho hai chữ số 0 không đứng cạnh nhau và các chữ số khác chỉ xuất hiện nhiều nhất một lần ta làm như sau:

+ Chọn 5 số trong 9 số và sắp xếp có $A_{9}^{5}$ cách.
+ 5 số vừa chọn sẽ tạo ra 6 khoảng trống, để xếp hai chữ số 0 sao cho chúng không đứng cạnh nhau ta có 6 vị trí để chọn. Tuy nhiên do chữ số 0 không được đứng đầu nên còn 5 vị trí. Vậy chọn 2 trong 5 vị trí đó để xếp số 0 nên có $C_{5}^{2}$ cách.

Vậy có tất cả: $A_{9}^{5} \cdot C_{5}^{2}=151200$.
Câu 58. Trong buổi dã ngoại, tổ có 12 học sinh tham gia gồm 4 bạn nữ trong đó có An và có 8 bạn nam trong đó có Bình. Thầy giáo chia tổ thành 3 nhóm sao cho các nhóm đều có nữ và hai bạn An , Bình cùng một nhóm. Số cách chia nhóm của thầy giáo là
A. 630 .
B. 840 .
C. 1050 .
D. 2100 .

## Lời giải

## Chọn C

Thầy giáo chia tổ thành 3 nhóm sao cho các nhóm đều có nữ và hai bạn An, Bình cùng một nhóm thì thầy có các cách chia như sau:

- TH1: An và Bình cùng với một bạn nam và một bạn nữ thành một nhóm nên có $C_{7}^{1} \cdot C_{3}^{1}$ cách. Nhóm thứ hai có ba nam và 1 nữ có $C_{6}^{3} \cdot C_{2}^{1}$. Cuối cùng còn ba bạn nam và một bạn nữ có duy nhất một cách cho nhóm thứ ba. Do đó trường hợp này có: $C_{7}^{1} \cdot C_{3}^{1} \cdot C_{6}^{3} \cdot C_{2}^{1}$ cách.
- TH2: An và Bình cùng với hai bạn nam vào một nhóm có $C_{7}^{2}$ cách. Nhóm thứ hai có hai bạn nam và 2 bạn nữ có $C_{5}^{2} \cdot C_{3}^{2}$. Cuối cùng còn ba bạn nam và một bạn nữ nên có duy nhất một cách cho nhóm ba. Do đó trường hợp này có: $C_{7}^{2} \cdot C_{5}^{2} \cdot C_{3}^{2}$ cách.

Vậy có tất cả: $C_{7}^{1} \cdot C_{3}^{1} \cdot C_{6}^{3} \cdot C_{2}^{1}+C_{7}^{2} \cdot C_{5}^{2} \cdot C_{3}^{2}=1470$ cách.
Câu 59. Từ các số $A=\{1 ; 2 ; 3 ; 4 ; 5 ; 6 ; 7 ; 8 ; 9\}$, người ta lập các số tự nhiên có sáu chữ số khác nhau đôi một sao cho tổng các chữ số ở hàng chục, hàng trăm và hàng ngàn bằng 8 . Số các số thỏa mãn là
A. 1300 .
B. 1440 .
C. 1500 .
D. 4320 .

## Lời giải

## Chọn B

Gọi số cần lập có sáu chữ số có dạng $\overline{a_{1} a_{2} a_{3} a_{4} a_{5} a_{6}}$ với $a_{5}+a_{4}+a_{3}=8$.
Ta có $1+2+5=1+3+4=8$. Do đó có 2 cách chọn nhóm 3 số để làm các chữ số hàng chục, hàng trăm, hàng ngàn.

Bài toán chọn số thỏa mãn yêu cầu bài toán được tiến hành theo các bước sau:

Bước 1: Chọn ra bộ 3 số trong 8 số để có $a_{5}+a_{4}+a_{3}=8$ : có 2 cách chọn bộ $\left(a_{5} ; a_{4} ; a_{3}\right)$.
Bước 2: Với mỗi bộ 3 số đã chọn ở bước 1 có $3!=6$ cách lập ra các số $a_{3} a_{4} a_{5}$.
Bước 3: Chọn 3 số từ tập 6 số trong tập $A \backslash\left\{a_{3} ; a_{4} ; a_{5}\right\}$ để xếp vào các vị trí của $a_{1} ; a_{2} ; a_{6}$ : có $A_{6}^{3}=120$ cách.

Theo quy tắc nhân ta có số các số thỏa mãn yêu cầu bài toán là: 2.6.120=1440 số.
Câu 60. Một nhóm học sinh gồm 12 nam và 6 nữ. Người ta muốn chọn từ nhóm ra 5 người để lập thành một đội cờ đỏ sao cho phải có 1 đội trưởng nam, 1 đội phó nam và có ít nhất 1 nữ. Hỏi có bao nhiêu cách lập đội cờ đỏ.
A. 1028160 .
B. 572 .
C. 8568 .
D. 58080 .

## Lời giải

## Chọn D

TH1: 1 đội trưởng nam, 1 đội phó nam, 2 nam, 1 nữ có $A_{12}^{2} \cdot C_{10}^{2} \cdot C_{6}^{1}=35640$ ( cách)
TH2: 1 đội trưởng nam, 1 đội phó nam, 1 nam, 2 nữ có $A_{12}^{2} \cdot C_{10}^{1} \cdot C_{6}^{2}=19800$ ( cách)
TH3: 1 đội trưởng nam, 1 đội phó nam, 3 nữ có $A_{12}^{2} \cdot C_{6}^{3}=2640$ ( cách)
Vậy có: $35640+19800+35640=58080$ (cách).
Câu 61. Một tổ có 5 học sinh nữ và 6 học sinh nam. Số cách chọn ngẫu nhiên 5 học sinh của tổ trong đó có cả học sinh nam và học sinh nữ là?
A. 545 .
B. 462 .
C. 455 .
D. 456 .

## Lời giải

## Chọn C

TH1: 1 nam, 4 nữ có $C_{6}^{1} \cdot C_{5}^{4}=30$ ( cách)
TH2: 2 nam, 3 nữ có $C_{6}^{2} \cdot C_{5}^{3}=150$ ( cách)
TH3: 3 nam, 2nữ có $C_{6}^{3} \cdot C_{5}^{2}=200$ ( cách)
TH4: 4 nam, 1 nữ có $C_{6}^{4} \cdot C_{5}^{1}=75$ ( cách)
Vậy có: $30+150+200+75=455$ (cách).
Câu 62. Tìm số tự nhiên $n$ thỏa mãn thỏa mãn $C_{n}^{2}+5=A_{n-1}^{2}$.
A. $n=8$.
B. $n=5$.
C. $n=6$.
D. $n=7$.

## Lời giải

## Chọn C

$$
\begin{aligned}
& C_{n}^{2}+5=A_{n-1}^{2} \\
& \Leftrightarrow \frac{n!}{2!\cdot(n-2)!}+5=(n-1)(n-2) \\
& \Leftrightarrow \frac{n(n-1)}{2}+5=(n-1)(n-2) \\
& \Leftrightarrow n(n-1)+10=2(n-1)(n-2) \\
& \Leftrightarrow n^{2}-5 n-6=0 \\
& \Leftrightarrow\left[\begin{array}{l}
n=-1(\text { Loai }) \\
n=6
\end{array}\right.
\end{aligned}
$$

