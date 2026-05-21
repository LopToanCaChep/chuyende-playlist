## PHẦN A. KIẾN THỨC CẦN NHỚ

## 1. ĐẠO HÀM BẰNG ĐỊNH NGHĨA

Hàm số $y=f(x)$ xác định trên $(a; b)$ và điểm $x_{0} \in(a; b)$. Công thức đạo hàm của hàm số $y=f(x)$ tại điểm $x_{0}$:
- $\displaystyle f^{\prime}\left(x_{0}\right)=\lim _{x \rightarrow x_{0}} \frac{f(x)-f\left(x_{0}\right)}{x-x_{0}}$

Nếu đặt $\Delta x = x - x_{0}$ (số gia biến số) và $\Delta y = f(x) - f\left(x_{0}\right)$ (số gia hàm số), ta có:
- $\displaystyle f^{\prime}\left(x_{0}\right)=\lim _{\Delta x \rightarrow 0} \frac{\Delta y}{\Delta x}$

## 2. QUY TẮC ĐẠO HÀM VÀ CÔNG THỨC SƠ CẤP

### 🔹 Các quy tắc cơ bản
- $(u+v)^{\prime}=u^{\prime}+v^{\prime}$
- $(u-v)^{\prime}=u^{\prime}-v^{\prime}$
- $(k.u)^{\prime}=k.u^{\prime}$ (với $k$ là số thực)
- $(u.v)^{\prime}=u^{\prime}v+v^{\prime}u$
- $\displaystyle \left(\frac{u}{v}\right)^{\prime}=\frac{u^{\prime}v-v^{\prime}u}{v^{2}}$

### 🔹 Đạo hàm sơ cấp và Đạo hàm hàm hợp
| Đạo hàm Sơ cấp | Đạo hàm Hàm hợp (với $u = u(x)$) |
| :--- | :--- |
| $\left(x^{n}\right)^{\prime}=n.x^{n-1}$ | $\left(u^{n}\right)^{\prime}=n.u^{n-1}.u^{\prime}$ |
| $\displaystyle (\sqrt{x})^{\prime}=\frac{1}{2\sqrt{x}}$ | $\displaystyle (\sqrt{u})^{\prime}=\frac{u^{\prime}}{2\sqrt{u}}$ |
| $\displaystyle \left(\frac{1}{x}\right)^{\prime}=-\frac{1}{x^{2}}$ | $\displaystyle \left(\frac{1}{u}\right)^{\prime}=-\frac{u^{\prime}}{u^{2}}$ |
| $(\sin x)^{\prime}=\cos x$ | $(\sin u)^{\prime}=u^{\prime}.\cos u$ |
| $(\cos x)^{\prime}=-\sin x$ | $(\cos u)^{\prime}=-u^{\prime}.\sin u$ |
| $\displaystyle (\tan x)^{\prime}=\frac{1}{\cos ^{2}x}$ | $\displaystyle (\tan u)^{\prime}=\frac{u^{\prime}}{\cos ^{2}u}$ |
| $\displaystyle (\cot x)^{\prime}=-\frac{1}{\sin ^{2}x}$ | $\displaystyle (\cot u)^{\prime}=-\frac{u^{\prime}}{\sin ^{2}u}$ |
| $\left(e^{x}\right)^{\prime}=e^{x}$ | $\left(e^{u}\right)^{\prime}=u^{\prime}.e^{u}$ |
| $\left(a^{x}\right)^{\prime}=a^{x}.\ln a$ | $\left(a^{u}\right)^{\prime}=u^{\prime}.a^{u}.\ln a$ |
| $\displaystyle (\ln x)^{\prime}=\frac{1}{x}$ | $\displaystyle (\ln u)^{\prime}=\frac{u^{\prime}}{u}$ |
| $\displaystyle \left(\log _{a} x\right)^{\prime}=\frac{1}{x.\ln a}$ | $\displaystyle \left(\log _{a} u\right)^{\prime}=\frac{u^{\prime}}{u.\ln a}$ |

### 🔹 Công thức tính nhanh đạo hàm phân thức
- Hàm bậc 1 / Bậc 1: $\displaystyle \left(\frac{ax+b}{cx+d}\right)^{\prime}=\frac{ad-bc}{(cx+d)^{2}}$
- Hàm bậc 2 / Bậc 2: $\displaystyle \left(\frac{ax^{2}+bx+c}{dx^{2}+ex+f}\right)^{\prime}=\frac{(ae-bd)x^{2}+2(af-cd)x+(bf-ce)}{\left(dx^{2}+ex+f\right)^{2}}$

## 3. ỨNG DỤNG CỦA ĐẠO HÀM

### 🔹 Phương trình tiếp tuyến (PTTT)
Phương trình tiếp tuyến của đồ thị hàm số $y=f(x)$ tại tiếp điểm $M\left(x_{0} ; y_{0}\right)$:
**$y = f^{\prime}\left(x_{0}\right).(x - x_{0}) + y_{0}$**
*(Trong đó: $x_{0}$ là hoành độ tiếp điểm, $y_{0}$ là tung độ tiếp điểm, $f^{\prime}(x_{0})$ là hệ số góc $k$)*

| Các dạng toán thường gặp |
| :--- |
| **Dạng 1: Viết PTTT tại điểm $M(x_{0}; y_{0})$** <br> **B1:** Tính $f^{\prime}(x)$ <br> **B2:** Thay $M(x_{0}; y_{0})$ chính là tiếp điểm nên áp dụng công thức: $y = f^{\prime}(x_{0})(x - x_{0}) + y_{0}$ <br> **Lưu ý:** <br> - Cho $x_{0}$ thì ta thay vào $f(x)$ tìm được $y_{0}$ <br> - Cho $y_{0}$ thì ta giải phương trình $y_{0} = f(x)$ tìm được $x_{0}$ |
| **Dạng 2: Biết hệ số góc $k$** <br> **B1:** Gọi $M(x_{0}; y_{0})$ là tiếp điểm và tính $f^{\prime}(x)$ <br> **B2:** Giải phương trình $f^{\prime}(x_{0}) = k$ tìm được $x_{0}$, từ đó suy ra $y_{0}$ <br> **B3:** Phương trình tiếp tuyến $y = k(x - x_{0}) + y_{0}$ <br> **Lưu ý:** <br> 1. Tiếp tuyến $d \parallel \Delta: y=ax+b$ thì $k = a$ <br> 2. Tiếp tuyến $d \perp \Delta: y=ax+b$ thì $k.a = -1$ <br> 3. Tiếp tuyến tạo với trục hoành một góc $\alpha$ thì $k = \pm \tan \alpha$ <br> 4. Tiếp tuyến cắt $Ox, Oy$ lần lượt tại $A$ và $B$ sao cho $OB = m.OA$ thì $k = \pm m$ |
| **Dạng 3: Viết PTTT đi qua điểm $A(x_{A}; y_{A})$** <br> **B1:** Phương trình qua $A$ có dạng $d: y = k(x - x_{A}) + y_{A}$ <br> **B2:** Điều kiện để $d$ là PTTT là hệ sau có nghiệm: $\begin{cases} f(x) = k(x - x_{A}) + y_{A} \\ f^{\prime}(x) = k \end{cases}$ <br> **B3:** Thay $k = f^{\prime}(x)$ vào phương trình trên ta giải tìm được $x$. Có $x$ thay lại tìm được $k$. Từ đó thay $k$ vào $d$ tìm được PTTT. |

### 🔹 Ứng dụng trong vật lý
- Vận tốc tức thời tại thời điểm $t$: $v(t) = s^{\prime}(t)$
- Gia tốc tức thời tại thời điểm $t$: $a(t) = v^{\prime}(t)$


## PHẦN C. BÀI TẬP TRẮC NGHIỆM

## DÀNH CHO HỌC SINH TRUNG BÌNH

Câu 1. Phát biểu nào trong các phát biểu sau là đúng?
A. Nếu hàm số $y=f(x)$ có đạo hàm trái tại $x_{0}$ thì nó liên tục tại điểm đó.
B. Nếu hàm số $y=f(x)$ có đạo hàm phải tại $x_{0}$ thì nó liên tục tại điểm đó.
C. Nếu hàm số $y=f(x)$ có đạo hàm tại $x_{0}$ thì nó liên tục tại điểm $-x_{0}$.
D. Nếu hàm số $y=f(x)$ có đạo hàm tại $x_{0}$ thì nó liên tục tại điểm đó.

## Lời giải

## Chọn D

Ta có định lí sau:
Nếu hàm số $y=f(x)$ có đạo hàm tại $x_{0}$ thì nó liên tục tại điểm đó.

Câu 2. Cho hàm số $y=f(x)$ có đạo hàm tại $x_{0}$ là $f^{\prime}\left(x_{0}\right)$. Khẳng định nào sau đây là sai?
A. $f^{\prime}\left(x_{0}\right)=\lim _{x \rightarrow x_{0}} \frac{f\left(x+x_{0}\right)-f\left(x_{0}\right)}{x-x_{0}}$.
B. $f^{\prime}\left(x_{0}\right)=\lim _{\Delta x \rightarrow 0} \frac{f\left(x_{0}+\Delta \mathrm{x}\right)-f\left(x_{0}\right)}{\Delta x}$.
C. $f^{\prime}\left(x_{0}\right)=\lim _{x \rightarrow x_{0}} \frac{f(x)-f\left(x_{0}\right)}{x-x_{0}}$.
D. $f^{\prime}\left(x_{0}\right)=\lim _{h \rightarrow 0} \frac{f\left(\mathrm{~h}+x_{0}\right)-f\left(x_{0}\right)}{h}$.

## Lời giải

## Chọn A

Theo định nghĩa đạo hàm của hàm số tại một điểm
Câu 3. Cho hàm số $y=f(x)$ xác định trên $\mathbb{R}$ thỏa mãn $\lim _{x \rightarrow 3} \frac{f(x)-f(3)}{x-3}=2$. Kết quả đúng là
A. $f^{\prime}(2)=3$.
B. $f^{\prime}(x)=2$.
C. $f^{\prime}(x)=3$.
D. $f^{\prime}(3)=2$.

## Lời giải

## Chọn D

Theo định nghĩa đạo hàm của hàm số tại một điểm ta có
$\lim _{x \rightarrow 3} \frac{f(x)-f(3)}{x-3}=2=f^{\prime}(3)$.
Câu 4. Cho hàm số $y=f(x)$ có đạo hàm thỏa mãn $f^{\prime}(6)=2$. Giá trị của biểu thức $\lim _{x \rightarrow 6} \frac{f(x)-f(6)}{x-6}$ bằng
A. 12 .
B. 2 .
C. $\frac{1}{3}$.
D. $\frac{1}{2}$.

## Lời giải

## Chọn B

Hàm số $y=f(x)$ có tập xác định là $D$ và $x_{0} \in D$. Nếu tồn tại giới hạn (hữu hạn) $\lim _{x \rightarrow x_{0}} \frac{f(x)-f\left(x_{0}\right)}{x-x_{0}}$ thì giới hạn gọi là đạo hàm của hàm số tại $x_{0}$

Vậy kết quả của biểu thức $\lim _{x \rightarrow 6} \frac{f(x)-f(6)}{x-6}=f^{\prime}(6)=2$.
Câu 5. Tiếp tuyến của đồ thị hàm số $y=\frac{x+1}{2 x-3}$ tại điểm có hoành độ $x_{0}=-1$ có hệ số góc bằng
A. 5 .
B. $-\frac{1}{5}$.
c. -5 .
D. $\frac{1}{5}$.

## Lời giải

## Chọn B

TXĐ: $D=\mathbb{R} \backslash\left\{\frac{3}{2}\right\}$
Ta có $f^{\prime}(x)=\frac{-5}{(2 x-3)^{2}}$
Hệ số góc của tiếp tuyến của đồ thị hàm số tại điểm có hoành độ $x_{0}=-1$ :
$f^{\prime}(-1)=\frac{-5}{(2 \cdot(-1)-3)^{2}}=\frac{-1}{5}$
Câu 6. Viết phương trình tiếp tuyến của đồ thị hàm số $y=x^{4}-4 x^{2}+5$ tại điểm có hoành độ $x=-1$.
A. $y=4 x-6$.
B. $y=4 x+2$.
C. $y=4 x+6$.
D. $y=4 x-2$.

## Lời giải

## Chọn C

Ta có $y^{\prime}=4 x^{3}-8 x, y^{\prime}(-1)=4$.
Điểm thuộc đồ thị đã cho có hoành độ $x=-1$ là: $M(-1 ; 2)$.
Vậy phương trình tiếp tuyến của đồ thị hàm số tại $M(-1 ; 2)$ là:
$y=y^{\prime}(-1)(x+1)+2 \Leftrightarrow y=4(x+1)+2 \Leftrightarrow y=4 x+6$.

Câu 7. Tiếp tuyến của đồ thị hàm số $y=\frac{2 x+3}{x-2}$ tại điểm có hoành độ bằng 3 , tương ứng là
A. $y=7 x+13$.
B. $y=-7 x+30$.
C. $y=3 x+9$.
D. $y=-x-2$.

## Lời giải

## Chọn B

$x=3 \Rightarrow y=9 ;$
$y^{\prime}=\frac{-7}{(x-2)^{2}} \Rightarrow y^{\prime}(3)=-7$.
Phương trình tiếp tuyến tương ứng là $y=-7(x-3)+9 \Leftrightarrow y=-7 x+30$.
Câu 8. Cho hàm số $y=\frac{1}{3} x^{3}+x^{2}-2 x+1$ có đồ thị là $(C)$. Phương trình tiếp tuyến của ( $C$ ) tại điểm $M\left(1 ; \frac{1}{3}\right)$ là:
A. $y=3 x-2$.
B. $y=-3 x+2$.
C. $y=x-\frac{2}{3}$.
D. $y=-x+\frac{2}{3}$

## Lời giải

## Chọn C

$y^{\prime}=\mathrm{x}^{2}+2 x-2$
$y^{\prime}(1)=1+2-2=1$
Phương trình tiếp tuyến của ( $C$ ) tại điểm $M\left(1 ; \frac{1}{3}\right)$ là:
$y=y^{\prime}(1)(x-1)+\frac{1}{3}=x-1+\frac{1}{3}=x-\frac{2}{3}$

Câu 9. Viết phương trình tiếp tuyến của đồ thị hàm số $y=x^{3}-3 x$ tại điểm có hoành độ bằng 2 .
A. $y=-9 x+16$.
B. $y=-9 x+20$.
C. $y=9 x-20$.
D. $y=9 x-16$.

## Lời giải

## Chọn D

$y^{\prime}=3 x^{2}-3$
Ta có $y(2)=2$ và $y^{\prime}(2)=9$. Do đó PTTT cần tìm là: $y=9(x-2)+2 \Leftrightarrow y=9 x-16$
Câu 10. Phương trình tiếp tuyến của đồ thị $(C): y=3 x-4 x^{2}$ tại điểm có hoành độ $x_{0}=0$ là
A. $y=0$.
B. $y=3 x$.
C. $y=3 x-2$.
D. $y=-12 x$.

## Lời giải

## Chọn B

Tập xác định $D=\mathbb{R}$.
Đạo hàm $y^{\prime}=3-8 x$.
Phương trình tiếp tuyến: $y=y_{(0)}^{\prime} \cdot(x-0)+y_{(0)} \Rightarrow \Delta: y=3 x$.
Câu 11. Cho hàm số $y=-x^{3}+3 x-2$ có đồ thị ( $C$ ). Viết phương trình tiếp tuyến của ( $C$ ) tại giao điểm của ( $C$ ) với trục tung.
A. $y=-2 x+1$.
B. $y=2 x+1$.
C. $y=3 x-2$.
D. $y=-3 x-2$.

## Lời giải

## Chọn C

+) $y^{\prime}=-3 x^{2}+3$
+) Giao điểm của $(C)$ với trục tung có tọa độ là $(0 ;-2)$.
+) Tiếp tuyến của $(C)$ tại điểm $(0 ;-2)$ có phương trình là:
$y=y^{\prime}(0)(x-0)-2 \Leftrightarrow y=3 x-2$.
Câu 12. Viết phương trình tiếp tuyến của đồ thị $(C): y=x^{4}-8 x^{2}+9$ tại điểm M có hoành độ bằng -1 .
A. $y=12 x+14$.
B. $y=12 x-14$.
C. $y=12 x+10$.
D. $y=-20 x-22$.

## Lời giải

## Chọn A

Tập xác định $\mathbb{R}$.
$y^{\prime}=4 x^{3}-16 x . \Rightarrow y^{\prime}(-1)=12$.
$\mathrm{M}\left(-1 ; \mathrm{y}_{0}\right) \in(C) \Leftrightarrow y_{0}=2$.
Tiếp tuyến của đồ thị $(C)$ tại $\mathrm{M}(-1 ; 2)$ có phương trình là $y=y^{\prime}(-1)(x+1)+2 \Leftrightarrow y=12 x+14$.
Vậy tiếp tuyến cần tìm có phương trình là $y=12 x+14$.
Câu 13. Cho hàm số $y=\frac{x-2}{x+1}$. Viết phương trình tiếp tuyến của đồ thị hàm số trên tại điểm có hoành độ $x_{0}=0$.
A. $y=3 x-2$.
B. $y=-3 x-2$.
C. $y=3 x-3$.
D. $y=3 x+2$.

## Lời giải

## Chọn A

Tập xác định $D=\mathbb{R} \backslash\{-1\}$.
$y=\frac{x-2}{x+1} \Rightarrow y^{\prime}=\frac{3}{(x+1)^{2}}$.
$y(0)=-2, y^{\prime}(0)=3$
⇒ phương trình tiếp tuyến của đồ thị hàm số trên tại điểm có hoành độ $x_{0}=0$ là $y=3(x-0)-2 \Leftrightarrow y=3 x-2$.

Câu 14. Cho hàm số $y=x^{3}-2 x+1$ có đồ thị $(C)$. Hệ số góc $k$ của tiếp tuyến với ( $C$ ) tại điểm có hoành độ bằng 1 bằng
A. $k=-5$.
B. $k=10$.
C. $k=25$.
D. $k=1$.

## Lời giải

## Chọn D

Ta có $y^{\prime}=3 x^{2}-2$.
Hệ số góc $k$ của tiếp tuyến với $(C)$ tại điểm có hoành độ bằng 1 bằng $k=y^{\prime}(1)=1$.
Câu 15. Tiếp tuyến của đồ thị hàm số $y=\frac{-x+1}{3 x-2}$ tại giao điểm của đồ thị hàm số với trục tung có hệ số góc là
A. -1 .
B. $\frac{1}{4}$.
C. $-\frac{5}{4}$.
D. $-\frac{1}{4}$.

## Lời giải

## Chọn D

Ta có: $y^{\prime}=\frac{-1}{(3 x-2)^{2}}$.
Gọi $M$ là tọa độ giao điểm của đồ thị hàm số với trục tung $\Rightarrow M\left(0 ;-\frac{1}{2}\right)$.

Vậy hệ số góc cần tìm là: $k=y^{\prime}(0)=-\frac{1}{4}$.
Câu 16. Một chất điểm chuyển động có phương trình $s=2 t^{2}+3 t$ ( $t$ tính bằng giây, $s$ tính bằng mét). Vận tốc của chất điểm tại thời điểm $t_{0}=2$ (giây) bằng
A. $22(m / s)$.
B. $19(m / s)$.
C. $9(\mathrm{~m} / \mathrm{s})$.
D. $11(m / s)$.

## Lời giải

## Chọn D

Vận tốc của chất điểm tại thời điểm $t_{0}=2$ (giây) là: $v(2)=s^{\prime}(2)=11 \mathrm{~m} / \mathrm{s}$
Câu 17. Một chất điểm chuyển động có vận tốc tức thời $v(t)$ phụ thuộc vào thời gian $t$ theo hàm số $v(t)=-t^{4}+8 t^{2}+500$. Trong khoảng thời gian $t=0$ đến $t=5$ chất điểm đạt vận tốc lớn nhất tại thời điểm nào?
A. $t=1$.
B. $t=4$.
C. $t=2$.
D. $t=0$.

## Lời giải

## Chọn C

Ta tính $v^{\prime}(t)=-4 t^{3}+16 t=0 \Leftrightarrow\left[\begin{array}{l}t=0 \\ t=-2(L) \\ t=2\end{array}\right.$
Ta có $v(0)=500, v(2)=516, v(5)=75$
Hàm số $v(t)$ liên tục trên $[0 ; 5]$ nên chất điểm đạt vận tốc lớn nhất tại thời điểm $t=2$.
Câu 18. Một chất điểm chuyển động thẳng được xác định bởi phương trình $s=t^{3}-3 t^{2}+5 t+2$, trong đó $t$ tính bằng giây và $s$ tính bằng mét. Gia tốc của chuyển động khi $t=3$ là:
A. $12 m / s^{2}$.
B. $17 \mathrm{~m} / \mathrm{s}^{2}$.
C. $24 m / s^{2}$.
D. $14 m / s^{2}$.

## Lời giải:

## Chọn A

Ta có: Vận tốc của chuyển động $v(t)=s^{\prime}(t)=3 t^{2}-6 t+5$.
Gia tốc của chuyển động $a(t)=v^{\prime}(\mathrm{t})=6 \mathrm{t}-6$. Khi $t=3 \Rightarrow a(t)=12 \mathrm{~m} / \mathrm{s}^{2}$.
Câu 19. Một vật chuyển động theo quy luật $s(t)=-\frac{1}{2} t^{3}+12 t^{2}, t$ (giây) là khoảng thời gian tính từ lúc vật bắt đầu chuyển động, $s$ (mét) là quãng đường vật chuyển động trong $t$ giây. Vận tốc tức thời của vật tại thời điểm $t=10$ (giây) là:
A. $80(\mathrm{~m} / \mathrm{s})$.
B. $90(\mathrm{~m} / \mathrm{s})$.
C. $100(\mathrm{~m} / \mathrm{s})$.
D. $70(\mathrm{~m} / \mathrm{s})$.

## Lời giải

## Chọn B

Vận tốc tức thời của vật tại thời điểm $t$ là: $v(t)=s^{\prime}(t)=-\frac{3}{2} t^{2}+24 t$.
Vận tốc tức thời của vật tại thời điểm $t=10$ (giây) là: $v(10)=-\frac{3}{2} 10^{2}+24.10=90(\mathrm{~m} / \mathrm{s})$.
Câu 20. Một vật chuyển động theo quy luật $s=-\frac{1}{2} t^{3}+9 t^{2}$ với $t$ (giây) là khoảng thời gian tính từ lúc bắt đầu chuyển động và $s$ (mét) là quãng đường vật đi được trong khoảng thời gian đó. Hỏi trong khoảng thời gian 10 giây, kể từ lúc bắt đầu chuyển động, vận tốc lớn nhất của vật đạt được bằng bao nhiêu?
A. $216(m / s)$.
B. $30(\mathrm{~m} / \mathrm{s})$.
C. $400(\mathrm{~m} / \mathrm{s})$.
D. $54(\mathrm{~m} / \mathrm{s})$

## Lời giải

## Chọn D

Vận tốc tại thời điểm $t$ là $v(t)=s^{\prime}(t)=-\frac{3}{2} t^{2}+18 t$ với $t \in[0 ; 10]$.
Ta có : $v^{\prime}(t)=-3 t+18=0 \Leftrightarrow t=6$.
Suy ra: $v(0)=0 ; v(10)=30 ; v(6)=54$. Vậy vận tốc lớn nhất của vật đạt được bằng $54(\mathrm{~m} / \mathrm{s})$.
Câu 21. Tính đạo hàm của hàm số $f(x)=\frac{2 x+7}{x+4}$ tại $x=2$ ta được:
A. $f^{\prime}(2)=\frac{1}{36}$.
B. $f^{\prime}(2)=\frac{11}{6}$.
C. $f^{\prime}(2)=\frac{3}{2}$.
D. $f^{\prime}(2)=\frac{5}{12}$.

## Lời giải

## Chọn A

Ta có $f^{\prime}(x)=\frac{1}{(x+4)^{2}} \Rightarrow f^{\prime}(2)=\frac{1}{36}$.

Câu 22. Tính đạo hàm của hàm số $y=x(x+1)(x+2)(x+3)$ tại điểm $x_{0}=0$ là:
A. $y^{\prime}(0)=5$.
B. $y^{\prime}(0)=6$.
C. $y^{\prime}(0)=0$.
D. $y^{\prime}(0)=-6$.

## Lời giải

## Chọn B

Ta có $y=x(x+1)(x+2)(x+3)=(x^{2}+x)(x^{2}+5x+6)$
$\Rightarrow y^{\prime}=(2x+1)(x^{2}+5x+6)+(x^{2}+x)(2x+5)$
$\Rightarrow y^{\prime}(0)=6$.
Câu 23. Tính đạo hàm của hàm số $y=\sqrt{x}+x$ tại điểm $x_{0}=4$ là:
A. $y^{\prime}(4)=\frac{9}{2}$.
B. $y^{\prime}(4)=6$.
C. $y^{\prime}(4)=\frac{3}{2}$.
D. $y^{\prime}(4)=\frac{5}{4}$.

## Lời giải

## Chọn D

Ta có $y^{\prime}=\frac{1}{2 \sqrt{x}}+1 \Rightarrow y^{\prime}(4)=\frac{1}{2 \sqrt{4}}+1=\frac{5}{4}$.
Câu 24. Đạo hàm của hàm số $y=5 \sin x-3 \cos x$ tại $x_{0}=\frac{\pi}{2}$ là:
A. $y^{\prime}\left(\frac{\pi}{2}\right)=3$.
B. $y^{\prime}\left(\frac{\pi}{2}\right)=5$.
C. $y^{\prime}\left(\frac{\pi}{2}\right)=-3$.
D. $y^{\prime}\left(\frac{\pi}{2}\right)=-5$.

## Lời giải

## Chọn A

Ta có: $y^{\prime}=5 \cos x+3 \sin x \Rightarrow y^{\prime}\left(\frac{\pi}{2}\right)=3$.
Câu 25. Cho hàm số $y=\frac{x+2}{x-1}$. Tính $y^{\prime}(3)$
A. $\frac{5}{2}$.
B. $-\frac{3}{4}$.
C. $-\frac{3}{2}$.
D. $\frac{3}{4}$.

## Lời giải

## Chọn B

Ta có $y=\frac{x+2}{x-1} \Rightarrow y^{\prime}=\frac{-3}{(x-1)^{2}}$
$y^{\prime}(3)=\frac{-3}{(3-1)^{2}}=-\frac{3}{4}$.

Câu 26. Cho hàm số $f(x)=\frac{3 x+1}{\sqrt{x^{2}+4}}$. Tính giá trị biểu thức $f^{\prime}(0)$.
A. -3 .
B. -2 .
C. $\frac{3}{2}$.
D. 3 .

## Lời giải

## Chọn C

Cách 1: Tập xác định $D=\mathbb{R}$.
$f^{\prime}(x)=\frac{3 \sqrt{x^{2}+4}-(3 x+1) \cdot \frac{x}{\sqrt{x^{2}+4}}}{\left(\sqrt{x^{2}+4}\right)^{2}}=\frac{12-x}{\sqrt[2]{\left(x^{2}+4\right)^{3}}}$
$\Rightarrow f^{\prime}(0)=\frac{3}{2}$.
Câu 27. Tính đạo hàm của hàm số $y=x^{3}+2 x+1$.
A. $y^{\prime}=3 x^{2}+2 x$.
B. $y^{\prime}=3 x^{2}+2$.
C. $y^{\prime}=3 x^{2}+2 x+1$.
D. $y^{\prime}=x^{2}+2$.

## Lời giải

## Chọn B

Ta có: $y^{\prime}=3 x^{2}+2$.
Câu 28. Khẳng định nào sau đây sai
A. $y=x \Rightarrow y^{\prime}=1$.
B. $y=x^{3} \Rightarrow y^{\prime}=3 x^{2}$.
C. $y=x^{5} \Rightarrow y^{\prime}=5 x$.
D. $y=x^{4} \Rightarrow y^{\prime}=4 x^{3}$.

## Lời giải

## Chọn C

+) Ta có: $y=x^{n} \Rightarrow y^{\prime}=n \cdot x^{n-1}, \forall n \in \mathbb{N}^{*}$ do đó các mệnh đề $\mathrm{A}, \mathrm{B}, \mathrm{D}$ đúng.
Vì $y=x^{5} \Rightarrow y^{\prime}=5 x^{4}$ nên mệnh đề C sai.
Câu 29. Đạo hàm của hàm số $y=-x^{3}+3 m x^{2}+3\left(1-m^{2}\right) x+m^{3}-m^{2}$ (với $m$ là tham số) bằng
A. $3 x^{2}-6 m x-3+3 m^{2}$.
B. $-x^{2}+3 m x-1-3 m$.
C. $-3 x^{2}+6 m x+1-m^{2}$.
D. $-3 x^{2}+6 m x+3-3 m^{2}$.



## Chọn D

Câu 30. Đạo hàm của hàm số $y=\frac{x^{4}}{2}+\frac{5 x^{3}}{3}-\sqrt{2 x}+a^{2}$ ( $a$ là hằng số) bằng.
A. $2 x^{3}+5 x^{2}-\frac{1}{\sqrt{2 x}}+2 a$.
B. $2 x^{3}+5 x^{2}+\frac{1}{2 \sqrt{2 x}}$.
C. $2 x^{3}+5 x^{2}-\frac{1}{\sqrt{2 x}}$.
D. $2 x^{3}+5 x^{2}-\sqrt{2}$.

## Lời giải

## Chọn C

Ta có $y^{\prime}=2 x^{3}+5 x^{2}-\frac{1}{\sqrt{2 x}}$.
Câu 31. Hàm số nào sau đây có đạo hàm bằng $\frac{1}{\sqrt{2 x}}$ ?
A. $f(x)=2 \sqrt{x}$.
B. $f(x)=\sqrt{x}$.
C. $f(x)=\sqrt{2 x}$.
D. $f(x)=-\frac{1}{\sqrt{2 x}}$.

## Lời giải

## Chọn C

Ta có $f^{\prime}(x)=(\sqrt{2 x})^{\prime}=\frac{1}{\sqrt{2 x}}$.
Câu 32. Cho các hàm số $u=u(x), v=v(x)$ có đạo hàm trên khoảng $J$ và $v(x) \neq 0$ với $\forall x \in J$. Mệnh đề nào sau đây sai?
A. $[u(x)+v(x)]^{\prime}=u^{\prime}(x)+v^{\prime}(x)$.
B. $\left[\frac{1}{v(x)}\right]^{\prime}=\frac{v^{\prime}(x)}{v^{2}(x)}$.
C. $[u(x) \cdot v(x)]^{\prime}=u^{\prime}(x) \cdot v(x)+v^{\prime}(x) \cdot u(x)$.
D. $\left[\frac{u(x)}{v(x)}\right]^{\prime}=\frac{u^{\prime}(x) \cdot v(x)-v^{\prime}(x) \cdot u(x)}{v^{2}(x)}$.



## Chọn B

Câu 33. Tính đạo hàm của hàm số $y=x^{2}-\frac{1}{x}$.
A. $y^{\prime}=2 x-\frac{1}{x^{2}}$.
B. $y^{\prime}=x-\frac{1}{x^{2}}$.
C. $y^{\prime}=x+\frac{1}{x^{2}}$.
D. $y^{\prime}=2 x+\frac{1}{x^{2}}$.

## Lời giải

## Chọn D

Tập xác định $D=\mathbb{R} \backslash\{0\}$
Có $y^{\prime}=2 x+\frac{1}{x^{2}}$.
Câu 34. Tính đạo hàm của hàm số $y=\frac{2 x}{x-1}$
A. $y^{\prime}=\frac{2}{(x-1)^{2}}$.
B. $y^{\prime}=\frac{2}{(x-1)}$.
C. $y^{\prime}=\frac{-2}{(x-1)^{2}}$.
D. $y^{\prime}=\frac{-2}{(x-1)}$.

## Lời giải

## Chọn C

$y=\frac{2 x}{x-1} \Rightarrow y^{\prime}=\frac{-2}{(x-1)^{2}}$.
Câu 35. Hàm số $y=\frac{1}{x^{2}+5}$ có đạo hàm bằng:
A. $y^{\prime}=\frac{1}{\left(x^{2}+5\right)^{2}}$.
B. $y^{\prime}=\frac{2 x}{\left(x^{2}+5\right)^{2}}$.
C. $y^{\prime}=\frac{-1}{\left(x^{2}+5\right)^{2}}$.
D. $y^{\prime}=\frac{-2 x}{\left(x^{2}+5\right)^{2}}$.

## Lời giải

## Chọn D

$y^{\prime}=\frac{-2 x}{\left(x^{2}+5\right)^{2}}$
Câu 36. Cho hàm số $y=x^{3}-3 x+2017$. Bất phương trình $y^{\prime}<0$ có tập nghiệm là:
A. $S=(-1 ; 1)$.
B. $S=(-\infty ;-1) \cup(1 ;+\infty)$.
C. $(1 ;+\infty)$.
D. $(-\infty ;-1)$.

## Lời giải

## Chọn A

$y=x^{3}-3 x+2017 \Rightarrow y^{\prime}=3 x^{2}-3, y^{\prime}<0 \Leftrightarrow x^{2}-1<0 \Leftrightarrow-1<x<1$.
Câu 37. Cho hàm số $f(x)=x^{4}+2 x^{2}-3$. Tìm $x$ để $f^{\prime}(x)>0$ ?
A. $-1<x<0$.
B. $x<0$.
C. $x>0$.
D. $x<-1$.

## Lời giải

## Chọn C

$f^{\prime}(x)>0 \Leftrightarrow 4 x^{3}+4 x>0 \Leftrightarrow 4 x\left(x^{2}+1\right)>0 \Leftrightarrow x>0$.
Câu 38. Cho hàm số $u(x)$ có đạo hàm tại $x$ là $u^{\prime}$. Khi đó đạo hàm của hàm số $y=\sin ^{2} u$ tại $x$ là
A. $y^{\prime}=\sin 2 u$.
B. $y^{\prime}=u^{\prime} \sin 2 u$.
C. $y^{\prime}=2 \sin 2 u$.
D. $y^{\prime}=2 u^{\prime} \sin 2 u$.

## Lời giải

## Chọn B

Ta có $y^{\prime}=\left(\sin ^{2} u\right)^{\prime}=2 \sin u \cdot(\sin u)^{\prime}=2 \sin u \cdot \cos u \cdot u^{\prime}=u^{\prime} \sin 2 u$.
Câu 39. Tính đạo hàm của hàm số $y=\sin 2 x-\cos x$
A. $y^{\prime}=2 \cos x+\sin x$.
B. $y^{\prime}=\cos 2 x+\sin x$.
C. $y^{\prime}=2 \cos 2 x+\sin x$.
D. $y^{\prime}=2 \cos x-\sin x$.

## Lời giải

## Chọn C

$y=\sin 2 x-\cos x \Rightarrow y^{\prime}=2 \cos 2 x+\sin x$.
Câu 40. Đạo hàm của hàm số $y=4 \sin 2 x+7 \cos 3 \mathrm{x}+9$ là
A. $8 \cos 2 x-21 \sin 3 x+9$.
B. $8 \cos 2 x-21 \sin 3 x$.
C. $4 \cos 2 x-7 \sin 3 x$.
D. $4 \cos 2 x+7 \sin 3 x$.

## Lời giải

## Chọn B

Ta có: $y^{\prime}=8 \cos 2 x-21 \sin 3 x$.
Câu 41. Tính đạo hàm của hàm số $f(x)=\sin x+\cos x+3$ là:
A. $f^{\prime}(x)=\sin x-\cos x$.
B. $f^{\prime}(x)=\cos x+\sin x+3$.
C. $f^{\prime}(x)=\cos x-\sin x$.
D. $f^{\prime}(x)=-\sin x-\cos x$.



## Chọn C.

Câu 42. Đạo hàm của hàm số $y=\cos 2 x+1$ là
A. $y^{\prime}=-\sin 2 x$.
B. $y^{\prime}=2 \sin 2 x$.
C. $y^{\prime}=-2 \sin 2 x+1$.
D. $y^{\prime}=-2 \sin 2 x$.

## Lời giải

## Chọn D

Ta có $y=\cos 2 x+1 \Rightarrow y^{\prime}=(\cos 2x+1)^{\prime}=-(2x)^{\prime} \sin 2x+(1)^{\prime}=-2 \sin 2 x$.
Câu 43. Đạo hàm của hàm số $y=\cos (2 x+1)$ là:
A. $y^{\prime}=2 \sin (2 x+1)$
B. $y^{\prime}=-2 \sin (2 x+1)$
C. $y^{\prime}=-\sin (2 x+1)$
D. $y^{\prime}=\sin (2 x+1)$.

## Lời giải

## Chọn B

$y=\cos (2 x+1) \Rightarrow y^{\prime}=-(2 x+1)^{\prime} \cdot \sin (2 x+1)=-2 \sin (2 x+1)$
Câu 44. Đạo hàm của hàm số $f(x)=\sin ^{2} x$ là:
A. $f^{\prime}(x)=2 \sin x$.
B. $f^{\prime}(x)=2 \cos x$.
C. $f^{\prime}(x)=-\sin (2 x)$.
D. $f^{\prime}(x)=\sin (2 x)$.

## Lời giải

## Chọn D

$f^{\prime}(x)=2 \sin x .(\sin x)^{\prime}=2 \sin x . \cos x=\sin 2 x$.
Câu 45. Tìm đạo hàm của hàm số $y=\tan x$.
A. $y^{\prime}=-\frac{1}{\cos ^{2} x}$.
B. $y^{\prime}=\frac{1}{\cos ^{2} x}$.
C. $y^{\prime}=\cot x$.
D. $y^{\prime}=-\cot x$.

## Lời giải

## Chọn B

Ta có: $y=\tan x \Rightarrow y^{\prime}=\frac{1}{\cos ^{2} x}$.
Câu 46. Tính đạo hàm của hàm số $y=x \sin x$
A. $y=\sin x-x \cos x$.
B. $y=x \sin x-\cos x$.
C. $y=\sin x+x \cos x$.
D. $y=x \sin x+\cos x$.

## Lời giải

## Chọn C

Áp dụng công thức tính đạo hàm của một tích $(u . v)^{\prime}=u^{\prime} v+v^{\prime} u$ ta có
$(x \sin x)^{\prime}=(x)^{\prime} \sin x+x(\sin x)^{\prime}=\sin x+x \cos x$
Vậy $y=x \sin x \Rightarrow y^{\prime}=\sin x+x \cos x$
Câu 47. Tập xác định của hàm số $y=8^{x}$ là
A. $\mathbb{R} \backslash\{0\}$.
B. $\mathbb{R}$.
C. $[0 ;+\infty)$.
D. $(0 ;+\infty)$.

## Lời giải

## Chọn B

Tập xác định của hàm số $y=8^{x}$ là $\mathbb{R}$
Câu 48. Tập xác định của hàm số $y=6^{x}$ là
A. $[0 ;+\infty)$.
B. $\mathbb{R} \backslash\{0\}$.
C. $(0 ;+\infty)$.
D. $\mathbb{R}$.

## Lời giải

## Chọn D

Tập xác định của hàm số $y=6^{x}$ là $D=\mathbb{R}$.

Câu 49. Tập xác định của hàm số $y=7^{x}$ là
A. $\mathbb{R} \backslash\{0\}$.
B. $[0 ;+\infty)$.
C. $(0 ;+\infty)$.
D. $\mathbb{R}$.



## Chọn D

Câu 50. Tìm đạo hàm của hàm số $y=\log x$.
A. $y^{\prime}=\frac{\ln 10}{x}$
B. $y^{\prime}=\frac{1}{x \ln 10}$
C. $y^{\prime}=\frac{1}{10 \ln x}$
D. $y^{\prime}=\frac{1}{x}$

## Lời giải

## Chọn B

Áp dụng công thức $\left(\log _{a} x\right)^{\prime}=\frac{1}{x \ln a}$, ta được $y^{\prime}=\frac{1}{x \ln 10}$.
Câu 51. Hàm số $y=2^{x^{2}-x}$ có đạo hàm là
A. $2^{x^{2}-x} \cdot \ln 2$.
B. $(2 x-1) \cdot 2^{x^{2}-x} \cdot \ln 2$.
C. $\left(x^{2}-x\right) \cdot 2^{x^{2}-x-1}$.
D. $(2 x-1) \cdot 2^{x^{2}-x}$.

## Lời giải

## Chọn B

Ta có $y^{\prime}=\left(x^{2}-x\right)^{\prime} \cdot 2^{x^{2}-x} \cdot \ln 2=(2 x-1) \cdot 2^{x^{2}-x} \cdot \ln 2$.
Câu 52. Hàm số $y=3^{x^{2}-x}$ có đạo hàm là
A. $(2 x-1) \cdot 3^{x^{2}-x}$.
B. $\left(x^{2}-x\right) \cdot 3^{x^{2}-x-1}$.
C. $(2 x-1) \cdot 3^{x^{2}-x} \cdot \ln 3$.
D. $3^{x^{2}-x} \cdot \ln 3$.

## Lời giải

## Chọn C

Ta có: $\left(a^{u}\right)^{\prime}=u^{\prime} \cdot a^{u} \cdot \ln a$ nên $\left(3^{x^{2}-x}\right)^{\prime}=(2 x-1) \cdot 3^{x^{2}-x} \cdot \ln 3$.
Câu 53. Tính đạo hàm của hàm số $y=13^{x}$
A. $y^{\prime}=\frac{13^{x}}{\ln 13}$
B. $y^{\prime}=x \cdot 13^{x-1}$
C. $y^{\prime}=13^{x} \ln 13$
D. $y^{\prime}=13^{x}$

## Lời giải

## Chọn C

Ta có: $y^{\prime}=13^{x} \ln 13$.
Câu 54. Tính đạo hàm của hàm số $y=\log _{2}(2 x+1)$.
A. $y^{\prime}=\frac{2}{(2 x+1) \ln 2}$
B. $y^{\prime}=\frac{1}{(2 x+1) \ln 2}$
C. $y^{\prime}=\frac{2}{2 x+1}$
D. $y^{\prime}=\frac{1}{2 x+1}$

## Lời giải

## Chọn A

Ta có $y^{\prime}=\left(\log _{2}(2 x+1)\right)^{\prime}=\frac{(2 x+1)^{\prime}}{(2 x+1) \ln 2}=\frac{2}{(2 x+1) \ln 2}$.
Câu 55. Tính đạo hàm của hàm số $y=\frac{x+1}{4^{x}}$
A. $y^{\prime}=\frac{1-2(x+1) \ln 2}{2^{2 x}}$
B. $y^{\prime}=\frac{1+2(x+1) \ln 2}{2^{2 x}}$
C. $y^{\prime}=\frac{1-2(x+1) \ln 2}{2^{x^{2}}}$
D. $y^{\prime}=\frac{1+2(x+1) \ln 2}{2^{x^{2}}}$

## Lời giải

## Chọn A

Ta có: $y^{\prime}=\frac{(x+1)^{\prime} \cdot 4^{x}-(x+1) \cdot\left(4^{x}\right)^{\prime}}{\left(4^{x}\right)^{2}}=\frac{4^{x}-(x+1) \cdot 4^{x} \cdot \ln 4}{\left(4^{x}\right)^{2}} =\frac{4^{x} \cdot(1-x \cdot \ln 4-\ln 4)}{\left(4^{x}\right)^{2}}=\frac{1-x \cdot 2 \ln 2-2 \ln 2}{4^{x}}=\frac{1-2(x+1) \ln 2}{2^{2 x}}$.

Câu 56. Hàm số $f(x)=\log _{2}\left(x^{2}-2 \mathrm{x}\right)$ có đạo hàm
A. $f^{\prime}(x)=\frac{\ln 2}{x^{2}-2 \mathrm{x}}$
B. $f^{\prime}(x)=\frac{1}{\left(x^{2}-2 \mathrm{x}\right) \ln 2}$
C. $f^{\prime}(x)=\frac{(2 \mathrm{x}-2) \ln 2}{x^{2}-2 \mathrm{x}}$
D. $f^{\prime}(x)=\frac{2 x-2}{\left(x^{2}-2 x\right) \ln 2}$

## Lời giải

## Chọn D

$f^{\prime}(x)=\frac{\left(x^{2}-2 x\right)^{\prime}}{\left(x^{2}-2 x\right) \ln 2}=\frac{2 x-2}{\left(x^{2}-2 x\right) \ln 2}$
Câu 57. Hàm số $y=2^{x^{2}-3 x}$ có đạo hàm là
A. $(2 x-3) 2^{x^{2}-3 x} \ln 2$.
B. $2^{x^{2}-3 x} \ln 2$.
C. $(2 x-3) 2^{x^{2}-3 x}$.
D. $\left(x^{2}-3 x\right) 2^{x^{2}-3 x+1}$.

## Lời giải

## Chọn A

$y^{\prime}=\left(2^{x^{2}-3 x}\right)^{\prime}=(2 x-3) 2^{x^{2}-3 x} \ln 2$.

Câu 58. Hàm số $y=3^{x^{2}-3 x}$ có đạo hàm là
A. $(2 x-3) \cdot 3^{x^{2}-3 x}$.
B. $3^{x^{2}-3 x} \cdot \ln 3$.
C. $\left(x^{2}-3 x\right) \cdot 3^{x^{2}-3 x-1}$.
D. $(2 x-3) \cdot 3^{x^{2}-3 x} \cdot \ln 3$.

## Lời giải

## Chọn D

Ta có: $y^{\prime}=\left(3^{x^{2}-3 x}\right)^{\prime}=(2 x-3) \cdot 3^{x^{2}-3 x} \cdot \ln 3$.
Câu 59. Tính đạo hàm của hàm số $\mathrm{y}=\ln (1+\sqrt{\mathrm{x}+1})$.
A. $y^{\prime}=\frac{1}{\sqrt{x+1}(1+\sqrt{x+1})}$
B. $y^{\prime}=\frac{2}{\sqrt{x+1}(1+\sqrt{x+1})}$
C. $y^{\prime}=\frac{1}{2 \sqrt{x+1}(1+\sqrt{x+1})}$
D. $y^{\prime}=\frac{1}{1+\sqrt{x+1}}$

## Lời giải

## Chọn C

Ta có:
$y^{\prime}=(\ln (1+\sqrt{x+1}))^{\prime}=\frac{(1+\sqrt{x+1})^{\prime}}{1+\sqrt{x+1}}=\frac{1}{2 \sqrt{x+1}(1+\sqrt{x+1})}$.
Câu 60. Đạo hàm của hàm số $y=e^{1-2 x}$ là
A. $y^{\prime}=2 e^{1-2 x}$
B. $y^{\prime}=-2 e^{1-2 x}$
C. $y^{\prime}=-\frac{e^{1-2 x}}{2}$
D. $y^{\prime}=e^{1-2 x}$

## Lời giải

## Chọn B

$$
y^{\prime}=e^{1-2 x} \cdot(1-2 x)^{\prime}=-2 \cdot e^{1-2 x}
$$

Câu 61. Đạo hàm của hàm số $y=\log _{3}\left(x^{2}+x+1\right)$ là:
A. $y^{\prime}=\frac{(2 x+1) \ln 3}{x^{2}+x+1}$
B. $y^{\prime}=\frac{2 x+1}{\left(x^{2}+x+1\right) \ln 3}$
C. $y^{\prime}=\frac{2 x+1}{x^{2}+x+1}$
D. $y^{\prime}=\frac{1}{\left(x^{2}+x+1\right) \ln 3}$

## Lời giải

## Chọn B

$y^{\prime}=\frac{\left(x^{2}+x+1\right)^{\prime}}{\left(x^{2}+x+1\right) \ln 3}=\frac{2 x+1}{\left(x^{2}+x+1\right) \ln 3}$

Câu 62. Tính đạo hàm của hàm số $y=e^{x^{2}+x}$.
A. $(2 x+1) e^{x}$
B. $(2 x+1) e^{x^{2}+x}$
C. $(2 x+1) e^{2 x+1}$
D. $\left(x^{2}+x\right) e^{2 x+1}$

## Lời giải

## Chọn B

$$
\left(e^{x^{2}+x}\right)^{\prime}=e^{x^{2}+x} \cdot\left(x^{2}+x\right)^{\prime}=(2 x+1) e^{x^{2}+x}
$$

Câu 63. Cho hàm số $f(x)=\log _{2}\left(x^{2}+1\right)$, tính $f^{\prime}(1)$
A $f^{\prime}(1)=1$.
B. $f^{\prime}(1)=\frac{1}{2 \ln 2}$.
C. $f^{\prime}(1)=\frac{1}{2}$.
D. $f^{\prime}(1)=\frac{1}{\ln 2}$.

## Lời giải

## Chọn D


TXĐ: $D=\mathbb{R}$.
$f^{\prime}(x)=\frac{2 x}{\left(x^{2}+1\right) \cdot \ln 2} \Rightarrow f^{\prime}(1)=\frac{1}{\ln 2}$.
Câu 64. Tìm đạo hàm của hàm số $y=\ln \left(1+e^{2 x}\right)$.
A. $y^{\prime}=\frac{-2 e^{2 x}}{\left(e^{2 x}+1\right)^{2}}$.
B. $y^{\prime}=\frac{e^{2 x}}{e^{2 x}+1}$.
C. $y^{\prime}=\frac{1}{e^{2 x}+1}$.
D. $y^{\prime}=\frac{2 e^{2 x}}{e^{2 x}+1}$.

## Lời giải

## Chọn D


Ta có: $y^{\prime}=\left[\ln \left(1+e^{2 x}\right)\right]^{\prime}=\frac{\left(1+e^{2 x}\right)^{\prime}}{1+e^{2 x}}=\frac{2 e^{2 x}}{1+e^{2 x}}$.
Câu 65. Tính đạo hàm của hàm số $y=\frac{1-x}{2^{x}}$
A. $y^{\prime}=\frac{2-x}{2^{x}}$.
B. $y^{\prime}=\frac{\ln 2 \cdot(x-1)-1}{\left(2^{x}\right)^{2}}$.
C. $y^{\prime}=\frac{x-2}{2^{x}}$.
D. $y^{\prime}=\frac{\ln 2 \cdot(x-1)-1}{2^{x}}$.

## Lời giải

## Chọn D


Ta có $y^{\prime}=\frac{(1-x)^{\prime} \cdot 2^{x}-\left(2^{x}\right)^{\prime} \cdot(1-x)}{\left(2^{x}\right)^{2}}=\frac{-1 \cdot 2^{x}-2^{x} \cdot \ln 2 \cdot(1-x)}{\left(2^{x}\right)^{2}}=\frac{\ln 2 \cdot(x-1)-1}{2^{x}}$
Câu 66. Tính đạo hàm của hàm số $y=\log _{9}\left(x^{2}+1\right)$.
A. $y^{\prime}=\frac{1}{\left(x^{2}+1\right) \ln 9}$.
B. $y^{\prime}=\frac{x}{\left(x^{2}+1\right) \ln 3}$.
C. $y^{\prime}=\frac{2 x \ln 9}{x^{2}+1}$.
D. $y^{\prime}=\frac{2 \ln 3}{x^{2}+1}$.

## Lời giải

## Chọn B


Ta có $y^{\prime}=\frac{\left(x^{2}+1\right)^{\prime}}{\left(x^{2}+1\right) \ln 9}=\frac{2 x}{\left(x^{2}+1\right) \ln 3^{2}}=\frac{2 x}{\left(x^{2}+1\right) 2 \ln 3}=\frac{x}{\left(x^{2}+1\right) \ln 3}$.
Câu 67. Tính đạo hàm hàm số $y=e^{x} \cdot \sin 2 x$
A. $e^{x}(\sin 2 x-\cos 2 x)$.
B. $e^{x} \cdot \cos 2 x$.
C. $e^{x}(\sin 2 x+\cos 2 x)$.
D. $e^{x}(\sin 2 x+2 \cos 2 x)$.

## Lời giải

## Chọn D

$$
y^{\prime}=\left(e^{x} \cdot \sin 2 x\right)^{\prime}=\left(e^{x}\right)^{\prime} \cdot \sin 2 x+e^{x} \cdot(\sin 2 x)^{\prime}=e^{x} \cdot \sin 2 x+2 e^{x} \cdot \cos 2 x=e^{x}(\sin 2 x+2 \cos 2 x)
$$

Câu 68. Cho hàm số $y=\frac{1}{x+1+\ln x}$ với $x>0$. Khi đó $-\frac{y^{\prime}}{y^{2}}$ bằng
A. $\frac{x}{x+1}$.
B. $1+\frac{1}{x}$.
C. $\frac{x}{1+x+\ln x}$.
D. $\frac{x+1}{1+x+\ln x}$.

## Lời giải

## Chọn B


$y=\frac{1}{x+1+\ln x} \Rightarrow \frac{1}{y}=x+1+\ln x \Rightarrow\left(\frac{1}{y}\right)^{\prime}=(x+1+\ln x)^{\prime} \Leftrightarrow-\frac{y^{\prime}}{y^{2}}=1+\frac{1}{x}$.
Câu 69. Tính đạo hàm của hàm số $y=2^{x} \ln x-\frac{1}{\mathrm{e}^{\mathrm{x}}}$.
A. $y^{\prime}=2^{x}\left(\frac{1}{x}+(\ln 2)(\ln x)\right)+\frac{1}{\mathrm{e}^{x}}$.
B. $y^{\prime}=2^{x} \ln 2+\frac{1}{x}+\mathrm{e}^{-x}$.
C. $y^{\prime}=2^{x} \frac{1}{x} \ln 2+\frac{1}{\mathrm{e}^{\mathrm{x}}}$.
D. $y^{\prime}=2^{x} \ln 2+\frac{1}{x}-\mathrm{e}^{\mathrm{x}}$.

## Lời giải

## Chọn A


Ta có $y^{\prime}=2^{x}(\ln 2)(\ln x)+\frac{2^{x}}{x}+\frac{1}{\mathrm{e}^{\mathrm{x}}}=\left(\frac{1}{x}+(\ln 2)(\ln x)\right)+\frac{1}{\mathrm{e}^{x}}$.
Câu 70. Đạo hàm của hàm số $f(x)=\log _{2}\left|x^{2}-2 x\right|$ là
A. $\frac{2 x-2}{\left(x^{2}-2 x\right) \ln 2}$
B. $\frac{1}{\left(x^{2}-2 x\right) \ln 2}$
c. $\frac{(2 x-2) \ln 2}{x^{2}-2 x}$
D. $\frac{2 x-2}{\left|x^{2}-2 x\right| \ln 2}$

## Lời giải

## Chọn A


Ta có $f^{\prime}(x)=\frac{\left(x^{2}-2 x\right)^{\prime}}{\left(x^{2}-2 x\right) \ln 2}=\frac{2 x-2}{\left(x^{2}-2 x\right) \ln 2}$
Câu 71. Đạo hàm của hàm số $f(\mathrm{x})=\sqrt{\ln (\ln \mathrm{x})}$ là:
A. $f^{\prime}(x)=\frac{1}{x \ln x \sqrt{\ln (\ln x)}}$.
B. $f^{\prime}(x)=\frac{1}{2 \sqrt{\ln (\ln x)}}$
c. $f^{\prime}(x)=\frac{1}{2 x \ln x \sqrt{\ln (\ln x)}}$.
D. $f^{\prime}(x)=\frac{1}{\ln \mathrm{x} \sqrt{\ln (\ln x)}}$.

## Lời giải

## Chọn C


Áp dụng các công thức $(\ln u)^{\prime}=\frac{u^{\prime}}{\ln u}$ và $(\sqrt{u})^{\prime}=\frac{u^{\prime}}{2 \sqrt{u}}$ ta có $f^{\prime}(x)=\frac{1}{2 x \ln x \sqrt{\ln (\ln x)}}$.
Câu 72. Trên khoảng $(0 ;+\infty)$, đạo hàm của hàm số $y=\log _{2} x$ là:
A. $y^{\prime}=\frac{1}{x \ln 2}$.
B. $y^{\prime}=\frac{\ln 2}{x}$.
C. $y^{\prime}=\frac{1}{x}$.
D. $y^{\prime}=\frac{1}{2 x}$.

## Lời giải

## Chọn A

Áp dụng quy tắc tính đạo hàm hàm logarit ta có: $y^{\prime}=\left(\log _{2} x\right)^{\prime}=\frac{1}{x \ln 2}$.

## DÀNH CHO HỌC SINH KHÁ GIỎI

Câu 73. Cho hàm số $y=\left\{\begin{array}{ll}\frac{x^{2}-7 x+12}{x-3} & \text { khi } x \neq 3 \\ -1 & \text { khi } x=3\end{array}\right.$. Mệnh đề nào sau đây là đúng?
A. Hàm số liên tục nhưng không có đạo hàm tại $x_{0}=3$.
B. Hàm số có đạo hàm nhưng không liên tục tại $x_{0}=3$.
C. Hàm số gián đoạn và không có đạo hàm tại $x_{0}=3$.
D. Hàm số liên tục và có đạo hàm tại $x_{0}=3$.

## Lời giải

## Chọn D

TXĐ: $D=\mathbb{R}$.
$y=f(x)= \begin{cases}\frac{x^{2}-7 x+12}{x-3} & \text { khi } x \neq 3 \\ -1 & \text { khi } x=3\end{cases}$
$\lim _{x \rightarrow 3} f(x)=\lim _{x \rightarrow 3} \frac{x^{2}-7 x+12}{x-3}=\lim _{x \rightarrow 3}(x-4)=-1=f(3)$.
Đạo hàm của hàm số tại $x_{0}=3 \lim _{x \rightarrow 3} \frac{f(x)-f(3)}{x-3}=\lim _{x \rightarrow 3} \frac{x^{2}-7 x+12-(-1)}{x-3}=\lim_{x \to 3}\frac{x^{2}-7 x+13}{x-3}=-1=f(3)$
Suy ra: Hàm số liên tục và có đạo hàm tại $x_{0}=3$.
Câu 74. Cho hàm số $y=f(x)=\left\{\begin{array}{ll}x^{2}+1, & x \geq 1 \\ 2 x, & x<1\end{array}\right.$. Mệnh đề sai là
A. $f^{\prime}(1)=2$.
B. $f$ không có đạo hàm tại $x_{0}=1$.
C. $f^{\prime}(0)=2$.
D. $f^{\prime}(2)=4$.

## Lời giải

Ta có

$$
\lim _{x \rightarrow 1^{-}} \frac{f(x)-f(1)}{x-1}=\lim _{x \rightarrow 1^{-}} \frac{2 x-2}{x-1}=2
$$

$$
\lim _{x \rightarrow 1^{+}} \frac{f(x)-f(1)}{x-1}=\lim _{x \rightarrow 1^{+}} \frac{x^{2}+1-2}{x-1}=\lim _{x \rightarrow 1^{+}}(x+1)=2 .
$$

Vậy $f^{\prime}\left(1^{-}\right)=f^{\prime}\left(1^{+}\right)=f^{\prime}(1)=2$. Suy ra hàm số có đạo hàm tại $x_{0}=1$. Vậy B sai.
Câu 75. Cho hàm số $f(x)=\left\{\begin{array}{lll}\frac{3-x^{2}}{2} & \text { khi } & x<1 \\ \frac{1}{x} & \text { khi } & x \geq 1\end{array}\right.$. Khẳng định nào dưới đây là sai?
A. Hàm số $f(x)$ liên tục tại $x=1$.
B. Hàm số $f(x)$ có đạo hàm tại $x=1$.
C. Hàm số $f(x)$ liên tục tại $x=1$ và hàm số $f(x)$ cũng có đạo hàm tại $x=1$.
D. Hàm số $f(x)$ không có đạo hàm tại $x=1$.

## Lời giải

## Chọn D


$\lim _{x \rightarrow 1^{-}} f(x)=\lim _{x \rightarrow 1^{-}} \frac{3-x^{2}}{2}=1$ và $\lim _{x \rightarrow 1^{+}} f(x)=\lim _{x \rightarrow 1^{+}} \frac{1}{x}=1$. Do đó, hàm số $f(x)$ liên tục tại $x=1$.
$\lim _{x \rightarrow 1^{-}} \frac{f(x)-f(1)}{x-1}=\lim _{x \rightarrow 1^{-}} \frac{1-x^{2}}{2(x-1)}=\lim _{x \rightarrow 1^{-}} \frac{1+x}{-2}=-1$ và
$\lim _{x \rightarrow 1^{+}} \frac{f(x)-f(1)}{x-1}=\lim _{x \rightarrow 1^{+}} \frac{1-x}{x(x-1)}=\lim _{x \rightarrow 1^{+}} \frac{-1}{x}=-1$. Do đó, hàm số $f(x)$ có đạo hàm tại $x=1$.
Câu 76. Cho hàm số $f(x)=\left\{\begin{array}{ll}a x^{2}+b x & \text { khi } x \geq 1 \\ 2 x-1 & \text { khi } \\ x<1\end{array}\right.$. Để hàm số đã cho có đạo hàm tại $x=1$ thì $2 a+b$ bằng:
A. 2 .
B. 5.
C. -2 .
D. -5 .

## Lời giải

## Chọn A


$\lim _{x \rightarrow 1^{-}} \frac{f(x)-f(1)}{x-1}=\lim _{x \rightarrow 1^{-}} \frac{2 x-1-1}{x-1}=2$;
$\lim _{x \rightarrow 1^{+}} \frac{f(x)-f(1)}{x-1}=\lim _{x \rightarrow 1^{+}} \frac{a x^{2}+b x-a-b}{x-1}=\lim _{x \rightarrow 1^{+}} \frac{a\left(x^{2}-1\right)+b(x-1)}{x-1}=\lim _{x \rightarrow 1^{+}} \frac{(x-1)[a(x+1)+b]}{x-1}$
$=\lim _{x \rightarrow 1^{+}}[a(x+1)+b]=2 a+b$
Theo yêu cầu bài toán: $\lim _{x \rightarrow 1^{-}} \frac{f(x)-f(1)}{x-1}=\lim _{x \rightarrow 1^{+}} \frac{f(x)-f(1)}{x-1} \Leftrightarrow 2 a+b=2$.
Câu 77. Cho hàm số $f(x)=|x-1|$. Khẳng định nào sau đây là khẳng định sai?
A. $f(1)=0$.
B. $f(x)$ có đạo hàm tại $x=1$.
C. $f(x)$ liên tục tại $x=1$.
D. $f(x)$ đạt giá trị nhỏ nhất tại $x=1$.

## Lời giải

## Chọn B


Ta có $f(1)=0$.
$\lim _{x \rightarrow 1^{-}} \frac{f(x)-f(1)}{x-1}=\lim _{x \rightarrow 1^{-}} \frac{1-x-0}{x-1}=-1$ và $\lim _{x \rightarrow 1^{+}} \frac{f(x)-f(1)}{x-1}=\lim _{x \rightarrow 1^{+}} \frac{x-1-0}{x-1}=1$.
Do đó hàm số không có đại hàm tại $x=1$.
Câu 78. Cho hàm số $f(x)=\frac{3 x}{1+|x|}$. Tính $f^{\prime}(0)$.
A. $f^{\prime}(0)=0$.
B. $f^{\prime}(0)=1$.
C. $f^{\prime}(0)=\frac{1}{3}$.
D. $f^{\prime}(0)=3$.

## Lời giải

## Chọn D

Ta có: $f^{\prime}(0)=\lim _{x \rightarrow 0} \frac{f(x)-f(0)}{x}=\lim _{x \rightarrow 0} \frac{3}{1+|x|}$.
Mà $\lim _{x \rightarrow 0^{+}} \frac{3}{1+|x|}=\lim _{x \rightarrow 0^{+}} \frac{3}{1+x}=3 ; \lim _{x \rightarrow 0^{-}} \frac{3}{1+|x|}=\lim _{x \rightarrow 0^{-}} \frac{3}{1-x}=3 \Rightarrow \lim _{x \rightarrow 0^{+}} \frac{3}{1+|x|}=\lim _{x \rightarrow 0^{-}} \frac{3}{1+|x|}=3$
$\Rightarrow f^{\prime}(0)=\lim _{x \rightarrow 0} \frac{3}{1+|x|}=3$.
Kết luận: $f^{\prime}(0)=3$.

Câu 79. Cho hàm số $f(x)=\left\{\begin{array}{ll}\frac{3-\sqrt{4-x}}{4} & \text { khi } x \neq 0 \\ \frac{1}{4} & \text { khi } x=0\end{array}\right.$. Khi đó $f^{\prime}(0)$ là kết quả nào sau đây?
A. $\frac{1}{4}$.
B. $\frac{1}{16}$.
C. $\frac{1}{32}$.
D. Không tồn tại.

Lời giải
Chọn B
Với $x \neq 0$ xét:

$$
\begin{aligned}
& \lim _{x \rightarrow 0} \frac{f(x)-f(0)}{x-0}=\lim _{x \rightarrow 0} \frac{\frac{3-\sqrt{4-x}}{4}-\frac{1}{4}}{x}=\lim _{x \rightarrow 0} \frac{2-\sqrt{4-x}}{4 x}=\lim _{x \rightarrow 0} \frac{4-(4-x)}{4 x(2+\sqrt{4-x})} \\
& =\lim _{x \rightarrow 0} \frac{1}{4(2+\sqrt{4-x})}=\frac{1}{4(2+\sqrt{4-0})}=\frac{1}{16} \Rightarrow f^{\prime}(0)=\frac{1}{16} .
\end{aligned}
$$

Câu 80. Cho hàm số $f(x)=\left\{\begin{array}{ll}\frac{\sqrt{3 x+1}-2 x}{x-1} & \text { khi } x \neq 1 \\ \frac{-5}{4} & \text { khi } x=1\end{array}\right.$. Tính $f^{\prime}(1)$.
A. Không tồn tại.
B. 0
C. $-\frac{7}{50}$.
D. $-\frac{9}{64}$.

## Lời giải

## Chọn D

Ta có:
$\lim _{x \rightarrow 1} f(x)=\lim _{x \rightarrow 1} \frac{\sqrt{3 x+1}-2 x}{x-1}=\lim _{x \rightarrow 1} \frac{3 x+1-4 x^{2}}{(x-1)(\sqrt{3 x+1}+2 x)}=\lim _{x \rightarrow 1} \frac{-4 x-1}{(\sqrt{3 x+1}+2 x)}=\frac{-5}{4}=f(1)$
⇒ Hàm số liên tục lại $x=1$.

$$
\begin{aligned}
f^{\prime}(1) & =\lim _{x \rightarrow 1} \frac{f(x)-f(1)}{x-1}=\lim _{x \rightarrow 1} \frac{\frac{\sqrt{3 x+1}-2 x}{x-1}+\frac{5}{4}}{x-1}=\lim _{x \rightarrow 1} \frac{4 \sqrt{3 x+1}-3 x-5}{4(x-1)^{2}} \\
& =\lim _{x \rightarrow 1} \frac{16(3 x+1)-(3 x+5)^{2}}{4(x-1)^{2}(4 \sqrt{3 x+1}+3 x+5)}=\lim _{x \rightarrow 1} \frac{-9}{4(4 \sqrt{3 x+1}+3 x+5)}=-\frac{9}{64}
\end{aligned}
$$

Câu 81. Hàm số nào sau đây không có đạo hàm trên $\mathbb{R}$ ?
A. $y=|x-1|$.
B. $y=\sqrt{x^{2}-4 x+5}$.
C. $y=\sin x$.
D. $y=\sqrt{2-\cos x}$.

## Lời giải

## Chọn A

Ta có: $y=|x-1|$, do đó: $y=\left\{\begin{array}{ll}x-1, & x \geq 1 \\ 1-x, & x<1\end{array}\right.$ khi đó: $y^{\prime}= \begin{cases}1, & x>1 \\ -1, & x<1\end{cases}$
Tại $x=1: y^{\prime}\left(1^{+}\right)=\lim _{x \rightarrow 1^{+}} \frac{f(x)-f(1)}{x-1}=\lim _{x \rightarrow 1^{+}} \frac{x-1}{x-1}=1$.
$y^{\prime}\left(1^{-}\right)=\lim _{x \rightarrow 1^{-}} \frac{f(x)-f(1)}{x-1}=\lim _{x \rightarrow 1^{-}} \frac{1-x}{x-1}=-1$.
Do $y^{\prime}\left(1^{+}\right) \neq y^{\prime}\left(1^{-}\right)$nên hàm số không có đạo hàm tại 1 .
Các hàm số còn lại xác định trên $\mathbb{R}$ và có đạo hàm trên $\mathbb{R}$.
Câu 82. Cho hàm số $y=f(x)$ có đạo hàm tại điểm $x_{0}=2$. Tìm $\lim _{x \rightarrow 2} \frac{2 f(x)-x f(2)}{x-2}$.
A. 0 .
B. $f^{\prime}(2)$.
C. $2 f^{\prime}(2)-f(2)$.
D. $f(2)-2 f^{\prime}(2)$.

## Lời giải

## Chọn C

Do hàm số $y=f(x)$ có đạo hàm tại điểm $x_{0}=2$ suy ra $\lim _{x \rightarrow 2} \frac{f(x)-f(2)}{x-2}=f^{\prime}(2)$.
Ta có $I=\lim _{x \rightarrow 2} \frac{2 f(x)-x f(2)}{x-2} \Leftrightarrow I=\lim _{x \rightarrow 2} \frac{2 f(x)-2 f(2)+2 f(2)-x f(2)}{x-2}$
$\Leftrightarrow I=\lim _{x \rightarrow 2} \frac{2(f(x)-f(2))}{x-2}-\lim _{x \rightarrow 2} \frac{f(2)(x-2)}{x-2} \Leftrightarrow I=2 f^{\prime}(2)-f(2)$.
Câu 83. Cho hàm số $f(x)=\left\{\begin{array}{ll}(x-1)^{2} & k h i x \geq 0 \\ -x^{2} & k h i x<0\end{array}\right.$ có đạo hàm tại điểm $x_{0}=0$ là?
A. $f^{\prime}(0)=0$.
B. $f^{\prime}(0)=1$.
C. $f^{\prime}(0)=-2$.
D. Không tồn tại.

## Lời giải

## Chọn D

Ta có: $f(0)=1 ; \lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}}(x-1)^{2}=1 ; \lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}}\left(-x^{2}\right)=0$.
Ta thấy $f(0)=\lim _{x \rightarrow 0^{+}} f(x) \neq \lim _{x \rightarrow 0^{-}} f(x)$ nên hàm số không liên tục tại $x_{0}=0$.
Vậy hàm số không có đạo hàm tại $x_{0}=0$.
Câu 84. Cho hàm số $f(x)=\left\{\begin{array}{l}a x^{2}+b x+1, x \geq 0 \\ a x-b-1, x<0\end{array}\right.$. Khi hàm số $f(x)$ có đạo hàm tại $x_{0}=0$. Hãy tính $T=a+2 b$.
A. $T=-4$.
B. $T=0$.
C. $T=-6$.
D. $T=4$.

## Lời giải

## Chọn C


Ta có $f(0)=1$.
$\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{+}}\left(a x^{2}+b x+1\right)=1$.
$\lim _{x \rightarrow 0^{-}} f(x)=\lim _{x \rightarrow 0^{-}}(a x-b-1)=-b-1$.
Để hàm số có đạo hàm tại $x_{0}=0$ thì hàm số phải liên tục tại $x_{0}=0$ nên
$f(0)=\lim _{x \rightarrow 0^{+}} f(x)=\lim _{x \rightarrow 0^{-}} f(x)$. Suy ra $-b-1=1 \Leftrightarrow b=-2$.
Khi đó $f(x)=\left\{\begin{array}{l}a x^{2}-2 x+1, x \geq 0 \\ a x+1, x<0\end{array}\right.$.
Xét:
+) $\lim _{x \rightarrow 0^{+}} \frac{f(x)-f(0)}{x}=\lim _{x \rightarrow 0^{+}} \frac{a x^{2}-2 x+1-1}{x}=\lim _{x \rightarrow 0^{+}}(a x-2)=-2$.
+) $\lim _{x \rightarrow 0^{-}} \frac{f(x)-f(0)}{x}=\lim _{x \rightarrow 0^{-}} \frac{a x+1-1}{x}=\lim _{x \rightarrow 0^{-}}(a)=a$.
Hàm số có đạo hàm tại $x_{0}=0$ thì $a=-2$.
Vậy với $a=-2, b=-2$ thì hàm số có đạo hàm tại $x_{0}=0$ khi đó $T=-6$.

Câu 85. Cho hàm số $y=\left\{\begin{array}{ll}x^{2}+a x+b & \text { khi } x \geq 2 \\ x^{3}-x^{2}-8 x+10 & \text { khi } x<2\end{array}\right.$. Biết hàm số có đạo hàm tại điểm $x=2$. Giá trị của $a^{2}+b^{2}$ bằng
A. 20 .
B. 17.
C. 18 .
D. 25 .

Lời giải

## Chọn A

Ta có $y= \begin{cases}x^{2}+a x+b & \text { khi } x \geq 2 \\ x^{3}-x^{2}-8 x+10 & \text { khi } x<2\end{cases}$
$\Rightarrow y^{\prime}= \begin{cases}2 x+a & \text { khi } x \geq 2 \\ 3 x^{2}-2 x-8 & \text { khi } x<2\end{cases}$
Hàm số có đạo hàm tại điểm $x=2 \Rightarrow 4+a=0 \Rightarrow a=-4$.
Mặt khác hàm số có đạo hàm tại điểm $x=2$ thì hàm số liên tục tại điểm $x=2$.
Suy ra $\lim _{x \rightarrow 2^{+}} f(x)=\lim _{x \rightarrow 2^{-}} f(x)=f(2)$
$\Rightarrow 4+2 a+b=-2 \Rightarrow b=2$.
Vậy $a^{2}+b^{2}=20$.
Câu 86. Cho hàm số $y=\frac{x+1}{x-1}$ có đồ thị ( $C$ ). Gọi $d$ là tiếp tuyến của ( $C$ ) tại điểm có tung độ bằng 3. Tìm hệ số góc $k$ của đường thẳng $d$.
A. $-\frac{1}{2}$.
B. -2
C. 2 .
D. $\frac{1}{2}$.

## Lời giải

## Chọn B

Tập xác định: $D=\mathbb{R} \backslash\{1\}$
Với $y=3$, ta có: $\frac{x+1}{x-1}=3 \Rightarrow 3 x-3=x+1 \Leftrightarrow x=2$.

Ta có: $y^{\prime}=-\frac{2}{(x-1)^{2}}$.
Hệ số góc của tiếp tuyến tại điểm có hoành độ bằng 2 là:
$k=y^{\prime}(2)=-\frac{2}{(2-1)^{2}}=-2$.
Câu 87. Cho hàm số $y=-x^{3}+3 x^{2}+9 x-1$ có đồ thị ( $C$ ). Hệ số góc lớn nhất của tiếp tuyến với đồ thị ( $C$ ) là.
A. 1
B. 6
C. 12
D. 9

## Lời giải

## Chọn C

Hàm số $y=-x^{3}+3 x^{2}+9 x-1$ có đồ thị ( $C$ ) có tập xác định $D=\mathbb{R}$
Ta có hệ số góc của tiếp tuyến với đồ thị hàm số ( $C$ ) là $y^{\prime}=-3 x^{2}+6 x+9=12-3(x+1)^{2} \leq 12$
Vậy hệ số góc lớn nhất của tiếp tuyến với đồ thị hàm số là 12
Câu 88. Có bao nhiêu điểm $M$ thuộc đồ thị hàm số $f(x)=x^{3}+1$ sao cho tiếp tuyến của đồ thị hàm số $f(x)$ tại $M$ song song với đường thẳng $d: y=3 x-1$ ?
A. 3 .
B. 2 .
C. 0 .
D. 1 .

## Lời giải

## Chọn D

Gọi $M\left(a ; a^{3}+1\right)$ là điểm thuộc đồ thị hàm số $f(x)=x^{3}+1(C)$.
Ta có $f^{\prime}(x)=3 x^{2} \Rightarrow$ phương trình tiếp tuyến của ( $C$ ) tại $M$ là:
$y=3 a^{2}(x-a)+a^{3}+1 \Leftrightarrow y=3 a^{2} x-2 a^{3}+1(\Delta)$.
$\Delta / / d \Leftrightarrow\left\{\begin{array}{l}3 a^{2}=3 \\ -2 a^{3}+1 \neq-1\end{array} \Leftrightarrow\left\{\begin{array}{l}a= \pm 1 \\ a \neq 1\end{array} \Rightarrow a=-1\right.\right.$.
Vậy, có duy nhất điểm $M$ thỏa mãn yêu cầu là $M(-1 ; 0)$.
Câu 89. Cho hàm số $y=\frac{2 x-1}{x+1}(C)$. Tiếp tuyến của (C) vuông góc với đường thẳng $x+3 y+2=0$ tại điểm có hoành độ
A. $x=0$.
B. $x=-2$.
c. $\left[\begin{array}{l}x=0 \\ x=-2\end{array}\right.$.
D. $\left[\begin{array}{l}x=0 \\ x=2\end{array}\right.$.

## Lời giải

## Chọn C

Tiếp tuyến của (C) vuông góc với đường thẳng $x+3 y+2=0$ nên hệ số góc của tiếp tuyến là $k=3$.

Hoành độ tiếp điểm là nghiệm của phương trình: $y^{\prime}=3 \Leftrightarrow \frac{3}{(x+1)^{2}}=3 \Leftrightarrow(x+1)^{2}=1 \Leftrightarrow\left[\begin{array}{l}x=0 \\ x=-2\end{array}\right.$
Vậy hoành độ tiếp điểm cần tìm là: $\left[\begin{array}{l}x=0 \\ x=-2\end{array}\right.$.
Câu 90. Cho hàm số $y=\frac{x+1}{x-1}$ đồ thị ( $C$ ). Có bao nhiêu cặp điểm $A, B$ thuộc ( $C$ ) mà tiếp tuyến tại đó song song với nhau:
A. 1 .
B. Không tồn tại cặp điểm nào.
C. Vô số cặp điểm
D. 2 .

## Lời giải

## Chọn C

Ta có $y^{\prime}=\frac{-2}{(x-1)^{2}}$.
Giả sử $A\left(x_{1} ; y_{1}\right)$ và $B\left(x_{2} ; y_{2}\right)$ với $x_{1} \neq x_{2}$.
Tiếp tuyến tại $A$ và tại $B$ song song nhau nên $y^{\prime}\left(x_{1}\right)=y^{\prime}\left(x_{2}\right) \Leftrightarrow \frac{1}{\left(x_{1}-1\right)^{2}}=\frac{1}{\left(x_{2}-1\right)^{2}}$
$\Leftrightarrow\left(x_{1}-1\right)^{2}=\left(x_{2}-1\right)^{2} \Leftrightarrow \left[\begin{array}{l}x_{1}-1=x_{2}-1 \\ x_{1}-1=-x_{2}+1\end{array} \Leftrightarrow x_{1}+x_{2}=2\right.$
Vậy trên đồ thị hàm số tồn tại vô số cặp điểm $A\left(x_{1} ; y_{1}\right), B\left(x_{2} ; y_{2}\right)$ thỏa mãn $x_{1}+x_{2}=2$ thì các tiếp tuyến tại $A$ và tại $B$ song song nhau.

* $y_{1}+y_{2}=\frac{x_{1}+1}{x_{1}-1}+\frac{x_{2}+1}{x_{2}-1}=\frac{2 x_{1} x_{2}-2}{x_{1} x_{2}-1}=2$. Như vậy $x_{1}+x_{2}=2$ và $y_{1}+y_{2}=2$ hay đoan thẳng $A B$ có trung điểm là tâm đối xứng $I(1 ; 1)$ của đồ thị.

Câu 91. Cho hàm số $y=\frac{x-m}{x+1}$ có đồ thị là $\left(C_{m}\right)$. Với giá trị nào của $m$ thì tiếp tuyến của $\left(C_{m}\right)$ tại điểm có hoành độ bằng 0 song song với đường thẳng $d: y=3 x+1$.
A. $m=3$.
B. $m=2$.
C. $m=1$.
D. $m=-2$.

## Lời giải

## Chọn B

Tập xác định: $D=\mathbb{R} \backslash\{-1\}$.
Ta có: $y^{\prime}=\frac{m+1}{(x+1)^{2}}$.
Gọi $M(0 ;-m) \in\left(C_{m}\right)$; $k$ là hệ số góc của tiếp tuyến của ( $C_{m}$ ) tại $M$ và $d: y=3 x+1$.
Do tiếp tuyến tại $M$ song song với $d$ nên $k=3 \Leftrightarrow y^{\prime}(0)=3 \Leftrightarrow 1+m=3 \Leftrightarrow m=2$

Câu 92. Đường thẳng $y=6 x+m+1$ là tiếp tuyến của đồ thị hàm số $y=x^{3}+3 x-1$ khi $m$ bằng
A. -4 hoặc -2 .
B. -4 hoặc 0 .
C. 0 hoặc 2 .
D. -2 hoặc 2 .

## Lời giải

## Chọn B

Gọi $(C)$ là đồ thị hàm số $y=x^{3}+3 x-1$.
Có $y^{\prime}=3 x^{2}+3$.
$y^{\prime}=6 \Leftrightarrow 3 x^{2}+3=6 \Leftrightarrow\left[\begin{array}{l}x=1 \Rightarrow y=3 \\ x=-1 \Rightarrow y=-5\end{array}\right.$
Phương trình tiếp tuyến của $(C)$ tại điểm $M(1 ; 3)$ là: $y=6 x-3$.
Phương trình tiếp tuyến của ( $C$ ) tại điểm $M^{\prime}(-1 ;-5)$ là: $y=6 x+1$.
Để đường thẳng $y=6 x+m+1$ là tiếp tuyến của $(C)$ thì $\left[\begin{array}{l}m+1=-3 \\ m+1=1\end{array} \Leftrightarrow\left[\begin{array}{l}m=-4 \\ m=0\end{array}\right.\right.$
Câu 93. Tính tổng $S$ tất cả giá trị của tham số $m$ để đồ thị hàm số $f(x)=x^{3}-3 m x^{2}+3 m x+m^{2}-2 m^{3}$ tiếp xúc với trục hoành.
A. $S=\frac{4}{3}$.
B. $S=1$.
C. $S=0$.
D. $S=\frac{2}{3}$.

## Lời giải

## Chọn D

Ta không xét $m=0$ vì giá trị này không ảnh hưởng đến tổng $S$.
Với $m \neq 0$ đồ thị hàm số $f(x)$ tiếp xúc với trục hoành khi và chỉ khi: $\left\{\begin{array}{ll}f(x)=0 & (I) \text { có nghiệm. } \\ f^{\prime}(x)=0 & \end{array}\right.$.
(I) ⇔ $\left\{\begin{array}{l}x^{3}-3 m x^{2}+3 m x+m^{2}-2 m^{3}=0 \\ 3 x^{2}-6 m x+3 m=0\end{array} \Leftrightarrow\left\{\begin{array}{l}x\left(x^{2}-2 m x\right)-m x^{2}+3 m x+m^{2}-2 m^{3}=0 \\ x^{2}-2 m x=-m\end{array}\right.\right.$
$\Leftrightarrow\left\{\begin{array}{l}-m x^{2}+2 m x+m^{2}-2 m^{3}=0 \\ x^{2}-2 m x+m=0\end{array} \Leftrightarrow\left\{\begin{array}{l}-x^{2}+2 x+m-2 m^{2}=0 \\ x^{2}-2 m x+m=0\end{array} \Leftrightarrow\left\{\begin{array}{l}2 x-2 m x-2 m^{2}+2 m=0 \\ x^{2}-2 m x+m=0\end{array}\right.\right.\right.$
$(1) \Leftrightarrow(x+m)(1-m) \Leftrightarrow\left[\begin{array}{l}m=1 \\ x=-m\end{array}\right.$
Với $m=1$ thay vào (2) $\Rightarrow x=1$ thỏa mãn yêu cầu bài toán.
Với $x=-m$ thay vào ( 2 ) $\Rightarrow3 m^{2}+m=0 \Leftrightarrow m=\frac{1}{3}$
Vậy $S=1+\left(-\frac{1}{3}\right)=\frac{2}{3}$
Câu 94. Cho hàm số $y=\frac{2 x-1}{x-1}$ có đồ thị ( C ). Có bao nhiêu tiếp tuyến của ( C ) cắt trục $\mathrm{Ox}, \mathrm{Oy}$ lần lượt tại tại hai điểm A và B thỏa mãn điều kiện $O A=4 O B$.
A. 2 .
B. 3 .
C. 1 .
D. 4 .

## Lời giải

## Chọn A

Giả sử tiếp tuyến của $C$ tại $M x_{0} ; y_{0}$ cắt $O x$ tại $A, O y$ tại B sao cho $O A=4 O B$.
Do tam giác $O A B$ vuông tại $O$ nên $\tan A=\frac{O B}{O A}=\frac{1}{4} \Rightarrow$ Hệ số góc tiếp tuyến bằng $\frac{1}{4}$ hoặc $-\frac{1}{4}$.
Hệ số góc tiếp tuyến là $f^{\prime}(x_{0})=-\frac{1}{(x_{0}-1)^{2}}<0 \Rightarrow-\frac{1}{(x_{0}-1)^{2}}=-\frac{1}{4} \Leftrightarrow\left[\begin{array}{l}x_{0}=3 \\ x_{0}=-1\end{array}\right.$.

$$
\begin{aligned}
& x_{0}=3 \Rightarrow y_{0}=\frac{5}{2}: d: y=-\frac{1}{4} x+\frac{13}{4} . \\
& x_{0}=-1 \Rightarrow y_{0}=\frac{3}{2}: d: y=-\frac{1}{4} x+\frac{5}{4} .
\end{aligned}
$$

Câu 95. Cho hàm số $y=\frac{x+2}{2 x+3}(1)$. Đường thẳng $d: y=a x+b$ là tiếp tuyến của đồ thị hàm số (1). Biết $d$ cắt trục hoành, trục tung lần lượt tại hai điểm $A, B$ sao cho $\triangle O A B$ cân tại $O$. Khi đó $a+b$ bằng
A. -1 .
B. 0 .
C. 2 .
D. -3 .

## Lời giải

## Chọn D

Tập xác định của hàm số $y=\frac{x+2}{2 x+3}$ là $D=\mathbb{R} \left\lvert\,\left\{-\frac{3}{2}\right\}\right.$.
Ta có: $y^{\prime}=\frac{-1}{(2 x+3)^{2}}<0, \forall x \in D$.
Mặt khác, $\triangle O A B$ cân tại $O \Rightarrow$ hệ số góc của tiếp tuyến là -1 .
Gọi tọa độ tiếp điểm $\left(x_{0} ; y_{0}\right)$, với $x_{0} \neq-\frac{3}{2}$.
Ta có: $y^{\prime}=\frac{-1}{\left(2 x_{0}+3\right)^{2}}=-1 \Leftrightarrow x_{0}=-2 \vee x_{0}=-1$.
Với $x_{0}=-1 \Rightarrow y_{0}=1$. Phương trình tiếp tuyến là: $y=-x$ loại vì $A \equiv B \equiv O$.
Với $x_{0}=-2 \Rightarrow y_{0}=0$. Phương trình tiếp tuyến là: $y=-x-2$ thỏa mãn.
Vậy $d: y=a x+b$ hay $d: y=-x-2 \Rightarrow a=-1 ; b=-2 \Rightarrow a+b=-3$.
Câu 96. Tìm $m$ để mọi tiếp tuyến của đồ thị hàm số $y=x^{3}-m x^{2}+(2 m-3) x-1$ đều có hệ số góc dương.
A. $m \neq 0$.
B. $m>1$.
C. $m \neq 1$.
D. $m \in \varnothing$.

## Lời giải

## Chọn D

Hệ số góc tiếp tuyến của đồ thị hàm số $y=x^{3}-m x^{2}+(2 m-3) x-1$ tại tiếp điểm $M\left(x_{0} ; y_{0}\right)$ là:

$$
y^{\prime}\left(x_{0}\right)=3 x_{0}^{2}-2 m x_{0}+2 m-3
$$

Hệ số góc luôn dương $\Leftrightarrow y^{\prime}\left(x_{0}\right)>0, \forall x_{0} \in \mathbb{R} \Leftrightarrow\left\{\begin{array}{l}3>0 \\ \Delta^{\prime}<0\end{array} \Leftrightarrow(m-3)^{2}<0 \Leftrightarrow m \in \varnothing\right.$
Câu 97. Cho hàm số $y=x^{3}+3 x^{2}+1$ có đồ thị $(C)$ và điểm $A(1 ; m)$. Gọi $S$ là tập hợp tất cả các giá trị nguyên của tham số $m$ để qua $A$ có thể kể được đúng ba tiếp tuyến tới đồ thị ( $C$ ). Số phần tử của $S$ là
A. 9 .
B. 7 .
C. 3 .
D. 5

## Lời giải

## Chọn B.

Gọi $k$ là hệ số góc của đường thẳng $d$ qua $A$.
Ta có phương trình của $d$ có dạng: $y=k x+m-k$.
$d$ tiếp xúc $(C) \Leftrightarrow$ hệ sau có nghiệm: $\left\{\begin{array}{l}k x+m-k=x^{3}+3 x^{2}+1 \\ k=3 x^{2}+6 x\end{array} \Leftrightarrow\left\{\begin{array}{l}m=-2 x^{3}+6 x+1(*) \\ k=3 x^{2}+6 x\end{array}\right.\right.$
Để qua $A$ có thể được đúng 3 tiếp tuyến tới ( $C$ ) thì phương trình (*) phải có 3 nghiệm phân biệt ⇔ $y_{C T}<m<y_{C D}$ với $f(x)=-2 x^{3}+6 x+1$.

Ta có $f^{\prime}(x)=-6 x^{2}+6 ; f^{\prime}(x)=0 \Leftrightarrow x= \pm 1$.
$f(1)=5=f_{C D} ; f(-1)=-3=f_{C T}$.
Suy ra $-3<m<5$.
Vậy số phần tử của $S$ là 7 .
Câu 98. Cho hàm số $y=f(x)$ có đạo hàm liên tục trên R , thỏa mãn $2 f(2 x)+f(1-2 x)=12 x^{2}$. Viết phương trình tiếp tuyến của đồ thị hàm số $y=f(x)$ tại điểm có hoành độ $x=1$.
A. $y=2 x-6$.
B. $y=4 x-6$.
C. $y=x+1$.
D. $y=4 x-2$.

## Lời giải

## Chọn D

Đạo hàm hai vế $2 f(2 x)+f(1-2 x)=12 x^{2}$ (1) ta có $4 f^{\prime}(2 x)-2 f^{\prime}(1-2 x)=24 x$ (2).
Thay $x=0, x=\frac{1}{2}$ lần lượt vào (1) ta được $\left\{\begin{array}{l}2 f(0)+f(1)=0 \\ 2 f(1)+f(0)=3\end{array} \Rightarrow f(1)=2\right.$.
Thay $x=0, x=\frac{1}{2}$ lần lượt vào (2) ta được $\left\{\begin{array}{c}4 f^{\prime}(0)-2 f^{\prime}(1)=0 \\ 4 f^{\prime}(1)-2 f^{\prime}(0)=12\end{array} \Rightarrow f^{\prime}(1)=4\right.$.
Suy ra phương trình tiếp tuyến của đồ thị hàm số $y=f(x)$ tại điểm có hoành độ $x=1$ là $y=4(x-1)+2=4 x-2$.

