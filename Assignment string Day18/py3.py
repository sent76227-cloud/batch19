''' 
3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5
'''

com = input("Enter complaint : ")

comp = com.split()
print("Total words: ",len(comp))  
print(type(comp))