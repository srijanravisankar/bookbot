def word_count(text: str) -> int:
    words = text.split()
    return len(words)

def char_count(text: str) -> dict[str, int]:
    chars_dict = {}
    for char in text:
        char = char.lower()
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_dict(chars_dict: dict[str, int]) -> list[dict]:
    chars_list = []
    
    for char, chr_count in chars_dict.items():
        char_dict = {"char": char, "num": chr_count}
        chars_list.append(char_dict)
        
    def sort_on(items):
        return items["num"]
        
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
    
    
    