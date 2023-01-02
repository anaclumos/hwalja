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
    "ㄱ": "ᄀᆞ",
    "ㄲ": "ᄁᆞ",
    "ㄳ": "ᄉᆞ",
    "ㄴ": "ᄂᆞ",
    "ㄵ": "ᄌᆞ",
    "ㄶ": "ᄒᆞ",
    "ㄷ": "ᄃᆞ",
    "ㄹ": "ᄅᆞ",
    "ㄺ": "ᄀᆞ",
    "ㄻ": "ᄆᆞ",
    "ㄼ": "ᄇᆞ",
    "ㄽ": "ᄉᆞ",
    "ㄾ": "ᄐᆞ",
    "ㄿ": "ᄑᆞ",
    "ㅁ": "ᄆᆞ",
    "ㅂ": "ᄇᆞ",
    "ㅄ": "ᄉᆞ",
    "ㅅ": "ᄉᆞ",
    "ㅆ": "ᄊᆞ",
    "ㅇ": "ᄋᆞ",
    "ㅈ": "ᄌᆞ",
    "ㅊ": "ᄎᆞ",
    "ㅋ": "ᄏᆞ",
    "ㅌ": "ᄐᆞ",
    "ㅍ": "ᄑᆞ",
    "ㅀ": "ᄒᆞ",
    "ㅎ": "ᄒᆞ",
}

with open("all.json", "r") as f:
    all = json.load(f)
    for element in all:
        char = HangulDecomposer(element)
        if char.종성이_있다면():
            # "천" 누를 경우
            # 앞 글자는 "받침" 딕셔너리에서 찾아서 붙이고
            # 뒷 글자는 "튀어나갈" 딕셔너리에서 찾아서 붙인다.
            원본_종성 = char.종성
            char.종성 = 받침[원본_종성]
            old_char = HangulComposer(char.초성, char.중성, char.종성).합성()
            new_char = 튀어나갈[원본_종성]
            # print(element, old_char, new_char)
            # open the file
            천 = {}
            with open("천.json", "r") as f:
                천 = json.load(f)
                if element in 천:
                    # print error and exit
                    print("error: already exists", old_char, new_char)
                else:
                    천[element] = old_char + new_char
                    print(old_char, new_char)

            # write the file
            with open("천.json", "w") as f:
                json.dump(천, f, ensure_ascii=False, indent=4)
