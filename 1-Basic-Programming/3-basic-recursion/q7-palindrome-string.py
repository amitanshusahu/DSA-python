def is_palindrome(str, left, right):
    if right <= left:
        return True
    if str[left] == str[right]:
        is_palindrome(str, left + 1, right - 1)
    else:
        return False

str = "nun"
if is_palindrome(str, 0, len(str) - 1):
    print(f"Then given string {str} is plaindrome")
else:
    print(f"Then given string {str} is not plaindrome")
