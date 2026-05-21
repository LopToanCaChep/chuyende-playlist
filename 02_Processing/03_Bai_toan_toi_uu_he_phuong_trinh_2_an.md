## PHẦN A. KIẾN THỨC CẦN NHỚ

## Biểu diễn miền nghiệm của hệ bất phương trình bậc nhất hai ẩn

Để biểu diễn miền nghiệm của hệ bất phương trình bậc nhất hai ẩn, ta làm như sau:

- **Bước 1.** Trong cùng mặt phẳng tọa độ, biểu diễn miền nghiệm của mỗi bất phương trình trong hệ bằng cách gạch bỏ phần không thuộc miền nghiệm của nó.
- **Bước 2.** Phần không bị gạch là miền nghiệm cần tìm.

**Ví dụ.** Biểu diễn miền nghiệm của hệ bất phương trình: $\left\{\begin{array}{ll}2 x+y \leq 4 & (1) \\ x+y \leq 3 & (2) \\ x \geq 0 & (3) \\ y \geq 0 & (4)\end{array}\right.$

* **Bước 1.** Vẽ các đường thẳng giới hạn:
  * Vẽ đường thẳng $d_1: 2x+y=4$. Chọn $(0; 4)$ và $(2; 0)$.
  * Vẽ đường thẳng $d_2: x+y=3$. Chọn $(0; 3)$ và $(3; 0)$.
  * Đường thẳng $x=0$ là trục tung (trục $Oy$).
  * Đường thẳng $y=0$ là trục hoành (trục $Ox$).

![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-01.jpg?height=588&width=570&top_left_y=1471&top_left_x=790)

* **Lần lượt biểu diễn các miền nghiệm của 4 bất phương trình:**
  * Thử điểm $O(0 ; 0)$ vào (1): $2 \cdot 0+0=0 \leq 4$ (thỏa mãn). Giữ phần chứa điểm $O$, gạch phần không chứa.
  
  ![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-02.jpg?height=650&width=604&top_left_y=75&top_left_x=774)

  * Thử điểm $O(0 ; 0)$ vào (2): $0+0=0 \leq 3$ (thỏa mãn). Giữ phần chứa điểm $O$, gạch phần không chứa.
  
  ![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-02.jpg?height=654&width=597&top_left_y=872&top_left_x=776)

  * Đối với bất phương trình (3): $x \geq 0$. Ta giữ phần $x$ dương (bên phải trục $Oy$), gạch đi phần $x$ âm (bên trái trục $Oy$).
  
  ![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-02.jpg?height=645&width=585&top_left_y=1738&top_left_x=788)

  * Đối với bất phương trình (4): $y \geq 0$. Ta giữ phần $y$ dương (bên trên trục $Ox$), gạch đi phần $y$ âm (bên dưới trục $Ox$).
  
  ![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-03.jpg?height=643&width=591&top_left_y=219&top_left_x=826)

* **Bước 2.** Miền nghiệm của hệ bất phương trình là tứ giác $OABC$ kể cả miền trong, với $O(0 ; 0)$, $A(2 ; 0)$, $B(1 ; 2)$, $C(0 ; 3)$.

![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-03.jpg?height=801&width=743&top_left_y=1025&top_left_x=708)

---

## ỨNG DỤNG CỦA HỆ BẤT PHƯƠNG TRÌNH BẬC NHẤT HAI ẨN

### Phương pháp tìm cực trị của biểu thức $F=a x+b y$ trên một miền đa giác

**Bài toán.** Tìm giá trị lớn nhất, giá trị nhỏ nhất của biểu thức $F=a x+b y$ ($a, b$ là hai số đã cho không đồng thời bằng 0) với $x, y$ thỏa mãn hệ bất phương trình bậc nhất hai ẩn (có miền nghiệm là miền đa giác $A_{1} A_{2} \ldots A_{n}$).

### Phương pháp giải
- **Bước 1.** Xác định miền đa giác $A_{1} A_{2} \ldots A_{n}$ là miền nghiệm của hệ bất phương trình.
- **Bước 2.** Tìm tọa độ các đỉnh $A_{1}, A_{2}, \ldots, A_{n}$.
- **Bước 3.** Tính giá trị biểu thức $F(x_i; y_i)$ tại tọa độ từng đỉnh $A_i(x_i; y_i)$.
- **Bước 4.** So sánh các giá trị tính được và kết luận:
  * Giá trị lớn nhất: $M = \max \{F(A_1), F(A_2), \ldots, F(A_n)\}$.
  * Giá trị nhỏ nhất: $m = \min \{F(A_1), F(A_2), \ldots, F(A_n)\}$.

**Ví dụ 1.** Trong năm nay, một cửa hàng điện lạnh dự định kinh doanh hai loại máy điều hoà: điều hoà hai chiều và điều hoà một chiều với số vốn ban đầu không vượt quá 1,2 tỉ đồng.

| Hạng mục | Điều hoà hai chiều | Điều hoà một chiều |
| :--- | :---: | :---: |
| **Giá mua vào** | 20 triệu đồng / 1 máy | 10 triệu đồng / 1 máy |
| **Lợi nhuận dự kiến** | 3,5 triệu đồng / 1 máy | 2 triệu đồng / 1 máy |

Cửa hàng ước tính rằng tổng nhu cầu của thị trường sẽ không vượt quá 100 máy cả hai loại. Nếu là chủ cửa hàng thì em cần đầu tư kinh doanh mỗi loại bao nhiêu máy để lợi nhuận thu được là lớn nhất?

## Lời giải

Giả sử cửa hàng cần nhập số máy điều hoà hai chiều là $x$ và số máy điều hoà một chiều là $y$. Khi đó ta có $x \geq 0, y \geq 0$.

* Vì nhu cầu của thị trường không quá 100 máy nên: $x+y \leq 100$.
* Số tiền để nhập hai loại máy điều hoà là: $20x + 10y$ (triệu đồng). Số vốn đầu tư không vượt quá 1,2 tỉ đồng (1200 triệu đồng) nên ta có: $20x + 10y \leq 1200 \Leftrightarrow 2x + y \leq 120$.

Từ đó ta thu được hệ bất phương trình bậc nhất hai ẩn sau:
$$\left\{\begin{array}{l}x \geq 0 \\ y \geq 0 \\ x+y \leq 100 \\ 2 x+y \leq 120\end{array}\right.$$

![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-04.jpg?height=659&width=670&top_left_y=1841&top_left_x=749)

Lợi nhuận thu được khi bán $x$ máy điều hòa hai chiều và $y$ máy điều hoà một chiều là $F(x ; y) = 3,5x + 2y$ (triệu đồng). Ta cần tìm giá trị lớn nhất của $F(x ; y)$ trên miền nghiệm của hệ bất phương trình trên.

- **Bước 1.** Xác định miền nghiệm là miền tứ giác $OABC$ với tọa độ các đỉnh: $O(0 ; 0)$, $A(0 ; 100)$, $B(20 ; 80)$, $C(60 ; 0)$.
- **Bước 2.** Tính giá trị của biểu thức $F$ tại các đỉnh của tứ giác này:
  * $F(0 ; 0) = 0$
  * $F(0 ; 100) = 2 \cdot 100 = 200$
  * $F(20 ; 80) = 3,5 \cdot 20 + 2 \cdot 80 = 230$
  * $F(60 ; 0) = 3,5 \cdot 60 = 210$
- **Bước 3.** So sánh các giá trị thu được, ta được giá trị lớn nhất là $F(20 ; 80) = 230$.

**Kết luận:** Cửa hàng cần đầu tư kinh doanh 20 máy điều hoà hai chiều và 80 máy điều hoà một chiều để lợi nhuận thu được là lớn nhất.

---

## PHẦN C. BÀI TẬP TRẮC NGHIỆM

## DÀNH CHO HỌC SINH TRUNG BÌNH

Câu 1. Giá trị nhỏ nhất của biểu thức $F=y-x$ trên miền xác định bởi hệ $\left\{\begin{array}{c}2 x+y \leq 2 \\ x-y \leq 2 \\ 5 x+y \geq-4\end{array}\right.$ là
A. $\min F=-3$ khi $x=1, y=-2$.
B. $\min F=0$ khi $x=0, y=0$.
C. $\min F=-2$ khi $x=\frac{4}{3}, y=-\frac{2}{3}$.
D. $\min F=8$ khi $x=-2, y=6$.

## Lời giải

Biểu diễn miền nghiệm của hệ bất phương trình trên hệ trục tọa độ như dưới đây:
![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-05.jpg?height=538&width=661&top_left_y=1537&top_left_x=836)

Giá trị nhỏ nhất của biểu thức $F=y-x$ đạt được tại một trong các đỉnh của tam giác $ABC$ là $A(-2 ; 6)$, $B\left(-\frac{1}{3} ; -\frac{7}{3}\right)$, $C\left(\frac{4}{3} ; -\frac{2}{3}\right)$.
Ta có: 
* $F(A) = 6 - (-2) = 8$
* $F(B) = -\frac{7}{3} - \left(-\frac{1}{3}\right) = -2$
* $F(C) = -\frac{2}{3} - \frac{4}{3} = -2$

Vậy $\min F = -2$ khi $x=\frac{4}{3}, y=-\frac{2}{3}$ hoặc $x=-\frac{1}{3}, y=-\frac{7}{3}$. Đối chiếu các phương án ta chọn C.

## Chọn C

Câu 2. Giá trị nhỏ nhất của biểu thức $F(x ; y)=x-2 y$ với điều kiện $\left\{\begin{array}{c}0 \leq y \leq 5 \\ x \geq 0 \\ x+y-2 \geq 0 \\ x-y-2 \leq 0\end{array}\right.$ là
A. -10.
B. 12.
C. -8.
D. -6.

## Lời giải

Biểu diễn miền nghiệm của hệ bất phương trình trên hệ trục tọa độ:
![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-06.jpg?height=634&width=721&top_left_y=511&top_left_x=808)

Nhận thấy biểu thức $F(x; y) = x - 2y$ đạt giá trị nhỏ nhất tại một trong các đỉnh $A(7; 5)$, $B(0; 5)$, $C(0; 2)$, $D(2; 0)$.
Ta tính giá trị tại các đỉnh:
* $F(A) = 7 - 2 \cdot 5 = -3$
* $F(B) = 0 - 2 \cdot 5 = -10$
* $F(C) = 0 - 2 \cdot 2 = -4$
* $F(D) = 2 - 2 \cdot 0 = 2$

Vậy $\min F = -10$ khi $x=0, y=5$.

## Chọn A

Câu 3. Biểu thức $F=y-x$ đạt giá trị nhỏ nhất với điều kiện $\left\{\begin{array}{c}-2 x+y \leq-2 \\ x-2 y \leq 2 \\ x+y \leq 5 \\ x \geq 0\end{array}\right.$ tại điểm $S(x ; y)$ có toạ độ là
A. $(4 ; 1)$.
B. $(3 ; 1)$.
C. $(2 ; 1)$.
D. $(1 ; 1)$.

## Lời giải

Biểu diễn miền nghiệm của hệ bất phương trình trên hệ trục tọa độ:
![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-06.jpg?height=556&width=620&top_left_y=2177&top_left_x=858)

Nhận thấy biểu thức $F=y-x$ đạt giá trị nhỏ nhất tại một trong các đỉnh $A(1; 0)$, $B(2; 0)$, $C(4; 1)$ hoặc đỉnh giao điểm khác.
Ta xét điểm $C(4 ; 1)$ thuộc miền nghiệm.
Tại $C(4; 1)$, ta có $F(C) = 1 - 4 = -3$.
Đây là điểm đạt giá trị nhỏ nhất của biểu thức $F$. Vậy toạ độ điểm $S$ là $(4; 1)$.

## Chọn A

Câu 4. Biểu thức $L=y-x$, với $x$ và $y$ thỏa mãn hệ bất phương trình $\left\{\begin{array}{l}2 x+3 y-6 \leq 0 \\ x \geq 0 \\ 2 x-3 y-1 \leq 0\end{array}\right.$, đạt giá trị lớn nhất là $a$ và đạt giá trị nhỏ nhất là $b$. Hãy chọn kết quả đúng trong các kết quả sau:
A. $a=\frac{25}{8}$ và $b=-2$.
B. $a=2$ và $b=-\frac{11}{12}$.
C. $a=3$ và $b=0$.
D. $a=3$ và $b=\frac{-9}{8}$.

## Lời giải

Trước hết, ta vẽ ba đường thẳng giới hạn miền nghiệm:
* $d_1: 2x+3y-6=0$
* $d_2: x=0$
* $d_3: 2x-3y-1=0$

Miền nghiệm là hình tam giác $ABC$ (kể cả biên), với các đỉnh:
* $A(0 ; 2)$
* $B\left(\frac{7}{4} ; \frac{5}{6}\right)$
* $C\left(0 ; -\frac{1}{3}\right)$

![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-07.jpg?height=231&width=273&top_left_y=1247&top_left_x=776)

Tính giá trị của $L = y-x$ tại các đỉnh:
* $L(A) = 2 - 0 = 2$
* $L(B) = \frac{5}{6} - \frac{7}{4} = -\frac{11}{12}$
* $L(C) = -\frac{1}{3} - 0 = -\frac{1}{3}$

So sánh các giá trị trên, ta được giá trị lớn nhất $a = 2$ (tại $A$) và giá trị nhỏ nhất $b = -\frac{11}{12}$ (tại $B$).

## Chọn B

## DÀNH CHO HỌC SINH KHÁ GIỎI

Câu 5. Trong một cuộc thi pha chế, hai đội $A, B$ được sử dụng tối đa 24 g hương liệu, 9 lít nước và 210 g đường để pha chế nước cam và nước táo. Để pha chế 1 lít nước cam cần 30 g đường, 1 lít nước và 1 g hương liệu; pha chế 1 lít nước táo cần 10 g đường, 1 lít nước và 4 g hương liệu. Mỗi lít nước cam nhận được 60 điểm thưởng, mỗi lít nước táo nhận được 80 điểm thưởng. Đội A pha chế được $a$ lít nước cam và $b$ lít nước táo và dành được điểm thưởng cao nhất. Hiệu số $a-b$ là
A. 1.
B. 3.
C. -1.
D. -6.

## Lời giải

Gọi $x, y$ lần lượt là số lít nước cam và nước táo mà đội A cần pha chế ($x \geq 0 ; y \geq 0$).
* Lượng đường sử dụng: $30x + 10y \leq 210$ (g).
* Lượng nước sử dụng: $x + y \leq 9$ (lít).
* Lượng hương liệu sử dụng: $x + 4y \leq 24$ (g).

Ta có hệ bất phương trình:
$$\left\{\begin{array}{l}30 x+10 y \leq 210 \\ x+y \leq 9 \\ x+4 y \leq 24 \\ x \geq 0 ; y \geq 0\end{array}\right.$$

Số điểm thưởng đạt được là $M(x, y) = 60x + 80y$. Ta cần tìm giá trị lớn nhất của $M(x, y)$ trên miền nghiệm của hệ bất phương trình.

Biểu diễn miền nghiệm của hệ trên mặt phẳng tọa độ:
![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-08.jpg?height=655&width=990&top_left_y=1025&top_left_x=670)

Miền nghiệm thu được là ngũ giác $OEDAB$ với các đỉnh:
* $O(0; 0)$
* $E(0; 6)$
* $A(4; 5)$
* $B(6; 3)$
* $C(7; 0)$ (tương ứng điểm trên trục hoành)

Tính giá trị $M(x, y)$ tại các đỉnh:
* $M(O) = 0$
* $M(E) = 60 \cdot 0 + 80 \cdot 6 = 480$
* $M(A) = 60 \cdot 4 + 80 \cdot 5 = 640$
* $M(B) = 60 \cdot 6 + 80 \cdot 3 = 600$
* $M(C) = 60 \cdot 7 + 80 \cdot 0 = 420$

Như vậy, điểm thưởng cao nhất đạt được là 640 điểm khi $x = 4$ và $y = 5$. Do đó $a = 4, b = 5 \Rightarrow a - b = -1$.

## Chọn C

Câu 6. Một công ty TNHH trong một đợt quảng cáo và bán khuyến mãi hàng hóa (1 sản phẩm mới của công ty) cần thuê xe để chở trên 140 người và trên 9 tấn hàng. Nơi thuê chỉ có hai loại xe A và B. Trong đó xe loại A có 10 chiếc, xe loại B có 9 chiếc. Một chiếc xe loại A cho thuê với giá 4 triệu, loại B giá 3 triệu. Hỏi phải thuê bao nhiêu xe mỗi loại để chi phí vận chuyển là thấp nhất. Biết rằng xe A chỉ chở tối đa 20 người và 0,6 tấn hàng. Xe B chở tối đa 10 người và 1,5 tấn hàng.
A. 4 xe A và 5 xe B.
B. 5 xe A và 6 xe B.
C. 5 xe A và 4 xe B.
D. 6 xe A và 4 xe B.

## Lời giải

Gọi $x$ là số xe loại A ($0 \leq x \leq 10 ; x \in \mathbb{N}$), $y$ là số xe loại B ($0 \leq y \leq 9 ; y \in \mathbb{N}$).
* Chi phí thuê xe cần tối thiểu hóa là: $T = 4x + 3y$ (triệu đồng).
* Điều kiện về số người chở được: $20x + 10y \geq 140$.
* Điều kiện về khối lượng hàng chở được: $0,6x + 1,5y \geq 9$.

Ta có hệ bất phương trình:
$$\left\{\begin{array}{l}0 \leq x \leq 10 \\ 0 \leq y \leq 9 \\ 20 x+10 y \geq 140 \\ 0,6 x+1,5 y \geq 9\end{array}\right.$$

Biểu diễn miền nghiệm của hệ trên mặt phẳng tọa độ:
![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-09.jpg?height=736&width=1023&top_left_y=900&top_left_x=657)

Miền nghiệm là miền tứ giác $ABCD$ kể cả biên với các đỉnh:
* $A(10 ; 2)$
* $B(10 ; 9)$
* $C(2,5 ; 9)$
* $D(5 ; 4)$

Tính chi phí $T$ tại các đỉnh:
* $T(A) = 4 \cdot 10 + 3 \cdot 2 = 46$
* $T(B) = 4 \cdot 10 + 3 \cdot 9 = 67$
* $T(C) = 4 \cdot 2,5 + 3 \cdot 9 = 37$
* $T(D) = 4 \cdot 5 + 3 \cdot 4 = 32$

Chi phí thấp nhất đạt được là $T_{\min} = 32$ triệu đồng khi thuê 5 xe loại A và 4 xe loại B.

## Chọn C

Câu 7. Một gia đình cần ít nhất 900 đơn vị protein và 400 đơn vị lipit trong thức ăn mỗi ngày. Mỗi kilogam thịt bò chứa 800 đơn vị protein và 200 đơn vị lipit. Mỗi kilogam thịt lợn chứa 600 đơn vị protein và 400 đơn vị lipit. Biết rằng gia đình này chỉ mua nhiều nhất $1,6 \text{ kg}$ thịt bò và $1,1 \text{ kg}$ thịt lợn. Giá tiền một kg thịt bò là 160 nghìn đồng, 1 kg thịt lợn là 110 nghìn đồng. Gọi $x, y$ lần lượt là số kg thịt bò và thịt lợn mà gia đình đó cần mua để tổng số tiền họ phải trả là ít nhất mà vẫn đảm bảo lượng protein và lipit trong thức ăn. Tính $x^2+y^2$.
A. $x^2+y^2=1,3$.
B. $x^2+y^2=2,6$.
C. $x^2+y^2=1,09$.
D. $x^2+y^2=0,58$.

## Lời giải

Ta có các điều kiện ràng buộc đối với lượng thịt bò $x$ (kg) và thịt lợn $y$ (kg):
* $0 \leq x \leq 1,6$
* $0 \leq y \leq 1,1$
* Lượng protein: $800x + 600y \geq 900 \Leftrightarrow 8x + 6y \geq 9$
* Lượng lipit: $200x + 400y \geq 400 \Leftrightarrow x + 2y \geq 2$

Ta được hệ bất phương trình:
$$\left\{\begin{array}{l}0 \leq x \leq 1,6 \\ 0 \leq y \leq 1,1 \\ 8 x+6 y \geq 9 \\ x+2 y \geq 2\end{array}\right.$$

Tổng số tiền chi tiêu là $T = 160x + 110y$ (nghìn đồng).

Biểu diễn miền nghiệm của hệ bất phương trình trên mặt phẳng tọa độ:
![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-10.jpg?height=510&width=563&top_left_y=1948&top_left_x=886)

Miền nghiệm là tứ giác $ABCD$ với tọa độ các đỉnh:
* $A(0,3 ; 1,1)$
* $B(1,6 ; 1,1)$
* $C(1,6 ; 0,2)$
* $D(0,6 ; 0,7)$ - giao điểm của $8x+6y=9$ và $x+2y=2$

Tính chi phí $T$ tại các đỉnh:
* $T(A) = 160 \cdot 0,3 + 110 \cdot 1,1 = 169$ (nghìn đồng)
* $T(B) = 160 \cdot 1,6 + 110 \cdot 1,1 = 377$ (nghìn đồng)
* $T(C) = 160 \cdot 1,6 + 110 \cdot 0,2 = 278$ (nghìn đồng)
* $T(D) = 160 \cdot 0,6 + 110 \cdot 0,7 = 173$ (nghìn đồng)

Chi phí nhỏ nhất đạt được khi $x = 0,3$ và $y = 1,1$.
Khi đó: $x^2 + y^2 = 0,3^2 + 1,1^2 = 0,09 + 1,21 = 1,3$.

## Chọn A

Câu 8. Có hai cái giỏ đựng trứng gồm giỏ A và giỏ B, các quả trứng trong mỗi giỏ đều có hai loại là trứng lành và trứng hỏng. Tổng số trứng trong hai giỏ là 20 quả và số trứng trong giỏ A nhiều hơn số trứng trong giỏ B. Lấy ngẫu nhiên mỗi giỏ 1 quả trứng, biết xác suất để lấy được hai quả trứng lành là $\frac{55}{84}$. Tìm số trứng lành trong giỏ A.
A. 6.
B. 14.
C. 11.
D. 10.

## Lời giải

Gọi $a$ là số trứng lành trong giỏ A, $N_A$ là tổng số trứng trong giỏ A.
Gọi $b$ là số trứng lành trong giỏ B, $N_B$ là tổng số trứng trong giỏ B.
* Ta có tổng số trứng là $N_A + N_B = 20$. Do $N_A > N_B$ nên $N_A \geq 11$.
* Xác suất lấy ra từ mỗi giỏ 1 quả trứng lành là:
  $$P = \frac{a}{N_A} \cdot \frac{b}{N_B} = \frac{55}{84}$$
* Vì $\frac{a \cdot b}{N_A \cdot N_B} = \frac{55}{84}$, ta suy ra tích $N_A \cdot N_B$ phải là bội của 84.
* Đồng thời ta có: $N_A \cdot N_B \leq \left(\frac{N_A + N_B}{2}\right)^2 = 10^2 = 100$.
* Bội số duy nhất của 84 nhỏ hơn hoặc bằng 100 là chính nó: $N_A \cdot N_B = 84$.
* Từ hệ $\left\{\begin{array}{l}N_A + N_B = 20 \\ N_A \cdot N_B = 84\end{array}\right.$ với $N_A > N_B$, ta tìm được $N_A = 14$ và $N_B = 6$.
* Khi đó: $\frac{a \cdot b}{14 \cdot 6} = \frac{55}{84} \Rightarrow a \cdot b = 55$.
* Vì $a \leq N_A = 14$ và $b \leq N_B = 6$, ước số của 55 thỏa mãn điều kiện chỉ có $a = 11, b = 5$.

Vậy số trứng lành trong giỏ A là 11 quả.

## Chọn C

Câu 9. Một xưởng cơ khí có hai công nhân là Chiến và Bình. Xưởng sản xuất loại sản phẩm $I$ và $II$. Mỗi sản phẩm $I$ bán lãi 500 nghìn đồng, mỗi sản phẩm $II$ bán lãi 400 nghìn đồng. Để sản xuất được một sản phẩm $I$ thì Chiến phải làm việc trong 3 giờ, Bình phải làm việc trong 1 giờ. Để sản xuất được một sản phẩm $II$ thì Chiến phải làm việc trong 2 giờ, Bình phải làm việc trong 6 giờ. Một người không thể làm được đồng thời hai sản phẩm. Biết rằng trong một tháng Chiến không thể làm việc quá 180 giờ và Bình không thể làm việc quá 220 giờ. Số tiền lãi lớn nhất trong một tháng của xưởng là
A. 32 triệu đồng.
B. 35 triệu đồng.
C. 14 triệu đồng.
D. 30 triệu đồng.

## Lời giải

Gọi $x, y$ lần lượt là số sản phẩm loại $I$ và loại $II$ được sản xuất ra ($x, y \geq 0$).
* Tổng thời gian Chiến làm việc: $3x + 2y \leq 180$ (giờ).
* Tổng thời gian Bình làm việc: $x + 6y \leq 220$ (giờ).

Ta có hệ bất phương trình:
$$\left\{\begin{array}{l}3 x+2 y \leq 180 \\ x+6 y \leq 220 \\ x \geq 0 \\ y \geq 0\end{array}\right. (*)$$

Miền nghiệm của hệ bất phương trình (*) được biểu diễn trên hình vẽ dưới đây:
![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-12.jpg?height=414&width=748&top_left_y=50&top_left_x=794)

Tiền lãi thu được trong một tháng của xưởng là $T = 0,5x + 0,4y$ (triệu đồng).
Biểu thức $T$ sẽ đạt cực đại tại một trong các đỉnh của tứ giác:
* $O(0; 0)$
* $A(60 ; 0)$
* $B(40 ; 30)$ - giao điểm của $3x+2y=180$ và $x+6y=220$
* $C\left(0 ; \frac{110}{3}\right)$

Tính giá trị $T$ tại các đỉnh:
* $T(O) = 0$
* $T(A) = 0,5 \cdot 60 = 30$ (triệu đồng)
* $T(B) = 0,5 \cdot 40 + 0,4 \cdot 30 = 32$ (triệu đồng)
* $T(C) = 0,4 \cdot \frac{110}{3} \approx 14,67$ (triệu đồng)

Vậy tiền lãi lớn nhất trong một tháng của xưởng là 32 triệu đồng khi sản xuất 40 sản phẩm loại $I$ và 30 sản phẩm loại $II$.

## Chọn A

Câu 10. Một gia đình cần ít nhất 900 đơn vị protein và 400 đơn vị lipit trong thức ăn mỗi ngày. Mỗi kilogam thịt bò chứa 800 đơn vị protein và 200 đơn vị lipit. Mỗi kilogam thịt lợn chứa 600 đơn vị protein và 400 đơn vị lipit. Biết rằng gia đình này chỉ mua nhiều nhất $1,6 \text{ kg}$ thịt bò và $1,1 \text{ kg}$ thịt lợn. Giá tiền một kg thịt bò là 160 nghìn đồng, một kg thịt lợn là 110 nghìn đồng. Gọi $x, y$ lần lượt là số kg thịt bò và thịt lợn mà gia đình đó cần mua. Tìm $x, y$ để tổng số tiền họ phải trả là ít nhất mà vẫn đảm bảo lượng protein và lipit trong thức ăn?
A. $x=0,3$ và $y=1,1$.
B. $x=0,3$ và $y=0,7$.
C. $x=0,6$ và $y=0,7$.
D. $x=1,6$ và $y=0,2$.

## Lời giải

Tương tự Câu 7, bài toán yêu cầu tìm cặp số $(x; y)$ để tổng số tiền họ phải trả là ít nhất mà vẫn đảm bảo lượng dinh dưỡng.
Hệ bất phương trình ràng buộc:
$$\left\{\begin{array}{l}0 \leq x \leq 1,6 \\ 0 \leq y \leq 1,1 \\ 8 x+6 y \geq 9 \\ x+2 y \geq 2\end{array}\right.$$

Hàm mục tiêu chi phí: $T = 160x + 110y$ (nghìn đồng).

Miền nghiệm của hệ bất phương trình được biểu diễn trên hình vẽ dưới đây:
![](https://cdn.mathpix.com/cropped/9cb78aa4-36e6-4b78-a5b1-f4de1c0013b3-13.jpg?height=496&width=709&top_left_y=57&top_left_x=813)

Tọa độ các đỉnh của đa giác nghiệm:
* $A(1,6 ; 1,1)$
* $B(1,6 ; 0,2)$
* $C(0,6 ; 0,7)$
* $D(0,3 ; 1,1)$

So sánh giá trị chi phí $T$ tại các đỉnh:
* $T(A) = 377$ nghìn đồng
* $T(B) = 278$ nghìn đồng
* $T(C) = 173$ nghìn đồng
* $T(D) = 169$ nghìn đồng

Như vậy, giá trị nhỏ nhất của chi phí là 169 nghìn đồng khi mua $x = 0,3$ kg thịt bò và $y = 1,1$ kg thịt lợn.

## Chọn A
