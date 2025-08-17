def sort_on(items):
    return items["num"]

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    lower = text.lower()
    count = {}

    for char in lower:
        if not (char in count):
            count[char] = 1
        else:
            count[char] += 1
    
    return count

def sort_dict(counts):
    count_list = []
    for count in counts:
        temp_dict = {"char": "", "num": 0}
        temp_dict["char"] = count
        temp_dict["num"] = counts[count]
        count_list.append(temp_dict)
    count_list.sort(reverse=True, key=sort_on)
    return count_list