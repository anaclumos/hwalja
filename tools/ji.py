from Hangul import HangulDecomposer, HangulComposer

# read everything from all.json
import json

중성들 = [
    "ㅗ",
    "ㅛ",
    "ㅡ",
]

이전_상태 = {
    "ㅗ": "ᆞ",
    "ㅛ": "ᆢ",
    "ㅡ": "",
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
            # open 지.json
            지 = {}
            with open("지.json", "r") as f:
                지 = json.load(f)
                지[이전글자] = element
            # write 지.json
            with open("지.json", "w") as f:
                json.dump(지, f, ensure_ascii=False, indent=4)
