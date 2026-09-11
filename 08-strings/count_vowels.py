vowels = "auieoAUOIE"
sentence = input("enter the sentence: ").strip()

sum_vowels = 0
for charector in sentence :
    if charector in vowels :
        sum_vowels += 1
        
print(sum_vowels)