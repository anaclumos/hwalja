from Hangul import HangulDecomposer, HangulComposer

# read everything from all.json
import json

with open("reference/all.json", "r") as f:
    all = json.load(f)
    for element in all:
        char = HangulDecomposer(element)
        if char.종성 == "ㅊ":
            # "ㅈㅊ" 누를 경우
            # 앞 글자는 "받침" 딕셔너리에서 찾아서 붙이고
            # 뒷 글자는 "튀어나갈" 딕셔너리에서 찾아서 붙인다.
            원본_종성 = char.종성
            char.종성 = ""
            old_char = HangulComposer(char.초성, char.중성, char.종성).합성()
            new_char = "ㅉ"
            ㅈㅊ = {}
            with open("ㅈㅊ.json", "r") as f:
                ㅈㅊ = json.load(f)
                if element in ㅈㅊ:
                    # print error and exit
                    print("error: already exists", old_char, new_char)
                else:
                    ㅈㅊ[element] = old_char + new_char
                    print(old_char, new_char)

            # write the file
            with open("ㅈㅊ.json", "w") as f:
                json.dump(ㅈㅊ, f, ensure_ascii=False, indent=4)
