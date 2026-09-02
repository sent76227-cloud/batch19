'''
3.
Reverse Sentence + Reverse Each Word(3 marks)

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:

```
Python is powerful
```

Output:

```
lufrewop si nohtyP 
'''


s = input("Enter String: ")
result = " "
word = s.split()

for n in range(0,len(word)):
     ch = word[n]
     rev = " "
     for x in range(0,len(ch)):
        rev = ch[x]+rev
     result = rev + result 
print("Result",result)
   


    











