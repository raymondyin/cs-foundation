class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        holder = []

        for char in s:
            if char == "(":
                holder.append(char)
            elif char == ")":
                for index, element in reversed(enumerate(holder)):
                    if element == "(":
                        print(holder)
                        result = self._evaluate(''.join(holder[index + 1:]))
                        holder = holder[:index]
                        holder.append(result)
                        break
            elif char == " ":
                continue
            else:
                holder.append(char)
        return self._evaluate(str(holder))

    def _evaluate(self, str):
        # print(str)
        if "+" in str:
            temp = str.split("+")
            first = temp[0]
            second = temp[1]
            return str(int(first) + int(second))
        elif "-" in str:
            temp = str.split("-")
            first = temp[0]
            second = temp[1]
            return str(int(first) - int(second))
        else:
            return str
a = Solution()
a.calculate("1 + 1")

