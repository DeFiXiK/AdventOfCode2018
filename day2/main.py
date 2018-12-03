def main():
    with open('input.txt') as f:
        lines = f.readlines()

        print("Calculate day")
        print(f"Part one, result is {part_one(lines)}")
        print(f"Part two, result is {part_two(lines)}")


def part_one(lines):
    two_count = 0
    three_count = 0
    for line in lines:
        chars = {}
        for letter in line:
            value = chars.get(letter)
            if not value:
                value = 0
            chars[letter] = 1 + value

        if 2 in chars.values():
            two_count += 1
        if 3 in chars.values():
            three_count += 1

    return two_count*three_count


def part_two(lines):
    for a in lines:
        for b in lines:
            delta = 0
            string = ""
            for i in range(len(a)):
                if a[i] != b[i]:
                    delta += 1
                    if (delta > 1):
                        break
                else:
                    string += a[i]
            if delta == 1:
                return string


if __name__ == "__main__":
    main()
