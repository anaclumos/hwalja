import json
import os
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python json-sorter.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Directory does not exist")
        sys.exit(1)

    files = []

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            files.append(filename)

    files.sort()

    final_file = "out.txt"

    for filename in files:
        filepath = os.path.join(directory, filename)
        with open(filepath, "r") as f:
            data = json.load(f)
        # public static let ㄱㅋ = [
        # map
        # ]

        with open(final_file, "a") as f:
            f.write("public static let " + filename[:-5] + " = [\n")
            for key, value in data.items():
                f.write('    "' + key + '": "' + value + '",\n')
            f.write("]\n\n")


main()
