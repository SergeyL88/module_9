# 1 вариант
def all_variants(text):
    len_ = len(text)
    for i in range(1, len_):
        for j in range(len_):
            if j + i > len_:
                yield text
            else:
                yield (text[j:i+j])


# 2 вариант

# def all_variants(text):
#     for i in range(len(text)):
#         for j in range(i + 1, len(text) + 1):
#             yield text[i:j]


a = all_variants("abc")
for i in a:
    print(i)
