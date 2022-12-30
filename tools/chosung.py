from Hangul import HangulDecomposer, HangulComposer

# read everything from all.json
import json

초성들 = [
    "ㄱ",
    "ㄲ",
    "ㄴ",
    "ㄷ",
    "ㄸ",
    "ㄹ",
    "ㅁ",
    "ㅂ",
    "ㅃ",
    "ㅅ",
    "ㅆ",
    "ㅇ",
    "ㅈ",
    "ㅉ",
    "ㅊ",
    "ㅋ",
    "ㅌ",
    "ㅍ",
    "ㅎ",
]

이전_상태 = {
    "ㄱ": "",
    "ㄲ": "ㅋ",
    "ㄴ": "",
    "ㄷ": "",
    "ㄸ": "ㅌ",
    "ㄹ": "ㄴ",
    "ㅁ": "ㅇ",
    "ㅂ": "",
    "ㅃ": "ㅍ",
    "ㅅ": "",
    "ㅆ": "ㅎ",
    "ㅇ": "",
    "ㅈ": "",
    "ㅉ": "ㅊ",
    "ㅊ": "ㅈ",
    "ㅋ": "ㄱ",
    "ㅌ": "ㄷ",
    "ㅍ": "ㅂ",
    "ㅎ": "ㅅ",
}

누른_버튼 = {
    "ㄱ": "ㄱ",
    "ㄲ": "ㄱ",
    "ㄴ": "ㄴ",
    "ㄷ": "ㄷ",
    "ㄸ": "ㄷ",
    "ㄹ": "ㄴ",
    "ㅁ": "ㅇ",
    "ㅂ": "ㅂ",
    "ㅃ": "ㅂ",
    "ㅅ": "ㅅ",
    "ㅆ": "ㅅ",
    "ㅇ": "ㅇ",
    "ㅈ": "ㅈ",
    "ㅉ": "ㅈ",
    "ㅊ": "ㅈ",
    "ㅋ": "ㄱ",
    "ㅌ": "ㄷ",
    "ㅍ": "ㅂ",
    "ㅎ": "ㅅ",
}

직접_누를_수_있는_자소 = ["ㄱ", "ㄴ", "ㄷ", "ㅂ", "ㅅ", "ㅈ", "ㅇ"]

대응되는_파일 = {
    "ㄱ": "ㄱㅋ.json",
    "ㄴ": "ㄴㄹ.json",
    "ㄷ": "ㄷㅌ.json",
    "ㅂ": "ㅂㅍ.json",
    "ㅅ": "ㅅㅎ.json",
    "ㅈ": "ㅈㅊ.json",
    "ㅇ": "ㅇㅁ.json",
}


with open("all.json", "r") as f:
    all = json.load(f)
    for element in all:
        char = HangulDecomposer(element)
        if not char.종성이_있다면() and not char.중성이_있다면() and char.초성이_있다면():
            초성 = char.초성.strip()
            이전상태 = 이전_상태[초성]
            누른버튼 = 누른_버튼[초성]

            with open(대응되는_파일[누른버튼], "r") as f:
                data = json.load(f)
                if 이전상태 in data:
                    print("이전상태가 있음")
                else:
                    data[이전상태] = element
                with open(대응되는_파일[누른버튼], "w") as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
