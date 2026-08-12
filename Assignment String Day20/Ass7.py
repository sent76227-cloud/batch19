'''
7. Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.

``
hello hello how are are you


Output:


hello how are you
```

'''
s=input('Enter String:')
newstr=''
s1=s.split()
for i in s1:
    if i not in newstr:
        newstr+=i+' '
print(newstr)        