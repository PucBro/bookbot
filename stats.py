def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count(file_path):
    return len(get_book_text(file_path).split())

def get_chars(file_path):
    dict = {}
    for char in get_book_text(file_path).lower():
        if char not in dict.keys():
            dict[char] = 1
        else:
            dict[char] += 1
    return dict

def sorted_dicts(file_path):
    dic_chars =get_chars(file_path)
    dic_list = []
    for char in dic_chars:
        new_dic = {}
        new_dic["char"] =char
        new_dic["num"] = dic_chars[char]
        dic_list.append(new_dic)
    dic_list.sort(reverse=True, key=lambda x:  x["num"])
    return dic_list




