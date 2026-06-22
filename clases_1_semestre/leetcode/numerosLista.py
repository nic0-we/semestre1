l1 = [2, 4, 3]
l2 = [5, 6, 4]

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = []
        i = 0

        while i < len(l1) or i < len(l2) or carry:
            x = l1[i] if i < len(l1) else 0
            y = l2[i] if i < len(l2) else 0
            total = x + y + carry
            result.append(total % 10)
            carry = total // 10
            i += 1

        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.addTwoNumbers(l1, l2))
