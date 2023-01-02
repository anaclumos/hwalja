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

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as f:
                data = json.load(f)
            with open(filepath, "w") as f:
                json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)


main()
