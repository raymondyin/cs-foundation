class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        queue = []
        dic = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in "([{":
                queue.append(char)
            elif char in "]})":
                if len(queue) == 0 or queue.pop() != dic[char]:
                    return False
        return len(queue) == 0

