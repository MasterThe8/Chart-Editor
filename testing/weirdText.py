list1 = ['Ａ', 'Ｂ', 'Ｃ', 'Ｄ', 'Ｅ', 'Ｆ', 'Ｇ', 'Ｈ', 'Ｉ', 'Ｊ', 'Ｋ', 'Ｌ', 'Ｍ', 'Ｎ', 'Ｏ', 'Ｐ', 'Ｑ', 'Ｒ', 'Ｓ', 'Ｔ', 'Ｕ', 'Ｖ', 'Ｗ', 'Ｘ', 'Ｙ', 'Ｚ']
list2 = ['ᴀ', 'ʙ', 'ᴄ', 'ᴅ', 'ᴇ', 'F', 'ɢ', 'ʜ', 'ɪ', 'ᴊ', 'ᴋ', 'ʟ', 'ᴍ', 'ɴ', 'ᴏ', 'ᴘ', 'Q', 'ʀ', 's', 'ᴛ', 'ᴜ', 'ᴠ', 'ᴡ', 'x', 'ʏ', 'ᴢ']
list3 = ['Z', 'y', 'X', 'M', 'Λ', '∩', '⊥', 'S', 'ᴚ', 'Ό', 'Ԁ', 'O', 'N', 'W ˥', 'k', 'ſ', 'I', 'H', '⅁', 'Ⅎ', 'Ǝ', 'D', 'Ɔ', 'B', '∀']
list4 = ['Ⓐ', 'Ⓑ', 'Ⓒ', 'Ⓓ', 'Ⓔ', 'Ⓕ', 'Ⓖ', 'Ⓗ', 'Ⓘ', 'Ⓙ', 'Ⓚ', 'Ⓛ', 'Ⓜ', 'Ⓝ', 'Ⓞ', 'Ⓟ', 'Ⓠ', 'Ⓡ', 'Ⓢ', 'Ⓣ', 'Ⓤ', 'Ⓥ', 'Ⓦ', 'Ⓧ', 'Ⓨ', 'Ⓩ']
list5 = ['ᴬ', 'ᴮ', 'ᶜ', 'ᴰ', 'ᴱ', 'ᶠ', 'ᴳ', 'ᴴ', 'ᴵ', 'ᴶ', 'ᴷ', 'ᴸ', 'ᴹ', 'ᴺ', 'ᴼ', 'ᴾ', 'Q', 'ᴿ', 'ˢ', 'ᵀ', 'ᵁ', 'ⱽ', 'ᵂ', 'ˣ', 'ʸ', 'ᶻ']
list6 = ['🄰', '🄱', '🄲', '🄳', '🄴', '🄵', '🄶', '🄷', '🄸', '🄹', '🄺', '🄻', '🄼', '🄽', '🄾', '🄿', '🅀', '🅁', '🅂', '🅃', '🅄', '🅅', '🅆', '🅇', '🅈', '🅉']


input_text = "Test"
text1 = ""

import codecs

with codecs.open("weird", "r", "utf-8") as file:
    list_text = file.read()

# char_list = list(list_text)

# char_list = [list_text[i:i+3] for i in range(0, len(list_text), 3)]
char_list = [list_text[i:i+2] for i in range(0, len(list_text), 2)]

print(char_list)

for char in input_text:
    if char.isalpha():
        index = ord(char.upper()) - ord('A')
        if index >= 0 and index < len(char_list):
            text1 += char_list[index]
    else:
        text1 += char

print(text1)