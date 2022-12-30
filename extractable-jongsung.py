from tools.Hangul import HangulDecomposer, HangulComposer

# read everything from all.json
import json

받침 = {
    "ㄱ": "",
    "ㄲ": "",
    "ㄳ": "ㄱ",
    "ㄴ": "",
    "ㄵ": "ㄴ",
    "ㄶ": "ㄴ",
    "ㄷ": "",
    "ㄹ": "",
    "ㄺ": "ㄹ",
    "ㄻ": "ㄹ",
    "ㄼ": "ㄹ",
    "ㄽ": "ㄹ",
    "ㄾ": "ㄹ",
    "ㄿ": "ㄹ",
    "ㅀ": "ㄹ",
    "ㅁ": "",
    "ㅂ": "",
    "ㅄ": "ㅂ",
    "ㅅ": "",
    "ㅆ": "",
    "ㅇ": "",
    "ㅈ": "",
    "ㅊ": "",
    "ㅋ": "",
    "ㅌ": "",
    "ㅍ": "",
    "ㅎ": "",
}

튀어나갈 = {
    "ㄱ": "ㄱ",
    "ㄲ": "ㄲ",
    "ㄳ": "ㅅ",
    "ㄴ": "ㄴ",
    "ㄵ": "ㅈ",
    "ㄶ": "ㅎ",
    "ㄷ": "ㄷ",
    "ㄹ": "ㄹ",
    "ㄺ": "ㄱ",
    "ㄻ": "ㅁ",
    "ㄼ": "ㅂ",
    "ㄽ": "ㅅ",
    "ㄾ": "ㅌ",
    "ㄿ": "ㅍ",
    "ㅀ": "ㅎ",
    "ㅁ": "ㅁ",
    "ㅂ": "ㅂ",
    "ㅄ": "ㅅ",
    "ㅅ": "ㅅ",
    "ㅆ": "ㅆ",
    "ㅇ": "ㅇ",
    "ㅈ": "ㅈ",
    "ㅊ": "ㅊ",
    "ㅋ": "ㅋ",
    "ㅌ": "ㅌ",
    "ㅍ": "ㅍ",
    "ㅎ": "ㅎ",
}

with open("all.json", "r") as f:
    all = json.load(f)
    for element in all:
        char = HangulDecomposer(element)
        if char.종성이_있다면():
            # "지" 누를 경우
            # 앞 글자는 "받침" 딕셔너리에서 찾아서 붙이고
            # 뒷 글자는 "튀어나갈" 딕셔너리에서 찾아서 붙인다.
            char.종성 = 받침[char.종성]
            old_char = HangulComposer(char.초성, char.중성, char.종성).합성()
            new_char = HangulComposer(char.초성, "ㅡ", "").합성()
            print(element, old_char, new_char)
