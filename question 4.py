string = input('Enter the vowels :')
count = 0
String = string.lower()
for vowel in String:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u' :
        count+=1
if count == 0:
    print('No vowels found')
else:
    print('Total numbers of vowels are :' + str(count))