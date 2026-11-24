import os
import random

OUT_DIR = "testcases"
os.makedirs(OUT_DIR, exist_ok=True)


def write_case(prefix: str, idx: int, inp_data: str, out_data: str):
    inp_path = os.path.join(OUT_DIR, f"{prefix}_{idx:02d}.INP")
    out_path = os.path.join(OUT_DIR, f"{prefix}_{idx:02d}.OUT")
    with open(inp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(inp_data.strip() + "\n")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(out_data.strip() + "\n")


def gen_bai01():
    # Bài 1: Nhập a, b (1 <= b <= a <= 10^18). In ra a+b, a-b, a//b, a%b
    fixed = [
        (10, 3),
        (25, 5),
        (10**18, 3),
    ]
    random.seed(101)
    for _ in range(7):
        b = random.randint(1, 10**9)
        a = random.randint(b, 10**18)
        fixed.append((a, b))

    for i, (a, b) in enumerate(fixed, start=1):
        inp = f"{a} {b}"
        out = f"{a + b}\n{a - b}\n{a // b}\n{a % b}"
        write_case("bai01", i, inp, out)


def gen_bai02():
    # Bài 2: Nhập chữ cái hoa C ('A'..'Y') và chuỗi số S. In chữ cái liền sau C và int(S) + 10
    fixed = [
        ("A", "5"),
        ("Y", "0"),
        ("M", "99"),
    ]
    random.seed(102)
    for _ in range(7):
        c = chr(random.randint(ord("A"), ord("Y")))
        s = str(random.randint(1, 10000))
        fixed.append((c, s))

    for i, (c, s) in enumerate(fixed, start=1):
        inp = f"{c} {s}"
        out = f"{chr(ord(c) + 1)}\n{int(s) + 10}"
        write_case("bai02", i, inp, out)


def gen_bai03():
    # Bài 3: Tên (dòng 1), Tuổi và Chiều cao (dòng 2). In "Xin chao <Ten>, <Tuoi> tuoi, cao <ChieuCao:.2f>m!"
    fixed = [
        ("Minh", 8, 1.35),
        ("An", 9, 1.4),
        ("Bo", 10, 1.526),
    ]
    names = ["Binh", "Chi", "Dung", "Ha", "Khanh", "Linh", "Nam"]
    random.seed(103)
    for name in names:
        age = random.randint(7, 15)
        height = round(random.uniform(1.15, 1.75), 3)
        fixed.append((name, age, height))

    for i, (name, age, height) in enumerate(fixed, start=1):
        inp = f"{name}\n{age} {height}"
        out = f"Xin chao {name}, {age} tuoi, cao {height:.2f}m!"
        write_case("bai03", i, inp, out)


def gen_bai04():
    # Bài 4 (Toán hình học thực tế): Mảnh vườn hình chữ nhật chiều dài a, chiều rộng b (1 <= b <= a <= 10^9).
    # In ra 2 dòng: Chu vi = (a + b) * 2 và Diện tích = a * b
    fixed = [
        (5, 3),
        (10, 10),
        (10**9, 10**9),
    ]
    random.seed(104)
    for _ in range(7):
        b = random.randint(1, 10**9)
        a = random.randint(b, 10**9)
        fixed.append((a, b))

    for i, (a, b) in enumerate(fixed, start=1):
        inp = f"{a} {b}"
        out = f"{(a + b) * 2}\n{a * b}"
        write_case("bai04", i, inp, out)


def gen_bai05():
    # Bài 5 (Mua sắm thực tế): Mua n quyển vở giá p đồng/quyển, đưa tờ tiền m đồng (m >= n * p).
    # In ra 2 dòng: Tổng tiền phải trả và Tiền thừa nhận lại
    fixed = [
        (3, 5000, 20000),
        (4, 7500, 30000),
        (100000, 12500, 2000000000),
    ]
    random.seed(105)
    for _ in range(7):
        n = random.randint(1, 10**5)
        p = random.randint(1, 10**4) * 500
        total = n * p
        m = total + random.randint(0, 10**6)
        fixed.append((n, p, m))

    for i, (n, p, m) in enumerate(fixed, start=1):
        total = n * p
        inp = f"{n} {p} {m}"
        out = f"{total}\n{m - total}"
        write_case("bai05", i, inp, out)


def gen_bai06():
    # Bài 6 (Quy đổi thời gian thực tế): Nhập tổng số giây S (0 <= S <= 10^9).
    # Quy đổi ra dạng: H giờ M phút S_rem giây (in 3 số nguyên cách nhau bởi dấu cách)
    fixed = [
        3661,
        59,
        86400,
    ]
    random.seed(106)
    for _ in range(7):
        fixed.append(random.randint(0, 10**9))

    for i, s in enumerate(fixed, start=1):
        h = s // 3600
        m = (s % 3600) // 60
        sec = s % 60
        inp = f"{s}"
        out = f"{h} {m} {sec}"
        write_case("bai06", i, inp, out)


def gen_bai07():
    # Bài 7 (Tính điểm trung bình thực tế): Nhập 3 điểm Toán, Văn, Anh (số thực 0..10).
    # Toán và Văn hệ số 2, Anh hệ số 1. In điểm trung bình làm tròn 2 chữ số thập phân.
    fixed = [
        (8.0, 7.5, 9.0),
        (10.0, 10.0, 10.0),
        (6.25, 7.5, 8.75),
    ]
    random.seed(107)
    for _ in range(7):
        t = round(random.uniform(0, 10), 2)
        v = round(random.uniform(0, 10), 2)
        a = round(random.uniform(0, 10), 2)
        fixed.append((t, v, a))

    for i, (t, v, a) in enumerate(fixed, start=1):
        avg = (t * 2 + v * 2 + a) / 5
        inp = f"{t} {v} {a}"
        out = f"{avg:.2f}"
        write_case("bai07", i, inp, out)


def gen_bai08():
    # Bài 8 (Thuần thuật toán - Tách chữ số): Cho số nguyên dương N có đúng 4 chữ số (1000 <= N <= 9999).
    # In ra 2 dòng: Dòng 1 là tổng 4 chữ số, Dòng 2 là số đảo ngược của N (dạng số nguyên, bỏ số 0 ở đầu nếu có).
    fixed = [
        1234,
        1000,
        9080,
    ]
    random.seed(108)
    for _ in range(7):
        fixed.append(random.randint(1000, 9999))

    for i, n in enumerate(fixed, start=1):
        d1 = n // 1000
        d2 = (n // 100) % 10
        d3 = (n // 10) % 10
        d4 = n % 10
        digit_sum = d1 + d2 + d3 + d4
        rev_num = d4 * 1000 + d3 * 100 + d2 * 10 + d1
        inp = f"{n}"
        out = f"{digit_sum}\n{rev_num}"
        write_case("bai08", i, inp, out)


def gen_bai09():
    # Bài 9 (Thuần thuật toán - Tổng cấp số cộng O(1)): Cho số nguyên dương N (1 <= N <= 10^9).
    # Tính S = 1 + 2 + 3 + ... + N
    fixed = [
        1,
        10,
        10**9,
    ]
    random.seed(109)
    for _ in range(7):
        fixed.append(random.randint(1, 10**9))

    for i, n in enumerate(fixed, start=1):
        ans = n * (n + 1) // 2
        inp = f"{n}"
        out = f"{ans}"
        write_case("bai09", i, inp, out)


def gen_bai10():
    # Bài 10 (Thuần thuật toán - Chia trần / Ceiling Division không dùng float):
    # Cho 2 số nguyên dương A, B (1 <= A, B <= 10^18). Tính ceil(A / B) = (A + B - 1) // B
    fixed = [
        (10, 3),
        (12, 4),
        (10**18, 3),
    ]
    random.seed(110)
    for _ in range(7):
        b = random.randint(1, 10**12)
        a = random.randint(1, 10**18)
        fixed.append((a, b))

    for i, (a, b) in enumerate(fixed, start=1):
        ans = (a + b - 1) // b
        inp = f"{a} {b}"
        out = f"{ans}"
        write_case("bai10", i, inp, out)


if __name__ == "__main__":
    gen_bai01()
    gen_bai02()
    gen_bai03()
    gen_bai04()
    gen_bai05()
    gen_bai06()
    gen_bai07()
    gen_bai08()
    gen_bai09()
    gen_bai10()
    print(f"Generated {len(os.listdir(OUT_DIR))} files in '{OUT_DIR}/'.")
