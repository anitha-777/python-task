# Write a Python program to keep asking the user to enter a password until they enter the correct
user_name="anitha_98"
password="Heloo@3#"
while True:
        pw=input("enter your password")
        if password==pw:
           print("welocome")
           break
else:
    print("enter a valid password")


#  Convert a 2D list into a flat 1D list using list comprehension.
l1=[[1,2],[3,4],[5,6,7]]  
l2=[]
for i in l1:
      l2.extend(i)
print(l2) 

# Given a string, use list comprehension to create a list of all characters, excluding vowels.
a="thelazydog"
l1=[i for i in a if i not in "aeiouAEIOU"]
print(l1)

# ⁠ ⁠From a given list of words, extract only those that start with a vowel (a, e, i, o, u).

words = ["functions", "loops", "oops", "exception", "as"]
v=("a","e","i","o","u","A","E","I","O","U")
for i in words:
     if i.startswith(v):
            print(i)