fullname=input("enter your full name: ").strip()
id=input("enter your id: ").strip()

names=fullname.replace(" ","")

vowels="aeiou"
vowel_count=0

for name in names:
    if name.lower() in vowels:
        vowel_count+=1

print(vowel_count)

print(len(id))

two_letter=names[:1]
two_digits=id[-2:]
new_string=two_letter+two_digits

if int(two_digits)%2==0:
    print(new_string.upper())
else:
    print(new_string[::-1])