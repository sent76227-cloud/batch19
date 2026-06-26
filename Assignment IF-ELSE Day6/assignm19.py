'''
4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test '''



subscription = input("Enter subscription type: ").lower()
progress = int(input("Enter progress: "))
test_score = int(input("Enter Test Score: "))

if subscription == "premium":
   if progress >= 80:
       if test_score >= 70:
           print("Unlock Certificate")
       else:
           print("Allow Retry")
   else:
       print("complete course")
else:
   if subscription == "basic":
       if progress >= 50:
           print("Allow limited Access")
       else:
           print("Lock content")

   else:
       print("Deny Access")
   
      

  