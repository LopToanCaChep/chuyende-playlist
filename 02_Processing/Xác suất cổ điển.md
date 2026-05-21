## PHẦN A. KIẾN THỨC CẦN NHÓ́

## 1. Một số khái niệm về xác suất

a) Phép thử ngẫu nhiên và không gian mẫu

- Có những phép thử mà ta không thể đoán trước được kết quả của nó, mặc dù đã biết tập hợp tất cả các kết quả có thể có của phép thử đó. Những phép thử như thế gọi là phép thử ngẫu nhiên (gọi tắt là phép thử).
- Tập hợp $\Omega$ các kết quả có thể xảy ra của một phép thử gọi là không gian mẫu của phép thử đó.
b) Biến cố và xác suất của biến cố
- Biến cố ngẫu nhiên (gọi tắt là biến cố) là một tập con của không gian mẫu.
- Xét phép thử $T$ với không gian mẫu là $\Omega$. Mỗi biến cố là một tập con của tập hợp $\Omega$. Vì thế, tập rỗng $\varnothing$ cũng là một biến cố, gọi là biến cố không thể (gọi tắt là biến cố không). Còn tập hợp $\Omega$ gọi là biến cố chắc chắn.
- Tập con $\Omega \backslash A$ xác định một biến cố, gọi là biến cố đối của biến cố $A$, kí hiệu là $\bar{A}$.
- Xét phép thử chỉ có một số hữu hạn kết quả có thể xảy ra và khả năng xảy ra của từng kết quả là giống nhau. Gọi $\Omega$ là không gian mẫu của phép thử đó. Khi đó, với mỗi biến cố $A$, ta có định nghĩa cổ điển của xác suất như sau:

Xác suất của biến cố $A$, kí hiệu là $P(A)$, bằng tỉ số $\dfrac{n(A)}{n(\Omega)}$, ở đó $n(A), n(\Omega)$ lần lượt là số phần tử của hai tập hợp $A$ và $\Omega$. Như vậy: $P(A)=\dfrac{n(A)}{n(\Omega)}$.

## 2. Tính chất của xác suất

Xét phép thử $T$ với không gian mẫu là $\Omega$. Khi đó, ta có các tính chất sau:
$-P(\varnothing)=0 ; P(\Omega)=1$
$-0 \leq P(A) \leq 1$ với mỗi biến cố $A$;
$-P(\bar{A})=1-P(A)$ với mỗi biến cố $A$.

## 3. Hình học Tổ hợp

* **Số vectơ** (khác $\overrightarrow{0}$) từ $n$ điểm: $A_n^2$
* **Số đường thẳng** tạo thành từ $n$ điểm (không có 3 điểm thẳng hàng): $C_n^2$
* **Hai đường thẳng song song** ($d_1$ có $m$ điểm, $d_2$ có $n$ điểm):
    * Số giao điểm của các đoạn thẳng chéo nhau: $C_m^2 \cdot C_n^2$
    * Số tam giác tạo thành: $C_m^2 \cdot n + C_n^2 \cdot m$
* **Lưới đường thẳng:** $m$ đường ngang cắt $n$ đường dọc tạo ra số hình bình hành: $C_m^2 \cdot C_n^2$

## 4. Đếm hình trong Đa giác lồi ($n$ đỉnh)

* **Số đoạn thẳng** (cạnh + đường chéo): $C_n^2$
* **Số đường chéo:** $\dfrac{n(n-3)}{2}$
* **Giao điểm đường chéo** (bên trong): $C_n^4$ 
  > ⚠️ *Điều kiện: đa giác ở vị trí tổng quát, không có 3 đường chéo nào đồng quy bên trong. Lưu ý các đa giác đều như lục giác, bát giác, thập nhị giác... có đường chéo đồng quy nên công thức này không áp dụng trực tiếp.*
* **Đếm tam giác theo cạnh chung:**
    * Đúng 2 cạnh chung: $n$
    * Đúng 1 cạnh chung: $n(n-4)$ *(với $n \ge 4$)*
    * Không có cạnh chung: $C_n^3 - n - n(n-4)$

## 5. Tam giác Nhọn, Vuông, Tù

Xét đa giác đều $n$ đỉnh nội tiếp đường tròn. Tổng số tam giác là $C_n^3$.

**Trường hợp $n$ chẵn ($n=2k$)**
* Số tam giác vuông: $\dfrac{n}{2} \cdot (n-2)$
* Số tam giác tù: $n \cdot C_{\dfrac{n}{2}-1}^2$
* Số tam giác nhọn: $C_n^3 - S_{\text{vuông}} - S_{\text{tù}}$

**Trường hợp $n$ lẻ ($n=2k+1$)**
* Số tam giác vuông: $0$ *(không có đường kính nào nối 2 đỉnh)*
* Số tam giác tù: $n \cdot C_{\dfrac{n-1}{2}}^2$
* Số tam giác nhọn: $C_n^3 - S_{\text{tù}}$

> **Mẹo trắc nghiệm nhanh:** Nếu lấy ngẫu nhiên 3 điểm độc lập, phân bố đều trên đường tròn, xác suất tam giác nhọn là **25%** và xác suất tam giác tù là **75%**. *(Đây là bài toán xác suất hình học liên tục, khác với bài toán đếm trên đa giác đều ở trên.)*

## PHẤN C. BÀI TẬP TRÃ́C NGHIỆM

(Trong các bài tập, các đồng xu và xúc xắc là cân đối và đồng chất)

## DÀNH CHO HỌC SINH TRUNG BİNH

Câu 1. Gieo một xúc xắc một lần. Biến cố nào sau đây là biến cố không?
A. Số chấm ở mặt xuất hiện là số nguyên
B. Số chấm ở mặt xuất hiện là số tự nhiên
C. Số chấm ở mặt xuất hiện là số nguyên tố
D. Số chấm ở mặt xuất hiện lớn hơn 7

## Lời giải

Khi gieo một xúc xắc, số chấm xuất hiện chỉ có thể là một trong các giá trị $1, 2, 3, 4, 5, 6$.
- Đáp án A, B đúng vì các số $1$–$6$ đều là số nguyên và là số tự nhiên → biến cố chắc chắn.
- Đáp án C có thể xảy ra khi xuất hiện $2, 3, 5$ → biến cố ngẫu nhiên.
- Đáp án D: không có mặt nào lớn hơn $7$ ⇒ biến cố này không bao giờ xảy ra, đó là biến cố không thể.

## Chọn D

Câu 2. Gieo một xúc xắc hai lần liên tiếp. Biến cố nào sau đây là biến cố chắc chắn?
A. Tổng số chấm ở hai lần gieo là 12
B. Tổng số chấm ở hai lần gieo không vượt quá 12
C. Tổng số chấm ở hai lần gieo là số nguyên tố
D. Tổng số chấm ở hai lần gieo là số chã̃n

## Lời giải

Tổng số chấm ở hai lần gieo nhỏ nhất bằng $1+1=2$ và lớn nhất bằng $6+6=12$.
- A: Tổng bằng $12$ chỉ xảy ra khi cả hai lần đều ra mặt $6$ → biến cố ngẫu nhiên.
- B: Tổng không vượt quá $12$ luôn đúng với mọi kết quả ⇒ biến cố chắc chắn.
- C, D: Tùy kết quả mà có hoặc không, là biến cố ngẫu nhiên.

## Chọn B

Câu 3. Tung một đồng xu hai lần liên tiếp. Tập hợp kết quả thuận lợi của biến cố $A$ là $\backslash\{S N\}$ ( $S$ là mặt sấp, $N$ là mặt ngửa). Biến cố đối của biến cố $A$ có tập hợp các kết quả thuận lợi là:
A. $\{N S\}$
B. $\{N N ; S S\}$
C. $\{S S ; N S ; N N\}$
D. $\{S S\}$

## Lời giải

Không gian mẫu khi tung đồng xu hai lần là: $\Omega = \{SS, SN, NS, NN\}$, $n(\Omega)=4$.
Biến cố $A=\{SN\}$ $\Rightarrow$ Biến cố đối $\bar{A} = \Omega \setminus A = \{SS, NS, NN\}$.

## Chọn C

Câu 4. Trong một hộp có 10 chiếc thẻ cùng loại, mỗi thẻ được ghi một số tự nhiên có một chữ số, hai thẻ khác nhau thì ghi hai số khác nhau. Lấy ngẫu nhiên một thẻ. Biến cố đối của biến cố "Số ở thẻ lấy được là số nguyên tố" là:
A. "Số ở thẻ lấy được là hợp số"
B. "Số ở thẻ lấy được không là số nguyên tố"
C. "Số ở thẻ lấy được là số chẵn"
D. "Số ở thẻ lấy được là số lẻ"

## Lời giải

## Chọn B

Câu 5. Gieo một xúc xắc ba lần liên tiếp. Số phần tử của không gian mẫu trong phép thử trên là:
A. $6$
B. $18$
C. $216$
D. $36$

## Lời giải

Mỗi lần gieo một xúc xắc có 6 khả năng xảy ra nên gieo một xúc xắc ba lần liên tiếp có $6 \cdot 6 \cdot 6=216$ khả năng xảy ra. Suy ra số phần tử của không gian mẫu là 216 .

## Chọn C

Câu 6. Gieo một xúc xắc ba lần liên tiếp. Xác suất của biến cố "Tích số chấm ở ba lần gieo là số chẵn" bằng:
A. $\dfrac{7}{8}$
B. $\dfrac{1}{8}$
C. $\dfrac{1}{216}$
D. $\dfrac{215}{216}$

## Lời giải

## Chọn A

Lấy biến cố đối của biến cố "Tích số chấm ở ba lần gieo là số chẵn" là $B$ : "Tích số chấm ở ba lần gieo là số lẻ".

Trên xúc xắc có 3 mặt số chấm lẻ là $1,3,5$. Muốn tích số chấm ở ba lần gieo là số lẻ thì số chấm ở ba lần gieo đều là số lẻ, suy ra $n(B)=3 \cdot 3 \cdot 3=27$.

Vậy xác suất của biến cố "Tích số chấm ở ba lần gieo là số chẵn" là: $1-P(B)=1-\dfrac{27}{216}=\dfrac{7}{8}$.
Câu 7. Một hộp có 10 chiếc thẻ cùng loại, mỗi thẻ được ghi một số nguyên dương không vượt quá 10 , hai thẻ khác nhau ghi hai số khác nhau. Lấy ngẫu nhiên 1 thẻ. Xác suất của biến cố "Số trên thẻ được lấy ra là số nguyên tố" bằng:
A. $0,4$
B. $0,5$
C. $0,3$
D. $0,6$

## Lời giải

## Chọn A

Có đúng 4 số nguyên tố không vượt quá 10 là $2,3,5,7$.
Xác suất cần tìm là: $\dfrac{4}{10}=0,4$.
Câu 8. Trong một hộp kẹo có 4 loại kẹo với vỏ ngoài và khối lượng giống nhau, tỉ lệ các loại kẹo được biểu diễn ở biểu đồ như hình bên. Chọn ngẫu nhiên 1 kẹo. Xác suất của biến cố "Chọn được 1 kẹo vị xoài" bằng:
![](https://cdn.mathpix.com/cropped/0f870c95-a07f-4ae9-831a-8d8b21ea630f-03.jpg?height=392&width=398&top_left_y=1667&top_left_x=397)
A. $0,15$
B. $0,20$
C. $0,30$
D. $0,35$

## Lời giải

## Chọn B

Dựa vào biểu đồ hình quạt tròn, tỉ lệ kẹo vị xoài chiếm $20\%$.
Do đó, xác suất để chọn được $1$ kẹo vị xoài là $20\% = 0,20$.

Câu 9. Tung một đồng xu hai lần liên tiếp. Xác suất của biến cố $A$ : "Kết quả của hai lần tung là giống nhau" bằng:
A. $0$
B. $1$
C. $\dfrac{1}{2}$
D. $\dfrac{1}{4}$

## Giải

Không gian mẫu $\Omega=\{S S ; N N ; S N ; N S\}$ (trong đó, $S$ là mặt sấp, $N$ là mặt ngửa). Vậy $n(\Omega)=4$

Ta có: $A=\{S S ; N N\}$ nên $n(A)=2$.
Suy ra $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{2}{4}=\dfrac{1}{2}$. Chọn $\mathbf{C}$
Câu 10. Gieo một xúc xắc hai lần liên tiếp. Xác suất của biến cố $A$ : "Số chấm ở hai lần gieo đều là số chẵn" bằng:
A. $0$
B. $1$
C. $\dfrac{1}{2}$
D. $\dfrac{1}{4}$

## Giải

Không gian mẫu $\Omega=\{(i ; j) \mid i, j=1,2,3,4,5,6\}$ (i là số chấm ở lần gieo thứ nhất, $j$ là số chấm ở lần gieo thứ hai). Vậy $n(\Omega)=36$.

Ta có: $A=\{(2 ; 2) ;(4 ; 4) ;(6 ; 6) ;(2 ; 4) ;(4 ; 2) ;(2 ; 6) ;(6 ; 2) ;(4 ; 6) ;(6 ; 4)\}$ nên $n(A)=9$.
Suy ra $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{9}{36}=\dfrac{1}{4}$. Chọn $\mathbf{D}$
Câu 11. Một tổ trong lớp 10 B có 12 học sinh trong đó có 7 học sinh nam và 5 học sinh nữ. Giáo viên chọn ngẫu nhiên 4 học sinh trong tổ đó để tham gia đội tình nguyện Mùa hè xanh. Tính xác suất để 4 học sinh được chọn đều là nữ.
A. $\dfrac{1}{99}$
B. $\dfrac{7}{99}$
C. $\dfrac{1}{3}$
D. $\dfrac{4}{5}$

## Lời giải

## Chọn A

Số phần tử của không gian mẫu $n(\Omega)=C_{12}^{4}=495$.
Gọi biến cố A : "Cả 4 học sinh được chọn đều là nữ"
$\Rightarrow n(A)=C_{5}^{4}=5$
Xác suất của biến cố $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{5}{495}=\dfrac{1}{99}$.
Câu 12. Chọn ngẫu nhiên hai số khác nhau từ tập $\{1 ; 2 ; 3 ; 4 ; 5 ; 6 ; 7 ; 8 ; 9\}$. Tính xác suất để trong hai số lấy ra có ít nhất một số lẻ.
A. $\dfrac{5}{6}$
B. $\dfrac{5}{9}$
C. $\dfrac{5}{18}$
D. $\dfrac{8}{9}$

## Lời giải

## Chọn A

Số phần tử của không gian mẫu $n(\Omega)=C_{9}^{2}=36$.
Gọi biến cố A : "Cả 2 số lấy ra đều chẵn"
$\Rightarrow n(A)=C_{4}^{2}=6$
Xác suất của biến cố $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{6}{36}=\dfrac{1}{6}$.
Ta có biến cố $\bar{A}$ : "Trong hai số lấy ra có ít nhất một số lẻ"
$\Rightarrow P(\bar{A})=1-P(A)=\dfrac{5}{6}$.

Câu 13. Có 10 tấm thẻ được đánh số từ 1 đến 10. Chọn ngẫu nhiên 2 tấm thẻ. Xác suất để chọn được 2 tấm thẻ đều ghi số chẵn là
A. $\dfrac{1}{4}$
B. $\dfrac{2}{9}$
C. $\dfrac{1}{2}$
C. $x=2$

## Lời giải

## Chọn B

Từ 1 đến 10 có 5 số chẵn.
Số cách chọn ngẫu nhiên 2 tấm thẻ là: $n(\Omega)=C_{10}^{2}=45$.
Số cách để chọn được hai tấm thẻ ghi số chẵn là: $n(A)=C_{5}^{2}=10$.
⇒ Xác suất để chọn được hai tấm thẻ đều ghi số chẵn là $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{10}{45}=\dfrac{2}{9}$.
Câu 14. Cho $E$ là một biến cố. Xác suất của biến cố đối $\bar{E}$ liên hệ với xác suất của biến cố $E$ theo công thức nào sau đây?
A. $P(\bar{E})=P(E)-1$
B. $P(\bar{E})=P(E)$
C. $P(\bar{E})=1-P(E)$
D. $P(\bar{E})=1+P(E)$

## Lời giải

## Chọn C

Xác suất của biến cố đối $\bar{E}$ liên hệ với xác suất của biến cố $E$ theo công thức $P(\bar{E})=1-P(E)$.
Câu 15. Có ba chiếc hộp. Hộp 1 có chứa hai viên bi: 1 viên màu đỏ, 1 viên màu vàng. Hộp 2 chứa hai viên bi: 1 viên màu đỏ, 1 viên màu xanh. Hộp 3 chứa hai viên bi: 1 viên màu vàng, 1 viên màu xanh. Từ mỗi hộp ta lấy ngẫu nhiên một viên bi và các phần tử của không gian mẫu được mô tả bằng sơ đồ dưới đây

Hộp 1

Hộp 2

Hộp 3

Đ: Đỏ, V: Vàng, X: Xanh
![](https://cdn.mathpix.com/cropped/0f870c95-a07f-4ae9-831a-8d8b21ea630f-05.jpg?height=426&width=691&top_left_y=1375&top_left_x=548)

Gọi $K$ là biến cố: "Trong ba viên bi lấy ra có đúng một viên bi màu đỏ". Số kết quả thuận lợi cho biến cố $K$ là
A. $8$
B. $2$
C. $6$
D. $4$

## Lời giải

## Chọn D

Số kết quả thuận lợi cho biến cố $K$ là 4 .
Câu 16. Một hộp có 8 chiếc thẻ cùng loại, mỗi thẻ được đánh số từ 1 đến 8 , hai thẻ khác nhau thì ghi hai số khác nhau. Rút ngẫu nhiên đồng thời hai chiếc thẻ từ trong hộp. Tính xác suất của biến cố "Rút được hai thẻ ghi số chẵn"
A. $\dfrac{1}{7}$
B. $\dfrac{3}{14}$
C. $\dfrac{1}{2}$
D. $\dfrac{1}{14}$

## Lời giải

## Chọn A

Số phần tử của không gian mẫu $n(\Omega)=C_{8}^{2}=28$.
Gọi biến cố $A=$ "Rút được hai thẻ ghi số chẵn"
$\Rightarrow n(A)=4 \Rightarrow p(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{4}{28}=\dfrac{1}{7}$.
Câu 17. Từ một đội văn nghệ có 5 nam và 8 nữ, cần lập một nhóm 4 người hát tốp ca một cách ngẫu nhiên. Xác suất để trong 4 người được chọn có ít nhất 3 nam bằng
A. $\dfrac{70}{143}$
B. $\dfrac{73}{143}$
C. $\dfrac{17}{143}$
D. $\dfrac{16}{143}$

## Lời giải

## Chọn C

$n(\Omega)=C_{13}^{4}$.
Gọi A là biến cố chọ đượcc ít nhất 3 nam: $n(\mathrm{~A})=C_{5}^{3} \cdot C_{8}^{1}+C_{5}^{4}$.
Xác suất để A xảy ra là: $P_{A}=\dfrac{n(A)}{n(\Omega)}=\dfrac{17}{143}$.
Câu 18. Bác $A$ có một chiếc điện thoại cũ để mật khẩu 4 chữ số. Bác đã quên mật khẩu chính xác và chỉ nhớ các chữ số đó là đôi một khác nhau. Xác suất để Bác A bấm đúng mật khẩu của chiếc điện thoại cũ đó trong một lần là:
A. $\dfrac{1}{C_{10}^{4}}$
B. $\dfrac{1}{A_{10}^{4}}$
C. $\dfrac{A_{10}^{4}}{4!}$
D. $\dfrac{4!}{A_{10}^{4}}$

## Lời giải

## Chọn B

Gọi A là biến cố "bác A bấm đúng mật khẩu của chiếc điện thoại cũ đó trong một lần"
Ta có $n(\Omega)=A_{10}^{4}$ và $n(A)=1 \Rightarrow P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{1}{A_{10}^{4}}$.
Câu 19. Một tổ trong lớp 10 A có 10 học sinh trong đó có 6 học sinh nam và 4 học sinh nữ. Giáo viên chọn ngẫu nhiên 4 học sinh trong tổ đó để tham gia đội làm báo tường của lớp. Xác suất để cả bốn bạn được chọn đều là nữ là
A. $\dfrac{1}{210}$.
B. $\dfrac{1}{10}$.
C. $\dfrac{1}{5040}$.
D. $\dfrac{2}{105}$

## Lời giải

## Chọn $\underline{\mathbf{A}}$

Số phần tử của không gian mẫu là: $n(\Omega)=C_{10}^{4}=210$.
Số kết quả thuận lợi cho biến cố $A$ : "cả bốn bạn được chọn đều là nữ" là $n(A)=1$.
Vậy xác suất cần tìm là $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{1}{210}$.
Câu 20. Một tổ trong lớp 10D có 10 học sinh trong đó có 6 học sinh nam và 4 học sinh nữ. Giáo viên chọn ngẫu nhiên 4 học sinh trong tổ đó để tham gia đội tình nguyện Mùa hè xanh. Xác suất để trong bốn bạn được chọn có ba nam và một nữ là
A. $\dfrac{8}{21}$.
B. $\dfrac{4}{35}$
C. $\dfrac{2}{21}$.
D. $\dfrac{1}{63}$

## Lời giải

## Chọn $\underline{\mathrm{A}}$

Số phần tử của không gian mẫu là: $n(\Omega)=C_{10}^{4}=210$.

Số kết quả thuận lợi cho biến cố $A$ : "bốn bạn được chọn có ba nam và một nữ" là $n(A)=C_{6}^{3} \cdot C_{4}^{1}=80$.

Vậy xác suất cần tìm là $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{80}{210}=\dfrac{8}{21}$.
Câu 21. Một khoa Bệnh viện $A$ có 12 bác sĩ trong đó có 6 bác sĩ nam và 6 bác sĩ nữ. Cần chọn ngẫu nhiên 6 bác sĩ trong khoa đó để thành lập đoàn kiểm tra công tác phòng chống dịch Covid 19. Xác suất để 6 bác sĩ được chọn có số bác sĩ nữ bằng số bác sĩ nam là
A. $\dfrac{100}{231}$.
B. $\dfrac{1}{924}$.
C. $\dfrac{5}{8316}$.
D. $\dfrac{5}{231}$

## Lời giải

## Chọn A

Số phần tử của không gian mẫu là: $n(\Omega)=C_{12}^{6}=924$.
Số kết quả thuận lợi cho biến cố $A$ : " 6 bác sĩ được chọn có số bác sĩ nữ bằng số bác sĩ nam" là $n(A)=C_{6}^{3} \cdot C_{6}^{3}=400$.

Vậy xác suất cần tìm là $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{400}{924}=\dfrac{100}{231}$.
Câu 22. Một hộp chứa các viên bi kích thước khác nhau, trong đó có 5 viên bi màu xanh, 4 viên bi màu đỏ và 6 viên bi màu vàng. Lấy ngẫu nhiên đồng thời 4 viên bi từ hộp. Tính xác suất để trong 4 viên bi lấy ra có đúng 1 viên bi màu vàng.
A. $\dfrac{37}{65}$.
B. $\dfrac{59}{65}$.
C. $\dfrac{24}{65} .$
D. $\dfrac{6}{65}$

## Lời giải

## Chọn C

Ta có $n(\Omega)=C_{15}^{4}$.
Số cách để lấy được 4 viên bi trong đó có đúng 1 bi màu vàng là $n(A)=C_{6}^{1} \cdot C_{9}^{3}$.
Xác suất cần tính là $P(A)=\dfrac{C_{6}^{1} \cdot C_{9}^{3}}{C_{15}^{4}}=\dfrac{24}{65}$.
Câu 23. Một người chọn ngẫu nhiên đồng thời 4 quân bài từ bộ tú lơ khơ gồm 52 quân bài. Tính xác suất của biến cố: "Cả 4 quân bài đều là Át".
A. $\dfrac{1}{C_{52}^{4}}$
B. $\dfrac{4}{C_{52}^{4}}$
C. $\dfrac{3}{4}$
D. $\dfrac{1}{2}$

## Lời giải

## Chọn $\underline{\mathrm{A}}$

Số phần tử không gian mẫu $n(\Omega)=C_{52}^{4}$.
Chỉ có 1 cách để lấy được cả 4 quân bài đều là Át nên xác suất cần tính là $\dfrac{1}{C_{52}^{4}}$.

Câu 24. Một hộp có 5 chiếc thẻ cùng loại được đánh số $1,2,3,4,5$. Hai thẻ khác nhau thì ghi hai số khác nhau. Rút ngẫu nhiên đồng thời 2 chiếc thẻ từ trong hộp. Xét biến cố Y: "Số ghi trên hai thẻ đều là số lẻ". Tính số phần tử của biến cố Y.
A. $4$
B. $3$
C. $5$
D. $6$

## Lời giải

## Chọn B

Số phần tử của $Y$ là $C_{3}^{2}=3$.
Câu 25. Một hộp chứa 3 quả cầu màu xanh và 7 quả cầu màu đỏ. Chọn ngẫu nhiên đồng thời hai quả cầu từ hộp đó. Xác suất để hai quả cầu được chọn ra cùng màu bằng
A. $\dfrac{7}{15}$
B. $\dfrac{7}{30}$
C. $\dfrac{5}{11}$
D. $\dfrac{8}{15}$

## Lời giải

## Chọn D

Ta có: $n(\Omega)=C_{10}^{2}=45$.
Gọi A là biến cố " Chọn được hai quả cầu cùng màu" $\Rightarrow n(A)=C_{3}^{2}+C_{7}^{2}=24$
Do đó: $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{24}{45}=\dfrac{8}{15}$..
Câu 26. Một khách sạn có 6 phòng đơn. Có 10 khách thuê phòng trong đó có 6 nam và 4 nữ. Người quản lí chọn ngẫu nhiên 6 người cho nhận phòng. Xác suất để cả 6 người là nam là
A. $\dfrac{1}{210}$
B. $\dfrac{11}{210}$
C. $\dfrac{1}{105}$
D. $\dfrac{7}{210}$

## Lời giải

## Chọn A

Chọn ngẫu nhiên 6 người có số cách chọn là $C_{10}^{6}=210$ cách.
Chọn ngẫu nhiên 6 người đều là nam có số cách chọn là $C_{6}^{6}=1$ cách.
Suy ra xác suất để cả 6 người là nam là $\dfrac{1}{210}$.
Câu 27. Từ một hộp chứa 12 quả bóng gồm 5 quả màu đỏ và 7 quả màu xanh, lấy ngẫu nhiên đồng thời 3 quả. Xác suất để lấy được 3 quả màu xanh bằng
A. $\dfrac{7}{44}$
B. $\dfrac{5}{12}$
C. $\dfrac{2}{7}$
D. $\dfrac{1}{22}$

## Lời giải

## Chọn A

Lấy ngẫu nhiên 3 quả bóng có số cách là $C_{12}^{3}=220$ cách.
Lấy ngẫu nhiên 3 quả bóng đều màu xanh có số cách là $C_{7}^{3}=35$ cách.
Suy ra xác suất để cả 6 người là nam là $\dfrac{35}{220}=\dfrac{7}{44}$.
Câu 28. Một bình đựng 5 quả cầu xanh và 4 quả cầu đỏ và 3 quả cầu vàng. Chọn ngẫu nhiên 3 quả cầu. Xác suất để được 3 quả cầu có đủ ba màu là
A. $\dfrac{3}{14}$
B. $\dfrac{3}{5}$
C. $\dfrac{3}{7}$
D. $\dfrac{3}{11}$

## Lời giải

## Chọn D

Số quả cầu trong bình là $5+4+3=12$
Số phần tử không gian mẫu là: $n(\Omega)=C_{12}^{3}=220$
Gọi A là biến cố: "Chọn được 3 quả cầu có đủ ba màu"
Số phần tử của biến cố A là: $n(A)=5.4 .3=60$
Xác suất của biến cố A là: $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{60}{220}=\dfrac{3}{11}$.
Câu 29. Một tổ học sinh có 7 nam và 3 nữ. Chọn ngẫu nhiên 2 người. Tính xác suất sao cho 2 người được chọn có một nam và một nữ.
A. $\dfrac{8}{15}$
B. $\dfrac{1}{5}$.
C. $\dfrac{7}{15} .$
D. $\dfrac{1}{15}$

## Lời giải

## Chọn C

Số người trong tổ học sinh là: $7+3=10$
Số phần tử không gian mẫu là: $n(\Omega)=C_{10}^{2}=45$
Gọi A là biến cố: " 2 người được chọn có một nam và một nữ"
Số phần tử của biến cố A là: $n(A)=7.3=21$
Xác suất của biến cố A là: $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{21}{45}=\dfrac{7}{15}$.
Câu 30. Từ một hộp chứa 10 quả cầu màu đỏ và 5 quả cầu màu xanh, lấy ngẫu nhiên đồng thời 3 quả cầu. Xác suất để lấy được 3 quả cầu màu xanh bằng
A. $\dfrac{2}{91}$
B. $\dfrac{1}{12}$
C. $\dfrac{24}{91}$
D. $\dfrac{12}{91}$

## Lời giải

## Chọn A

Số quả cầu trong hộp là: $10+5=15$
Số phần tử không gian mẫu là: $n(\Omega)=C_{15}^{3}=455$
Gọi A là biến cố: "lấy được 3 quả cầu màu xanh"
Số phần tử của biến cố A là $n(A)=C_{5}^{3}=10$
Xác suất của biến cố A là $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{10}{455}=\dfrac{2}{91}$.
Câu 31. Trong một hộp có 5 viên bi vàng, 4 viên bi đỏ và 7 viên bi xanh. Lấy ngẫu nhiên đồng thời 3 viên bi từ hộp đó. Xác suất để lấy ra được 3 viên bi cùng màu bằng
A. $\dfrac{1}{56}$
B. $\dfrac{1}{16}$
C. $\dfrac{1}{140}$
D. $\dfrac{7}{80}$

## Lời giải

## Chọn D

Ta có: $n(\Omega)=C_{16}^{3}=560$.
Gọi $A$ là biến cố lấy được 3 viên cùng màu, khi đó: $n(A)=C_{5}^{3}+C_{4}^{3}+C_{7}^{3}=49$.
Suy ra $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{49}{560}=\dfrac{7}{80}$.

Câu 32. Đội Thanh niên tình nguyện của Đoàn trường THPT Lê Quý Đôn gồm có 15 học sinh ( 9 học sinh nam và 6 học sinh nữ). Chọn ngẫu nhiên 3 học sinh đi làm nhiệm vụ. Xác suất để chọn được 3 học sinh nam là
A. $\dfrac{4}{91}$
B. $\dfrac{12}{65}$
C. $\dfrac{5}{21}$
D. $\dfrac{21}{55}$

## Lời giải

## Chọn B

Số cách chọn 3 học sinh từ 15 học sinh là $C_{15}^{3}$
Số cách chọn 3 học sinh nam từ 9 học sinh nam là $C_{9}^{3}$
Vậy xác suất để chọn được 3 học sinh nam là $\dfrac{C_{9}^{3}}{C_{15}^{3}}=\dfrac{12}{65}$.
Câu 33. Trong một hộp chứa một số bi, mỗi bi mang một số từ số 1 đến số 21 và không có hai bi nào mang số giống nhau. Chọn ngẫu nhiên từ hộp đó ra 2 bi. Xác suất 2 bi được chọn đều mang số lẻ là
A. $\dfrac{3}{14}$
B. $\dfrac{5}{14}$
C. $\dfrac{23}{42}$
D. $\dfrac{11}{42}$

## Lời giải

## Chọn D

Số cách chọn 2 bi từ 21 bi là $C_{21}^{2}$
Từ số 1 đến số 21 có 11 số lẻ nên số cách chọn được 2 bi đều mang số lẻ là $C_{11}^{2}$
Vậy xác suất 2 bi được chọn đều mang số lẻ là $\dfrac{C_{11}^{2}}{C_{21}^{2}}=\dfrac{11}{42}$.
Câu 34. Từ một hộp có 6 viên bi xanh, 5 viên bi đỏ và 4 viên bi vàng, lấy ngẫu nhiên 7 viên bi. Tính xác suất để lấy được ít nhất một viên bi vàng.
A. $\dfrac{661}{715}$
B. $\dfrac{2}{39}$
C. $\dfrac{37}{39}$
D. $\dfrac{56}{195}$

## Lời giải

## Chọn C

Số phần tử không gian mẫu là $C_{15}^{7}=6435$
Số phần tử biến cố lấy ngẫu nhiên 7 viên bi không có viên bi màu vàng là $C_{11}^{7}=330$
Vậy xác suất để lấy được ít nhất một viên bi vàng là $P=\dfrac{6435-330}{6435}=\dfrac{37}{39}$.
Câu 35. Cho hai đường thẳng song song $d_{1}, d_{2}$. Trên $d_{1}$ có 6 điểm phân biệt được tô màu đỏ, trên $d_{2}$ có 4 điểm phân biệt được tô màu xanh. Xét tất cả các tam giác được tạo thành khi nối các điểm đó với nhau. Chọn ngẫu nhiên một tam giác, khi đó xác suất để thu được tam giác có hai đỉnh màu đỏ là
A. $\dfrac{5}{9}$
B. $\dfrac{5}{8}$
C. $\dfrac{2}{9}$
D. $\dfrac{3}{8}$

## Lời giải

## Chọn B

Số phần tử của không gian mẫu: $n(\Omega)=C_{6}^{1} \cdot C_{4}^{2}+C_{6}^{2} \cdot C_{4}^{1}=96$.
Gọi $A$ là biến cố "thu được tam giác có hai đỉnh màu đỏ".
Vậy $P(A)=\dfrac{C_{6}^{2} \cdot C_{4}^{1}}{96}=\dfrac{5}{8}$.
Câu 36. Một hộp chứa 11 quả cầu gồm 5 quả màu xanh và 6 quả màu đỏ. Chọn ngẫu nhiên đồng thời 2 quả cầu từ hộp đó. Xác suất để 2 quả cầu chọn ra cùng màu bằng
A. $\dfrac{3}{11}$
B. $\dfrac{6}{11}$
C. $\dfrac{5}{11}$
D. $\dfrac{2}{11}$

## Lời giải

## Chọn C

Xác suất để 2 quả cầu chọn ra cùng màu bằng: $\dfrac{C_{5}^{2}+C_{6}^{2}}{C_{11}^{2}}=\dfrac{25}{55}=\dfrac{5}{11}$
Câu 37. Có 10 tấm thẻ được đánh số từ 1 đến 10. Chọn ngẫu nhiên 2 tấm thẻ. Xác suất để chọn được 2 tấm thẻ đều ghi số chẵn là
A. $\dfrac{1}{4}$
B. $\dfrac{2}{9}$
C. $\dfrac{7}{9}$
D. $\dfrac{1}{2}$

## Lời giải

## Chọn B

Số phần tử của không gian mẫu: $n(\Omega)=C_{10}^{2}=45$.
Gọi $A$ là biến cố "chọn được 2 tấm thẻ đều ghi số chẵn".
Để chọn được 2 tấm thẻ đều ghi số chẵn có $n(A)=C_{5}^{2}=10$ khả năng.
Vậy $P(A)=\dfrac{10}{45}=\dfrac{2}{9}$.
Câu 38. Chọn ngẫu nhiên hai số khác nhau từ 15 số nguyên dương đầu tiên. Xác suất để chọn được hai số có tổng là một số lẻ là
A. $\dfrac{1}{7}$
B. $\dfrac{1}{14}$
C. $\dfrac{4}{15}$
D. $\dfrac{8}{15}$

## Lời giải

## Chọn D

Số cách chọn ngẫu nhiên hai số khác nhau từ 15 số nguyên dương đầu tiên là $C_{15}^{2}=105$
Để chọn được hai số có tổng là một số lẻ thì hai số được chọn có 1 số chẵn và 1 số lẻ.
Chọn 1 số chẵn từ 7 số chẵn và chọn 1 số lẻ từ 8 số lẻ là $C_{7}^{1} \cdot C_{8}^{1}=56$
Xác suất để chọn được hai số có tổng là một số lẻ là $\dfrac{56}{105}=\dfrac{8}{15}$
Câu 39. Cho đa giác đều có 14 đỉnh. Chọn ngẫu nhiên 3 đỉnh trong số 14 đỉnh của đa giác. Xác suất để 3 đỉnh được chọn là 3 đỉnh của một tam giác vuông là
A. $\dfrac{3}{13}$
B. $\dfrac{5}{13}$
C. $\dfrac{4}{13}$
D. $\dfrac{2}{13}$

## Lời giải

## Chọn $\underline{\mathrm{A}}$

Số cách chọn 3 đỉnh từ 14 đỉnh là $C_{14}^{3}=364$
Đa giác đều có 14 đỉnh có 7 đường kính.
Tam giác vuông được tạo thành từ 1 đường kính và 1 đỉnh bất kì trong 12 đỉnh còn lại (trừ 2 đỉnh tạo nên đường kính) do đó số tam giác vuông được tạo thành là $7.12=84$

Xác suất để 3 đỉnh được chọn là 3 đỉnh của một tam giác vuông là $\dfrac{84}{364}=\dfrac{3}{13}$

## DÀNH CHO HỌC SINH KHÁ GIỎI

Câu 40. Một người chọn ngẫu nhiên một dãy kí tự gồm 4 chữ số để làm mật khẩu cho vali. Xác suất của biến cố "Chọn được một dãy 4 chữ số sắp xếp theo thứ tự tăng dần mà số liền sau hơn số liền trước 1 đơn vị" bằng:
A. $\dfrac{7}{10^{4}}$
B. $\dfrac{6}{10^{4}}$
C. $\dfrac{7}{9.10^{3}}$
D. $\dfrac{6}{9.10^{3}}$

## Lời giải

## Chọn A

Các dãy 4 chữ số sắp xếp theo thứ tự tăng dần mà số liền sau hơn số liền trước 1 đơn vị là: 0123,1234,2345,3456,4567,5678,6789. Suy ra số phần tử của biến cố là 7 .

Số cách chọn một dãy 4 chữ số là: $10 \cdot 10 \cdot 10 \cdot 10=10^{4}$. Suy ra số phần tử của không gian mẫu là $10^{4}$.

Vậy xác suất cần tìm là: $\dfrac{7}{10^{4}}$.
Câu 41. Mật khẩu của một ứng dụng mobile banking là dãy 6 kí tự bao gồm chữ và số. Xét tập hợp $A$ bao gồm các mật khẩu có 2 kí tự đầu là chữ cái thuộc tập hợp 27 chữ cái in thường và 4 kí tự sau là chữ số thuộc tập hợp 10 chữ số. Chọn ngẫu nhiên 1 mật khẩu từ $A$. Xác suất của biến cố "Chọn được mật khẩu ab0123" bằng:
A. $\dfrac{1}{2^{27} \cdot 4^{10}}$
B. $\dfrac{1}{270}$
C. $\dfrac{6}{270}$
D. $\dfrac{1}{27^{2} \cdot 10^{4}}$

## Lời giải

## Chọn D

Số phần tử của tập hợp $A$ là $27^{2} \cdot 10^{4}$. Số phần tử của biến cố là 1 . Vậy xác suất cần tìm là: $\dfrac{1}{27^{2} \cdot 10^{4}}$.

Câu 42. Gieo một xúc xắc hai lần liên tiếp. Xác suất của biến cố "Số chấm ở lần gieo thứ hai hơn số chấm ở lần gieo thứ nhất 2 đơn vị" bằng:
A. $\dfrac{1}{8}$
B. $\dfrac{1}{3}$
C. $\dfrac{1}{9}$
D. $\dfrac{3}{8}$

## Lời giải

## Chọn C

Các kết quả thuận lợi của biến cố là: $(1 ; 3),(2 ; 4),(3 ; 5),(4 ; 6)$, với $(i ; j)$ là kết quả mặt xuất hiện ở lần gieo thứ nhất và thứ hai lần lượt là $i$ chấm và $j$ chấm.

Số phần tử của không gian mẫu là 36 .

Vậy xác suất cần tìm là: $\dfrac{4}{36}=\dfrac{1}{9}$.
Câu 43. Gieo một xúc xắc ba lần liên tiếp. Xác suất của biến cố "Tổng số chấm ở ba lần gieo không nhỏ hơn 16 " bằng:
A. $\dfrac{1}{216}$
B. $\dfrac{5}{108}$
C. $\dfrac{7}{216}$
D. $\dfrac{3}{108}$

## Lời giải

## Chọn B

Các kết quả thuận lợi của biến cố là: $(6 ; 6 ; 4),(6 ; 4 ; 6),(4 ; 6 ; 6),(5 ; 5 ; 6)$, $(5 ; 6 ; 5),(6 ; 5 ; 5),(6 ; 6 ; 5),(6 ; 5 ; 6),(5 ; 6 ; 6),(6 ; 6 ; 6)$, với $(i ; j ; k)$ là kết quả mặt xuất hiện ở lần gieo thứ nhất, thứ hai và thứ ba lần lượt là $i$ chấm, $j$ chấm và $k$ chấm.

Số phần tử của không gian mẫu là 216 .
Xác suất cần tìm là: $\dfrac{10}{216}=\dfrac{5}{108}$.
Câu 44. Nhân ngày khai trương, một siêu thị đưa ra chương trình tặng quà như sau: Các khách hàng vào siêu thị được đánh số thứ tự là các số tự nhiên liên tiếp (khách hàng đầu tiên được đánh số thứ tự là 1); cứ 4 lượt khách vào siêu thị thì khách thứ 4 được tặng một cái lược, cứ 5 lượt khách vào siêu thị thì khách thứ 5 được tặng một bọc khăn giấy, cứ 6 lượt khách vào siêu thị thì khách thứ 6 được tặng một cục xà bông. Sau một thời gian có 200 khách đầu tiên vào siêu thị và chưa có ai đi về. Chọn ngẫu nhiên 1 người trong 200 khách hàng đó. Xác suất của biến cố "Chọn được một khách hàng được nhận cả 3 món quà" là:
A. $\dfrac{1}{100}$
B. $\dfrac{3}{100}$
C. $\dfrac{3}{200}$
D. $\dfrac{1}{200}$

## Lời giải

## Chọn C

Gọi $n$ là số thứ tự của khách hàng được nhận cả ba món quà, suy ra $n$ chia hết cho cả $4,5,6$ nên $n$ chia hết cho $\operatorname{BCNN}(4,5,6)$.

Mà $n<200$ nên $n \in\{60 ; 120 ; 180\}$. Vậy xác suất cần tìm là: $\dfrac{3}{200}$.
Câu 45. Cho tập hợp $A$ gồm 2022 số nguyên dương không vượt quá 2 022. Chọn ngẫu nhiên 2 số thuộc tập hợp $A$. Xác suất của biến cố "Tích của hai số được chọn là số chẵ" là:
A. $\dfrac{C_{1011}^{2}}{C_{2022}^{2}}$
B. $1-\dfrac{C_{1011}^{2}}{C_{2022}^{2}}$
C. $\dfrac{1}{2}$
D. $\dfrac{1}{1011}$

## Lời giải

## Chọn B

Lấy biến cố đối của biến cố "Tích của hai số được chọn là số chã̃n" là "Tích của hai số được chọn là số lẻ".

Tích của hai số nguyên dương là số lẻ khi và chỉ khi cả hai số đều là số lẻ.
Có 1011 số nguyên dương lẻ không vượt quá 2022.

Vậy xác suất cần tìm là: $1-\dfrac{C_{1011}^{2}}{C_{2011}^{2}}$.
Câu 46. Ngân hàng đề thi của một môn khoa học xã hội gồm 150 câu hỏi. Người ta chọn trong ngân hàng đề thi 5 câu hỏi để làm thành một đề thi, hai đề thi được gọi là giống nhau nếu có cùng tập hợp 5 câu hỏi. Một học sinh chắc chắn trả lời đúng 105 câu hỏi trong ngân hàng đề thi đó. Xác suất của biến cố "Học sinh đó rút ngẫu nhiên được một đề thi mà có đúng 3 câu hỏi chắc chắn trả lời đúng" là:
A. $\dfrac{C_{105}^{3}}{C_{120}^{5}}$
B. $1-\dfrac{C_{105}^{3}}{C_{150}^{5}}$
C. $\dfrac{105}{150}$
D. $\dfrac{C_{45}^{2} C_{105}^{3}}{C_{150}^{5}}$

## Lời giải

## Chọn D

Số cách chọn một đề thi mà có đúng 3 câu hỏi sao cho học sinh chắc chắn trả lời đúng là: $C_{45}^{2} \cdot C_{105}^{3}$ .

Số cách chọn 5 câu trong 150 câu là: $C_{150}^{5}$.
Vậy xác suất cần tìm là: $\dfrac{C_{45}^{2} C_{105}^{3}}{C_{150}^{5}}$.
Câu 47. Một đề thi trắc nghiệm gồm 50 câu hỏi, mỗi câu hỏi có 4 phương án trả lời và có duy nhất 1 phương án đúng. Một học sinh khoanh ngẫu nhiên cả 50 câu, mỗi câu khoanh một phương án, nếu đúng thì được 0,2 điểm. Xác suất của biến cố "Học sinh đó được 9 điểm" là:
A. $\dfrac{C_{50}^{45} 3^{5}}{4^{45}}$
B. $C_{50}^{45}\left(\dfrac{1}{4}\right)^{45}$
C. $\left(\dfrac{1}{4}\right)^{45}\left(\dfrac{3}{4}\right)^{5}$
D. $C_{50}^{45}\left(\dfrac{1}{4}\right)^{45}\left(\dfrac{3}{4}\right)^{5}$

## Lời giải

## Chọn D

Mô̂i câu hỏi có 4 cách khoanh đáp án, số cách khoanh 50 câu là $4^{50}$.
Học sinh đó được 9 điểm khi khoanh đúng 45 câu, khoanh sai 5 câu.
Số cách chọn 45 câu khoanh đúng trong 50 câu là $C_{50}^{45}$. Sau khi chọn 45 câu khoanh đúng, chỉ có 1 cách chọn 5 câu còn lại khoanh sai.

Có 1 cách để khoanh đáp án đúng ở mỗi câu và có 3 cách để khoanh đáp án sai ở mỗi câu.
Vậy xác suất cần tìm là: $\dfrac{C_{50}^{45} \cdot 1^{45} \cdot 3^{5}}{4^{50}}=C_{50}^{45}\left(\dfrac{1}{4}\right)^{45} \cdot\left(\dfrac{3}{4}\right)^{5}$.
Câu 48. Một hộp đựng 11 chiếc thẻ cùng loại, mỗi thẻ được ghi một số nguyên dương không vượt quá 11, hai thẻ khác nhau ghi hai số khác nhau. Lấy ngẫu nhiên đồng thời 2 thẻ. Xác suất của biến cố $A$ : "Tích hai số trên hai thẻ được lấy ra là số lẻ" bằng:
A. $\dfrac{2}{C_{11}^{2}}$
B. $\dfrac{8}{11}$
C. $\dfrac{3}{11}$
D. $\dfrac{2}{A_{11}^{2}}$

## Giải

Mô̂i cách lấy ra đồng thời 2 thẻ là một tổ hợp chập 2 của 11 phần tử. Do đó, số phần tử của không gian mẫu $\Omega$ là: $n(\Omega)=C_{11}^{2}=55$.

Tích của hai số nguyên dương là số lẻ khi và chỉ khi cả hai số là số lẻ. Tập hợp các số nguyên dương lẻ không vượt quá 11 là $\{1 ; 3 ; 5 ; 7 ; 9 ; 11\}$ có 6 phần tử.

Suy ra số phần tử của biến cố $A$ là: $n(A)=C_{6}^{2}=15$
Vậy xác suất của biến cố $A$ là: $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{15}{55}=\dfrac{3}{11}$. Chọn $\mathbf{C}$
Câu 49. Chọn ngẫu nhiên hai số khác nhau từ 30 số nguyên dương đầu tiên. Xác suất để chọn được hai số có tổng là một số chẵn bằng
A. $\dfrac{14}{29}$
B. $\dfrac{28}{29}$
C. $\dfrac{7}{29}$
D. $\dfrac{1}{2}$

## Lời giải

## Chọn A

Gọi $A$ là biến cố "hai số được chọn có tổng là một số chẵn".
$n(\Omega)=C_{30}^{2}=435$.
Tổng của hai số là một số chẵn khi và chỉ khi cả 2 số đó đều chẵn hoặc đều lẻ
$\Rightarrow n(A)=C_{15}^{2}+C_{15}^{2}=210$.
$P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{210}{435}=\dfrac{14}{29}$.
Câu 50. Một lớp có 20 nam sinh và 23 nữ sinh. Giáo viên chọn ngẫu nhiên 5 học sinh đi test Covid. Tính xác suất $P$ để 5 học sinh được chọn có cả nam và nữ.
A. $P \approx 0,85$
B. $P \approx 0,97$
C. $P \approx 0,96$
D. $P \approx 0,95$

## Lời giải

## Chọn D

Số cách chọn 5 học sinh trong 43 học sinh là $C_{43}^{5}=962598$.
Số cách chọn 5 học sinh chỉ có nam hoặc chỉ có nữ là $C_{20}^{5}+C_{23}^{5}=49153$.
Số cách chọn 5 học sinh có cả nam và nữ là $962598-49153=913445$.
$P=\dfrac{913445}{962598} \approx 0,95$.
Câu 51. Một tổ có 10 học sinh nam và 8 học sinh nữ. Chọn ngẫu nhiên đồng thời 5 học sinh. Tính xác suất để trong 5 học sinh được chọn có cả nam và nữ đồng thời số học sinh nam nhiều hơn số học sinh nữ.
A. $\dfrac{3}{5}$
B. $\dfrac{3}{11}$
C. $\dfrac{10}{17} \ldots$
D. $\dfrac{7}{17}$

## Lời giải

## Chọn C

Số phân tử không gian mẫu $n(\Omega)=C_{18}^{5}=8568$.
Các trường hợp thõa mãn yêu cầu bài toán:
TH1: Chọn được 3 nam và 2 nữ: $C_{10}^{3} \cdot C_{8}^{2}=3360$.
TH2: Chọn được 4 nam và 1 nữ: $C_{10}^{4} \cdot C_{8}^{1}=1680$
Vậy có $3360+1680=5040$ cách chọn thỏa mãn.

Suy ra xác suất cần tính là $P=\dfrac{5040}{8568}=\dfrac{10}{17}$.
Câu 52. Một hộp có 37 cái thẻ được đánh số từ 1 đến 37 . Hai thẻ khác nhau được đánh số khác nhau. Rút ngẫu nhiên đồng thời ba thẻ. Tính xác suất để các số ghi trên ba thẻ được rút có tổng là một số chia hết cho 3 .
A. $\dfrac{121}{1295}$
B. $\dfrac{1189}{3385}$
C. $\dfrac{253}{3885}$
D. $\dfrac{433}{1295}$

## Lời giải

## Chọn D

Từ số 1 đến 37 ta có: 12 số chia hết cho 3 ; 13 số chia cho 3 dư 1 ; 12 số chia 3 dư 2 .
Số phần tử không gian mẫu $n(\Omega)=C_{37}^{3}=7770$.
Để lấy được 3 số có tổng chia hết cho 3 ta có các trường hợp sau:

+ TH1: 3 số đều chia hết cho 3 , số cách chọn là $C_{12}^{3}=220$.
+ TH2: 3 số chia cho 3 dư 1, số cách chọn là $C_{13}^{3}=286$.
+ TH3: 3 số chia cho 3 dư 2 , số cách chọn là $C_{12}^{3}=220$.
+ TH4: 1 số chia hết cho 3,1 số chia 3 dư 1,1 số chia 3 dư 2 , số cách là 12.13.12 = 1872 .
Vậy có tất cả $220+286+220+1872=2598$ cách chọn thỏa mãn.
Suy ra xác suất cần tính là $P=\dfrac{2598}{7770}=\dfrac{433}{1295}$.
Câu 53. Trên kệ có 5 quyển sách Tiếng Anh và 7 quyển sách Toán. Lấy ngẫu nhiên ba quyển sách. Xác suất ba quyển lấy ra có cả sách Tiếng Anh và sách Toán là
A. $\dfrac{9}{44}$
B. $\dfrac{1}{22}$
C. $\dfrac{7}{44}$
D. $\dfrac{35}{44}$


## Lời giải

## Chọn D

Gọi không gian mẫu $\Omega \Rightarrow n(\Omega)=C_{12}^{3}=220$ (Lấy 3 trong 12 quyển sách)
Gọi $E$ là " Biến cố lấy được 3 quyển có cả sách Tiếng Anh và Toán " $\Rightarrow \bar{E}$ là " Biến cố lấy được 3 quyển chỉ có một loại Tiếng Anh hoặc Toán " $\Rightarrow n(\bar{E})=C_{5}^{3}+C_{7}^{3}=45$.

Xác suất cần tìm là: $P(E)=1-P(\bar{E})=1-\dfrac{n(\bar{E})}{n(\Omega)}=1-\dfrac{45}{220}=\dfrac{35}{44}$.
Câu 54. Gọi là $X$ tập hợp các số có 4 chữ số khác nhau được lập từ $\{1 ; 2 ; 3 ; 4 ; 5 ; 6 ; 7 ; 8 ; 9\}$. Lấy ngẫu nhiên một số bất kỳ từ tập $X$. Xác suất để số lấy được có mặt đúng hai chữ số chẵn và hai chữ số lẻ là
A. $\dfrac{4}{7}$
B. $\dfrac{11}{21}$
C. $\dfrac{10}{21}$
D. $\dfrac{3}{7}$

## Lời giải

## Chọn C

Gọi không gian mẫu $\Omega$. Mỗi số tự nhiên có 4 chữ số khác nhau lập từ các số của tập A là một chỉnh hợp chập 4 của $9 \Rightarrow n(\Omega)=A_{9}^{4}=3024$.

Gọi $E$ là " Biến cố lấy được số có mặt đúng hai chữ số chẵn và hai chữ số lẻ ", ta có:
Số cách lấy một bộ gồm 2 số chẵn và 2 số lẻ từ tập A là: $C_{4}^{2} \cdot C_{5}^{2}=60$, mỗi bộ như vậy sẽ lập được 4! số suy ra $n(E)=60.4!=1440$. Vậy xác suất cần tìm là $P(E)=\dfrac{n(E)}{n(\Omega)}=\dfrac{1440}{3024}=\dfrac{10}{21}$.

Câu 55. Lấy ngẫu nhiên hai tấm thẻ trong một hộp chứa 9 tấm thẻ đánh số từ 1 đến. Tính xác suất để tổng của các số trên hai thẻ lấy ra là số chẵn.
A. $\dfrac{1}{9}$
B. $\dfrac{5}{3}$
C. $\dfrac{5}{9}$
D. $\dfrac{4}{9}$

## Lời giải

## Chọn D

Số phần tử không gian mẫu là $n(\Omega)=C_{9}^{2}=36$.
Gọi $A$ là biến cố "Tổng của các số trên hai thẻ lấy ra là số chẵn".
Suy ra $n(A)=C_{4}^{2}+C_{5}^{2}=16$.
Vậy xác suất của biến cố $A$ là $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{16}{36}=\dfrac{4}{9}$.
Câu 56. Trong một lớp học gồm có 18 học sinh nam và 17 học sinh nữ. Giáo viên gọi ngẫu nhiên 4 học sinh lên bảng giải bài tập. Xác suất để 4 học sinh được gọi có cả nam và nữ là
A. $\dfrac{69}{77}$
B. $\dfrac{65}{71}$
C. $\dfrac{443}{506}$
D. $\dfrac{68}{75}$

## Lời giải

## Chọn $\underline{\mathbf{A}}$

Số phần tử không gian mẫu là $n(\Omega)=C_{35}^{4}=52360$.
Gọi $A$ là biến cố " 4 học sinh được gọi có cả nam và nữ".
Suy ra $\bar{A}$ là biến cố " 4 học sinh được chỉ có cả nam hoặc nữ".
Suy ra $n(\bar{A})=C_{18}^{4}+C_{17}^{4}=2380+3060=5440 \Rightarrow n(A)=46920$.
Vậy xác suất của biến cố $A$ là $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{69}{77}$.
Câu 57. Chọn ngẫu nhiên hai số phân biệt từ 15 số nguyên dương đầu tiên. Xác suất để tích hai số được chọn là một số chẵn bằng
A. $\dfrac{4}{15}$
B. $\dfrac{4}{5}$
C. $\dfrac{11}{15}$
D. $\dfrac{1}{5}$

## Lời giải

## Chọn C

Số phần tử không gian mẫu là $n(\Omega)=C_{15}^{2}=105$.

Gọi $A$ là biến cố "Tích hai số được chọn là một số chẵn".
Suy ra $n(A)=7.8+C_{7}^{2}=77$.
Vậy xác suất của biến cố $A$ là $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{11}{15}$.
Câu 58. Từ một hộp chứa 9 quả cầu đỏ và 6 quả cầu xanh, lấy ngẫu nhiên đồng thời 3 quả cầu. Xác suất để lấy được 3 quả cầu màu xanh bằng?
A. $\dfrac{5}{21}$
B. $\dfrac{24}{91}$
C. $\dfrac{4}{91}$
D. $\dfrac{12}{65}$

## Lời giải

## Chọn C

Số phần tử không gian mẫu là $n(\Omega)=C_{15}^{3}=455$.
Gọi $A$ là biến cố "Lấy được 3 quả cầu màu xanh".
Suy ra $n(A)=C_{6}^{3}=20$.
Vậy xác suất của biến cố $A$ là $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{4}{91}$.
Câu 59. Một người đi du lịch mang 3 hộp thịt, 2 hộp quả và 3 hộp sữa. Do trời mưa nên các hộp bị mất nhãn. Người đó chọn ngẫu nhiên 3 hộp. Tính xác suất để trong đó có một hộp thịt, một hộp sữa, một hộp quả.
A. $\dfrac{5}{14}$
B. $\dfrac{9}{14}$
C. $\dfrac{9}{28}$
D. $\dfrac{19}{28}$

## Lời giải

## Chọn C

Chọn ngẫu nhiên 3 hộp từ 3 hộp thịt, 2 hộp quả và 3 hộp sữa ta có $n(\Omega)=C_{8}^{3}$.
Để chọn được một hộp thịt, một hộp sữa, một hộp quả ta có $n(\mathrm{~A})=C_{3}^{1} C_{2}^{1} C_{3}^{1}$
Vậy $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{n(\mathrm{~A})=C_{3}^{1} C_{2}^{1} C_{3}^{1}}{C_{8}^{3}}=\dfrac{9}{28}$.
Câu 60. Một hộp đựng 9 chiếc thẻ được đánh số từ 1 đến 9. Rút ngẫu nhiên ra hai thẻ rồi nhân hai số ghi trên hai thẻ lại với nhau. Xác suất để kết quả nhận được là một số chẵn bằng
A. $\dfrac{1}{2}$
B. $\dfrac{13}{18}$
C. $\dfrac{5}{18}$
D. $\dfrac{1}{6}$

## Lời giải

## Chọn.

B. 

Rút ngẫu nhiên hai thẻ từ 9 chiếc thẻ được đánh số từ 1 đến 9 , số cách rút hay $n(\Omega)=C_{9}^{2}$
Gọi A là biến cố: " Tích hai số ghi trên hai thẻ là số chẵn"
Tích hai số là một số chẵn nếu hai số mang nhân có ít nhất 1 số chẵn.
Khi đó $n(A)=C_{4}^{1} \cdot C_{5}^{1}+C_{4}^{2}=26$

Vậy xác suất của biến cố $A$ là $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{13}{18}$.
Câu 61. Bạn Hằng có 6 cuốn sách khoa học và 4 cuốn truyện tranh (các sách khác nhau từng đôi một). Hằng cho Tâm mượn ngẫu nhiên 3 cuốn sách trong số đó để đọc. Tính xác suất của biến cố: "Hằng cho Tâm mượn ít nhất 1 cuốn truyện tranh".
A. $\dfrac{1}{5}$
B. $\dfrac{1}{6}$
C. $\dfrac{5}{6}$
D. $\dfrac{3}{10}$

## Lời giải

## Chọn C

Gọi $\Omega$ là không gian mẫu. $n(\Omega)=C_{10}^{3}=120$.
Gọi $A$ là biến cố: "Hằng cho Tâm mượn ít nhất 1 cuốn truyện tranh".
$\bar{A}$ là biến cố: " Hằng cho Tâm mượn 3 cuốn sách khoa học". $n(\bar{A})=C_{6}^{3}=20$.
Xác suất: $P(\bar{A})=\dfrac{n(\bar{A})}{n(\Omega)}=\dfrac{20}{120}=\dfrac{1}{6} \Rightarrow P(A)=1-P(\bar{A})=\dfrac{5}{6}$.
Câu 62. Có năm tấm bìa được đánh số từ 1 đến 5 . Rút ngẫu nhiên ba tấm. Xác suất của biến cố "Tổng các số trên ba tấm bìa chia hết cho 3 " là
A. $\dfrac{2}{5}$
B. $\dfrac{9}{10}$
C. $\dfrac{1}{10}$
D. $\dfrac{3}{10}$

## Lời giải

## Chọn $\underline{\mathbf{A}}$

Gọi $\Omega$ là không gian mẫu. $n(\Omega)=C_{5}^{3}=10$.
Gọi A là biến cố: "Tổng các số trên ba tấm bìa chia hết cho 3 ".
Các số ghi trên các tấm bìa chia làm 3 nhóm:

- Nhóm 1: các số chia hết cho $3: 3$.
- Nhóm 2: các số chia 3 dư 1: 1;4.
- Nhóm 3: các số chia 3 dư 2: 2;5.

Vì chỉ có 5 số như trên nên muốn tổng 3 số là số chia hết cho 3 thì 3 số lấy ra sẽ có 1 số ở nhóm 1, một số ở nhóm 2, một số ở nhóm 3 .
$n(A)=1.2 .2=4$.
Xác suất $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{4}{10}=\dfrac{2}{5}$.
Câu 63. Một chiếc hộp chứa 20 quả cầu gồm 8 quả màu xanh, 7 quả màu đỏ và 5 quả màu vàng. Lấy ngẫu nhiên 6 quả cầu từ chiếc hộp đó. Xác suất để trong 6 quả cầu lấy được ít nhất một quả màu đỏ bằng:
A. $\dfrac{143}{3230}$
B. $\dfrac{3}{10}$
C. $\dfrac{1287}{6460}$
D. $\dfrac{3087}{3230}$

## Lời giải

## Chọn D

Ta có số phần tử của không gian mẫu là: $n(\Omega)=C_{20}^{6}$.
Gọi $A$ là biến cố: "trong 6 quả cầu lấy được ít nhất một quả màu đỏ"
Gọi $B$ là biến cố: "trong 6 quả cầu lấy được không có quả màu đỏ"
Số phần tử của biến cố là: $n(B)=C_{13}^{6}$
Xác suất $P(B)=\dfrac{n(B)}{n(\Omega)}=\dfrac{143}{3230}$.
Xác suất cần tính là: $P(A)=1-P(B)=\dfrac{3087}{3230}$.
Câu 64. Từ một hộp chứa 6 quả cầu trắng và 3 ba quả cầu đen, lấy ngẫu nhiên đồng thời 3 quả. Xác suất sao cho lấy được 3 quả cùng màu
A. $1$
B. $\dfrac{1}{4}$
C. $3$
D. $4$

## Lời giải

## Chọn B

Hộp có $6+3=9$ quả cầu. Số phần tử của không gian mẫu là: $n(\Omega)=C_{9}^{3}=84$.
Gọi $A$ là biến cố "lấy được 3 quả cùng màu"
TH1: Lấy 3 quả cầu trắng có $C_{6}^{3}=20$ cách.
TH2: Lấy 3 quả cầu đen có $C_{3}^{3}=1$ cách.
$\Rightarrow n(A)=20+1=21$
Xác suất sao cho lấy được 3 quả cùng màu là: $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{21}{84}=\dfrac{1}{4}$.
Câu 65. Từ một hộp chứa 15 quả cầu gồm 10 quả màu đỏ và 5 quả màu xanh, lấy ngẫu nhiên đồng thời hai quả. Xác suất để lấy được 2 quả có màu khác nhau là
A. $\dfrac{10}{21}$
B. $\dfrac{2}{21}$
C. $\dfrac{1}{7}$
D. $\dfrac{3}{7}$

## Lời giải

## Chọn A

Ta có số phần tử của không gian mẫu là: $n(\Omega)=C_{15}^{2}$.
Gọi $A$ là biến cố: "lấy được 2 quả khác màu"
Số phần tử của biến cố là: $n(A)=C_{10}^{1} \cdot C_{5}^{1}$.
Xác suất cần tính là: $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{10}{21}$.

Câu 66. Cho hai hộp, hộp I chứa 4 viên bi đỏ và 3 viên bi xanh, hộp II chứa 5 viên bi đỏ và 2 viên bi xanh. Lấy ngẫu nhiên từ mỗi hộp ra 2 viên bi. Xác suất để các viên bi lấy ra cùng màu là
A. $\dfrac{131}{1001}$
B. $\dfrac{9}{143}$
C. $\dfrac{131}{441}$
D. $\dfrac{1}{7}$

## Lời giải

## Chọn D

Lấy ngẫu nhiên 2 viên bi từ hộp I có $C_{7}^{2}=21$.
Lấy ngẫu nhiên 2 viên bi từ hộp II có $C_{7}^{2}=21$.
Ta có số phần tử của không gian mẫu là: $n(\Omega)=21.21=441$.
Gọi $A$ là biến cố: "các viên bi lấy ra cùng màu".
Số phần tử của biến cố là: $n(A)=C_{4}^{2} \cdot C_{5}^{2}+C_{3}^{2} \cdot C_{2}^{2}$.
Xác suất cần tính là: $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{1}{7}$.
Câu 67. Chọn ngẫu nhiên hai số khác nhau từ 30 số nguyên dương đầu tiên. Xác suất để chọn được hai số có tổng là một số chẵn bằng
A. $\dfrac{14}{29}$
B. $\dfrac{28}{29}$
C. $\dfrac{7}{29}$
D. $\dfrac{1}{2}$

## Lời giải

## Chọn A

Ta có số phần tử của không gian mẫu là: $n(\Omega)=C_{30}^{2}$.
Gọi $A$ là biến cố: "chọn được hai số có tổng là một số chẵn".
TH1: Chọn hai số chẵn có $C_{15}^{2}$
TH2: Chọn hai số lẻ có $C_{15}^{2}$
Số phần tử của biến cố là: $n(A)=2 \cdot C_{15}^{2}$.
Xác suất cần tính là: $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{14}{29}$.
Câu 68. Một hộp chứa 5 viên bi màu trắng, 10 viên bi màu xanh và 15 viên bi màu đỏ. Lấy ngẫu nhiên từ hộp ra 7 viên bi. Xác suất để trong số 7 viên bi được lấy ra có ít nhất 2 viên bi màu đỏ là:
A. $\dfrac{5011}{5220}$
B. $\dfrac{250}{261}$
C. $\dfrac{17}{180}$
D. $\dfrac{20}{261}$

## Lời giải

## Chọn A

Số phần tử của không gian mẫu là: $n(\Omega)=C_{30}^{7}$
Gọi $A$ là biến cố để trong số 7 viên bi được lấy ra có ít nhất 2 viên bi màu đỏ.
$\bar{A}$ là biến cố để trong số 7 viên bi được lấy ra có 1 viên bi màu đỏ và không có viên bị màu đỏ nào. Khi đó: $n(\bar{A})=15 . C_{15}^{6}+C_{15}^{7}=81510$

Vậy xác suất để trong số 7 viên bi được lấy ra có ít nhất 2 viên bi màu đỏ là: $1-\dfrac{n(\bar{A})}{n(\Omega)}=1-\dfrac{81510}{C_{30}^{7}}=\dfrac{5011}{5220}$.
Câu 69. Cho tập hợp $A=\{1 ; 2 ; 3 ; 4 ; 5\}$. Gọi $S$ là tập hợp tất cả các số tự nhiên có 3 chữ số, các chữ số đôi một khác nhau được lập thành từ các chữ số thuộc tập $A$. Chọn ngẫu nhiên hai số từ $S$, tính xác xuất để hai số được chọn đều chia hết cho 3 ?
A. $\dfrac{3}{5}$
B. $\dfrac{46}{295}$
C. $\dfrac{2}{5}$
D. $\dfrac{51}{590}$

## Lời giải

## Chọn D

Gọi $B$ là biến cố "chọn được hai số được chọn đều chia hết cho 3 "
Số các số tự nhiên có ba chữ số tạo nên từ tập $A$ là: $A_{5}^{3}=60$
$n(\Omega)=C_{60}^{2}$
Tập các số gồm ba chữ số tạo thành các số chia hết cho 3 là:
$\{1 ; 2 ; 3\},\{1 ; 3 ; 5\},\{2 ; 3 ; 4\}$
Mỗi tập trên tạo thành 3 ! số chia hết cho 3 , nên có 3.3 ! $=18$ số chia hết cho 3 .
Suy ra: $n(B)=C_{18}^{2}$
$P(B)=\dfrac{n(B)}{n(\Omega)}=\dfrac{C_{18}^{2}}{C_{60}^{2}}=\dfrac{51}{590}$.
Câu 70. Cho đa giác đều có 24 đỉnh. Chọn ngẫu nhiên bốn đỉnh. Tính xác suất chọn ra được hình chữ nhật có các đỉnh là 4 trong 24 đỉnh của đa giác đó.
A. $\dfrac{35}{46}$
B. $\dfrac{11}{46}$
C. $\dfrac{1}{161}$
D. $\dfrac{15}{322}$

## Lời giải

## Chọn C

Số phần tử của không gian mẫu là $n(\Omega)=C_{24}^{4}$
Ta vẽ đường tròn ngoại tiếp đa giác đều 24 đỉnh.Vẽ một đường kính của đường tròn này.Khi đó 2 nửa đường tròn đều chứa 12 đỉnh.

Với mỗi đỉnh thuộc nửa đường tròn thứ nhất ta đều có 1 đỉnh đối xứng với nó qua đường kính và thuộc nưa đường tròn còn lại.

Như vậy cứ 2 đỉnh thuộc đường tròn thứ nhất ta xác định được 2 đỉnh đối xứng với nó qua đường kính và thuộc nửa đường tròn còn lại,bốn đỉnh này tạo thành hình chữ nhật.

Vậy số hình chữ nhật tạo thành từ 4 đa giác đã cho là $C_{12}^{2}$
Xác xuất cần tìm $P=\dfrac{C_{12}^{2}}{C_{24}^{4}}=\dfrac{1}{161}$
Câu 71. Một tổ trong lớp 10 A có 5 bạn nữ và 6 bạn nam. Giáo viên chọn ngẫu nhiên ba bạn trong tổ đó tham gia đội làm báo của lớp. Xác suất để ba bạn được chọn có đúng một bạn nữ là
A. $\dfrac{5}{11}$
B. $\dfrac{29}{33}$
C. $\dfrac{4}{33}$
D. $\dfrac{9}{11}$

## Lời giải

## Chọn A

Không gian mẫu $\Omega$ là các cách chọn ba bạn từ tổ gồm 5 bạn nữ và 6 bạn nam của lớp $10 \mathbf{A}$.
Số phần tử của không gian mẫu là $n(\Omega)=C_{11}^{3}=165$.
Biến cố $A$ là các cách chọn ba bạn sao cho có đúng một bạn nữ.
Chọn 1 bạn nữ từ 5 bạn nữ có $C_{5}^{1}$ cách chọn.
Chọn 2 bạn nam từ 6 bạn nam có $C_{6}^{2}$ cách chọn.
Số phần tử của biến cố $A$ là $C_{5}^{1} \cdot C_{6}^{2}=75$.
Xác suất cần tìm là: $P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{75}{165}=\dfrac{5}{11}$.
Câu 72. Xếp ngẫu nhiên 6 nam và 4 nữ thành hàng ngang. Tính xác suất để không có hai bạn nữ nào đứng cạnh nhau.
A. $\dfrac{1}{6}$
B. $\dfrac{1}{30}$
C. $\dfrac{29}{30}$
D. $\dfrac{1}{210}$

## Lời giải

## Chọn A

Các kết quả của không gian mẫu là các các cách xếp ngẫu nhiên 6 nam và 4 nữ thành hàng ngang có 10 vị trí, nên $n(\Omega)=10$ !; 12345678910
Gọi $A$ : biến cố không có hai bạn nữ nào đứng cạnh nhau.
+) Xếp 6 bạn nam có: $6!=720$ cách;
+) Cứ hai bạn nam có một chỗ trống và có 5 chỗ trống giữa hai nam, và hai chỗ trống ở đầu hàng và cuối hàng;
+) Số cách xếp 4 bạn nữ vào 7 chỗ trống: $A_{7}^{4}=840$ cách
$n(A)=720.840=604800$;
$P(A)=\dfrac{604800}{10!}=\dfrac{1}{6}$.
Câu 73. Một đội gồm 5 nam và 8 nữ. Lập một nhóm gồm 4 người hát tốp ca, tính xác suất để trong 4 người được chọn có ít nhất 3 nữ.
A. $\dfrac{73}{143}$
B. $\dfrac{70}{143}$
C. $\dfrac{87}{143}$
D. $\dfrac{56}{143}$

## Lời giải

## Đáp án B

Chọn ngẫu nhiên 4 người từ 13 có $n(\Omega)=C_{13}^{4}=715$
Gọi A: "4 người được chọn có ít nhất 3 nữ"
$n(A)=C_{8}^{3} \cdot C_{5}^{1}+C_{8}^{4}=350$
$P(A)=\dfrac{n(A)}{n(\Omega)}=\dfrac{70}{143}$
Câu 74. Một tổ học sinh có 7 nữ và 5 nam. Chọn ngẫu nhiên 3 học sinh. Xác suất để trong 3 học sinh được chọn có đúng 1 học sinh nữ bằng
A. $\dfrac{21}{44}$
B. $\dfrac{5}{12}$
C. $\dfrac{7}{22}$
D. $\dfrac{1}{5}$

## Lời giải

## Chọn C

Số cách chọn ngẫu nhiên 3 học sinh của tổ có 7 nữ và 5 nam là $C_{12}^{3}=220$. Do đó, số phần tử của không gian mẫu là $n(\Omega)=220$.
Để chọn ra 3 học sinh có đúng 1 học sinh nữ thì ta chọn ra 1 học sinh nữ và 2 học sinh nam.
Số cách chọn ra 1 học sinh nữ và 2 học sinh nam là $C_{7}^{1} \cdot C_{5}^{2}=70$.
Gọi A là biến cố "chọn ra 3 học sinh có đúng 1 học sinh nữ" thì $n(A)=70$.
Do đó $P(A)=\dfrac{70}{220}=\dfrac{7}{22}$.
Câu 75. Một bình đựng 8 viên bi xanh và 4 viên bi đỏ. Lấy ngẫu nhiên 3 viên bi. Xác suất để có được ít nhất hai viên bi xanh là bao nhiêu?
A. $\dfrac{28}{55}$
B. $\dfrac{14}{55}$
C. $\dfrac{41}{55}$
D. $\dfrac{42}{55}$

## Lời giải

## Chọn D

Số phần tử của không gian mẫu: $n(\Omega)=C_{12}^{3}=220$.
Gọi $A$ là biến cố "lấy được ít nhất hai viên bi xanh".
TH1: Lấy được 2 bi xanh và 1 bi đỏ: $C_{8}^{2} \cdot C_{4}^{1}=112$.
TH2: Lấy được cả 3 đều là bi xanh: $C_{8}^{3}=56$.
Vậy $P(A)=\dfrac{56+112}{220}=\dfrac{42}{55}$.
Câu 76. Một hộp chứa 11 quả cầu gồm 5 quả màu xanh và 6 quả màu đỏ. Chọn ngẫu nhiên đồng thời 2 quả cầu từ hộp đó. Xác suất để 2 quả cầu chọn ra cùng màu là
A. $\dfrac{8}{11}$
B. $\dfrac{5}{22}$
C. $\dfrac{6}{11}$
D. $\dfrac{5}{11}$

## Lời giải

## Chọn D

Gọi $A$ là biến cố " 2 quả cầu chọn ra cùng màu".
Số phần tử của không gian mẫu: $n(\Omega)=C_{11}^{2}=55$.
Trường hợp 1: Hai quả chọn được cùng màu xanh sẽ có $C_{5}^{2}$ khả năng.
Trường hợp 2: Hai quả chọn được cùng màu đỏ sẽ có $C_{6}^{2}$ khả năng.
Vậy $n(A)=C_{5}^{2}+C_{6}^{2}=25$ và $P(A)=\dfrac{25}{55}=\dfrac{5}{11}$.

