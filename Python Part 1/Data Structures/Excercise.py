from pprint import pprint

sentence = "This is a common interview question"

char_count = {}
for char in sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

pprint(char_count, width=1)

sorted_count = sorted(char_count.items(),
                      key=lambda kv: kv[1],
                      reverse=True)
print(sorted_count[0])
