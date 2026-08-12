'''1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8 '''

feedback = input("Enter Feedback message: ").lower()
count = 0

length = len(feedback)
i = 0
while i<length:
      ch =  feedback[i]


      if ch == "a" or  ch == "i" or ch == "o" or ch == "e" or ch == "u":
         count = count + 1
      print(ch,end="")
      i = i+1
print("Total vowels: ",count) 