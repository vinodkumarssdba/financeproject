text="programming"
count=0
i=0
while i < len(text):
    if text[i] in "aeiou":
        count+=1
    i+=1
print(count)