from pathlib import Path
import math

def min_num_of_drop(N, H):
    k = 1
    while S(k, N) < H:
        k += 1
    return k

def S(k, n):
    return sum(math.comb(k, i) for i in range(1, n + 1))

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        line = line.split(", ")
        print(min_num_of_drop(int(line[0]), int(line[1])), end="\n")


if __name__ == "__main__":
    main()
