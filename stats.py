def seeker(text):    
    words = text.split()
    return len(words)

def stat(text):
    text = text.lower()
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

def sort_char(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
