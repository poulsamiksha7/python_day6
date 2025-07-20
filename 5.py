#Q1 Count vowels
text=input("Enter Your Text: ")

vowels="aeiouAEIOU"

count=0

for ch in text:
    if ch in vowels:
        count += 1
print("Count of Vowels in Text is",count)

#Q2 Reverse string
text= input("Enter Your Text: ")

reverse_str=text[::-1]

print("Reverse String is",reverse_str)

#Q3  Palindrome check
text=input("Enter your Text: ")

if text==text[::-1]:
    print("It is Palindrome")
else:
    print("It is not Palindrome")

#Q4  Word frequency

text=input("Enter Sentense")
words=text.split()

freq={}

for word in words:
 word=word.lower()
 if word in freq:
  freq[word] +=1
 else:
  freq[word] =1

for word, count in freq.items():
 print(f"{word}:{count}")

#Q5 - Remove punctuation
import string

text=input("Enter Text: ")
text=text.translate(str.maketrans('','',string.punctuation))

words=text.lower().split()

freq={}

for word in words:
    freq[word]=freq.get(word,0)+1

for word, count in freq.items():
    print(f"{word}:{count}")    

    #Q6  Find longest word
text=input("Enter your text: ")
import string
text=text.translate(str.maketrans('','',string.punctuation))
words=text.split()
longest=""
for word in words:
        if len(word)>len(longest):
            longest=word
print("The longest word is: ",longest)
print("The count of word is: ",len(longest))

#Q7 Replace substring
text="Samiksha is kind girl"
new_str=text.replace("kind","good")

print(new_str)

#Q8  Title case
text=input("Enter your text")
new_txt=text.title()
print(new_txt)

#Q9 Remove whitespace
text="   Hello Python           "
clean_text=text.strip()
print(clean_text)

#Q10  Sort characters alphabetically

text=input("Enter your text")
text=text.replace(" ","")

new_txt="".join(sorted(text))
print(new_txt)