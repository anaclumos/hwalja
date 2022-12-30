from Hangul import HangulDecomposer, HangulComposer

# read everything from all.json
import json

중성들 = ["ㅏ", "ㅑ", "ㅜ", "ㅠ", "ㅘ"]

이전_상태 = {"ㅏ": "ㅣ", "ㅑ": "ㅏ", "ㅜ": "ㅡ", "ㅠ": "ㅜ", "ㅘ": "ㅚ"}


with open("all.json", "r") as f:
    all = json.load(f)
    for element in all:
        if len(element) != 1:
            continue
        char = HangulDecomposer(element)
        if char.중성 in 중성들 and not char.종성이_있다면():
            이전상태 = 이전_상태[char.중성]
            새한글 = HangulComposer(char.초성, 이전상태, char.종성)
            이전글자 = 새한글.합성()
            print(이전글자, element)
            # open 천.json
            천 = {}
            with open("천.json", "r") as f:
                천 = json.load(f)
                천[이전글자] = element
            # write 천.json
            with open("천.json", "w") as f:
                json.dump(천, f, ensure_ascii=False, indent=4)
