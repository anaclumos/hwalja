from Hangul import HangulDecomposer, HangulComposer

# read everything from all.json
import json

중성들 = [
    "ㅐ",
    "ㅒ",
    "ㅓ",
    "ㅔ",
    "ㅕ",
    "ㅖ",
    "ㅙ",
    "ㅚ",
    "ㅝ",
    "ㅞ",
    "ㅟ",
    "ㅢ",
    "ㅣ",
]


이전_상태 = {
    "ㅐ": "ㅏ",
    "ㅒ": "ㅑ",
    "ㅓ": chr(4510),
    "ㅔ": "ㅓ",
    "ㅕ": chr(4510) + chr(4510),
    "ㅖ": "ㅕ",
    "ㅙ": "ㅘ",
    "ㅚ": "ㅗ",
    "ㅝ": "ㅠ",
    "ㅞ": "ㅝ",
    "ㅟ": "ㅜ",
    "ㅢ": "ㅡ",
    "ㅣ": "",
}


with open("all.json", "r") as f:
    all = json.load(f)
    for element in all:
        if len(element) != 1:
            continue
        char = HangulDecomposer(element)
        if char.중성 in 중성들 and not char.종성이_있다면():
            이전상태 = 이전_상태[char.중성]
            새한글 = HangulComposer(char.초성, 이전상태, char.종성)
            이전글자 = ""
            try:
                이전글자 = 새한글.합성()
            except:
                이전글자 = char.초성 + 이전상태
            print(이전글자, element)
            # open 인.json
            인 = {}
            with open("인.json", "r") as f:
                인 = json.load(f)
                인[이전글자] = element
            # write 인.json
            with open("인.json", "w") as f:
                json.dump(인, f, ensure_ascii=False, indent=4)
