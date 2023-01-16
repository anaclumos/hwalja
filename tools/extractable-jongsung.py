from Hangul import HangulDecomposer, HangulComposer

# read everything from all.json
import json

with open("reference/all.json", "r") as f:
    all = json.load(f)
    for element in all:
        char = HangulDecomposer(element)
        if char.종성 == "ㅋ":
            # "ㄱㅋ" 누를 경우
            # 앞 글자는 "받침" 딕셔너리에서 찾아서 붙이고
            # 뒷 글자는 "튀어나갈" 딕셔너리에서 찾아서 붙인다.
            원본_종성 = char.종성
            char.종성 = ""
            old_char = HangulComposer(char.초성, char.중성, char.종성).합성()
            new_char = "ㄲ"
            ㄱㅋ = {}
            with open("ㄱㅋ.json", "r") as f:
                ㄱㅋ = json.load(f)
                if element in ㄱㅋ:
                    # print error and exit
                    print("error: already exists", element, old_char, new_char)
                else:
                    ㄱㅋ[element] = old_char + new_char
                    print(old_char, new_char)

            # write the file
            with open("ㄱㅋ.json", "w") as f:
                json.dump(ㄱㅋ, f, ensure_ascii=False, indent=4)
