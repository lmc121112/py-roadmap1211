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


if __name__ == "__main__":
    gen_bai01()
    gen_bai02()
    gen_bai03()
    print(f"Generated {len(os.listdir(OUT_DIR))} files in '{OUT_DIR}/'.")
