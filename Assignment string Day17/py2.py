'''
2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5 '''


chat = input("Enter Chat message: ")
count = 0
length = len(chat)
i = 0 
while i<length:
    ch = chat[i]
    if ch == " ":
      count = count+1
    i = i+1
print("Total spaces: ",count)