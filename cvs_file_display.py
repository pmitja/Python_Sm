from pathlib import Path

data = Path(".", "data", "data.cvs")

if __name__ == "__main__":
    with open(data, "r") as data_r:
        data_r = str(data_r.read())

    row_data = data_r.split(",")

    for x in range(0, len(row_data), 3):
        index = x
        print(f"{row_data[index]} is {row_data[index + 1]} years old and {row_data[index + 2]}.")
