from collections import defaultdict


def main():
    with open('input.txt') as f:
        lines = f.readlines()
        data = [parse(line) for line in lines]

        overlaps = defaultdict(int)
        for _, l, t, w, h in data:
            for i in range(w):
                for j in range(h):
                    overlaps[(i + l, j + t)] += 1

        print("Calculate day")
        print(f"Part one, result is {part_one(overlaps)}")
        print(f"Part two, result is {part_two(data, overlaps)}")


def parse(line):
    ids, _, offset, d = line.split()
    left, top = offset[:-1].split(",")
    width, height = d.split("x")
    return ids, int(left), int(top), int(width), int(height)


def part_one(overlaps):
    total = 0
    for v in overlaps.values():
        if v > 1:
            total += 1

    return total


def part_two(data, overlaps):
    for ids, l, t, w, h in data:
        is_valid = True
        for i in range(w):
            for j in range(h):
                if overlaps[(i + l, j + t)] != 1:
                    is_valid = False
                    break
            if not is_valid:
                break
        if is_valid:
            return(ids[1:])


if __name__ == "__main__":
    main()
