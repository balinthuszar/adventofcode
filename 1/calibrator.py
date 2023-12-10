import re


def getInputData():
    f = open("D:\\git\\adventofcode\\1\\data", "r")
    data = f.read()
    f.close()
    return data


def sum_calibration_values(rows: list):
    sum = 0
    for row in rows:
        numbers_in_row = re.findall("[0-9]", row)
        value_of_row = numbers_in_row[0] + numbers_in_row[-1]
        sum += int(value_of_row)
    return sum


def main():
    data = getInputData()
    rows = data.split("\n")
    print(sum_calibration_values(rows))


if __name__ == "__main__":
    main()
