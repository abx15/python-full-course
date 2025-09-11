# check if a string is a palindrome


text = input("Enter a string: ")
cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("✅ Palindrome")
else:
    print("❌ Not a Palindrome")