def reversed_words(s):
    r=' '.join(reversed(s.split(' ')))
    return r

s=input('Enter a string : ')
print(reversed_words(s))