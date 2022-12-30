종성들 = [
    # "ㄳ",
    # "ㄵ",
    # "ㄶ",
    # "ㄺ",
    # "ㄻ",
    # "ㄼ",
    # "ㄽ",
    # "ㄾ",
    # "ㄿ",
    # "ㅀ",
    "ㅄ",
]

from Hangul import HangulDecomposer, HangulComposer

# read everything from all.json
import json

with open("all.json", "r") as f:
    all = json.load(f)
    for element in all:
        if len(element) != 1:
            continue
        char = HangulDecomposer(element)
        if char.종성이_있다면() and char.종성 in 종성들:
            print(element)
            char.종성 = "ㅂ"
            print(HangulComposer(char.초성, char.중성, char.종성).합성())
            with open("ㅅㅎ.json", "r") as f:
                data = json.load(f)
                data[element] = HangulComposer(char.초성, char.중성, char.종성).합성() + "ㅎ"
            with open("ㅅㅎ.json", "w") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
