import json
import os
import sys

all_data = {}


def main():
    if len(sys.argv) != 2:
        print("Usage: python json-sorter.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print("Directory does not exist")
        sys.exit(1)

    for filename in os.listdir(directory):
        if (
            filename.endswith(".json")
            and filename != "한글.json"
            and filename != "all_data.json"
            and filename != "한글.min.json"
        ):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as f:
                data = json.load(f)
                all_data[filename.split(".")[0]] = data

    # save as file
    with open("all_data.json", "w") as f:
        json.dump(all_data, f, indent=4, sort_keys=True, ensure_ascii=False)


main()
