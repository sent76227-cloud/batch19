'''

2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:


Python is powerful


Output:


lufrewop si nohtyP
'''

s = input("Enter stirng: ")
ns = s.split()
result = " "
for n in range(0,len(ns)):
      ch = ns[n]
      rev = " "
      for x in range(0,len(ch)):
            rev =ch[x]+rev
      result = rev+ result
print("Result: ",result)
            









'''
s=input("Enter String: ")
ns=s.split()
cs=''
for i in range(0,len(ns)):
     nw=''
     for j in range(0,len(ns[i])):
           nw=ns[i][j]+nw
     cs=nw+' '+cs
print(cs)'''