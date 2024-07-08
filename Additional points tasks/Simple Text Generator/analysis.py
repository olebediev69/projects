from random import choices

alice_in_wonderland_file = open("alice_in_wonderland.txt", "r")

token_set = set()
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def remove_punctuation(word):
    return ''.join(char for char in word if char not in punctuation).strip()

for row in alice_in_wonderland_file:
    row_list = list(row.split(' '))
    cleaned_row_list = [remove_punctuation(word) for word in row_list if word.strip()]
    for i in cleaned_row_list:
        token_set.add(i.lower())

print(' '.join(choices(list(token_set), k=200)))