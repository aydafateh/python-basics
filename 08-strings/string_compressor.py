text = input("Enter the text:")
result = ""
count = 1
for ch in range(1, len(text)):
    if text[ch] == text[ch - 1]:
        count += 1
    else:
        result += text[ch-1] + str(count)
        count = 1
result += text[-1] + str(count)
print(result)
