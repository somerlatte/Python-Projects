def PTLetterCount(strParam):
    words = strParam.split()
    max_count = 0 
    max_word = -1
    for word in words:
        count = 0
        for letter in word:
            if word.count(letter) > 1:
                count += 1
        if count > max_count:
            max_count = count
            max_word = word
    return max_word

# Mantenha esta chamada de função aqui
print(PTLetterCount(input()))
