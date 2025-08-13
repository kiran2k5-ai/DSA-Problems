class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        pal = ""

        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                pal += s[i].lower()
        
        if pal == pal[::-1]:
            return True
        else:
            return False


        
