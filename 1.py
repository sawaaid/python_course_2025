def reverse_each_word(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

text = " تاكبشلاب ةطبترلما جماربلا"
reversed_text = reverse_each_word(text)
print(reversed_text)