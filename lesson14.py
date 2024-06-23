def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(root_word):
        str = []
        for j in range(*other_words):
            str.append(*other_words)
        same_words.append(str)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)




