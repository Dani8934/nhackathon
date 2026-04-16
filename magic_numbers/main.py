from pathlib import Path

def next_magic_num(number):
    if "^" in str(number):
        number = str(eval(str(number).replace("^", "**")))

    num_list = list(map(int, str(number).strip()))
    num_len = len(num_list)

    mirrored = mirror(num_list)

    if int("".join(map(str, mirrored))) > int(number):
        return int("".join(map(str, mirrored)))

    if all(x == 9 for x in num_list):
        return (int("".join(map(str, num_list))) + 2)

    i = (num_len - 1) // 2
    while i >= 0:
        if num_list[i] < 9:
            num_list[i] += 1
            break
        num_list[i] = 0
        i -= 1

    num_list = mirror(num_list)

    return int("".join(map(str, num_list)))


def mirror(list):
        for i in range(len(list) // 2):
            list[len(list) - 1 - i] = list[i]
        return list

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        print(next_magic_num(line), end="\n")


if __name__ == "__main__":
    main()
