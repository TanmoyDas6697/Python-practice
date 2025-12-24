x = str(input("What is the sentence? "))
vowels = "aeiouAEIOU"
count = 0
for i in x:
    if i in vowels:
        count += 1
print("Number of vowels:", count)   