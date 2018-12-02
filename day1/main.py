
def main():
    with open('input.txt') as f:
        lines = f.readlines()

        print("Calculate day 1")
        print(f"Part one, result is {part_one(lines)}")
        print(f"Part two, result is {part_two(lines)}")


def part_one(lines):
    total = 0
    for line in lines:
        try:
            value = int(line)
        except ValueError as e:
            raise(f"Input error, except {line}")
        total += value
    return total


def part_two(lines):
    total = 0
    items = set()
    while True:
        for line in lines:
            try:
                value = int(line)
            except ValueError as e:
                raise(f"Input error, except {line}")
            total += value

            if total in items:
                return total

            items.add(total)


if __name__ == "__main__":
    main()
