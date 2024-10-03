def all_variants(text):
    for i in range(len(text)):
        if i == len(text):
            yield text
        else:
            for j in range(len(text)):
                if i == 0:
                    yield text[j]
                if i == j:
                    continue
                elif i == j+1:
                    yield (text[j]+text[i])
    yield text


a = all_variants("abc")
for i in a:
    print(i)


# a
# b
# c
# ab
# bc
# abc
