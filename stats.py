def get_num_words(contents):
    return len(contents.split())

def get_times_each_char(contents):
    frequency = {}
    for char in contents:
        char = char.lower()
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def sort_dict(dictionary):
  return dict(sorted(dictionary.items(), key=lambda x:x[1], reverse=True))