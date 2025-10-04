def isPalindrome(self, s: str) -> bool:
        import re

        words = re.split(r'/W+',s)

        words = [w for w in words if w]
        
        
        left=0
        right=len(words)-1

        while left<right:
            if words[left]!=words[right]:
                return False
            left+=1
            right-=1
        return True