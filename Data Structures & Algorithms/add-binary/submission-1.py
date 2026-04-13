class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        len_a, len_b = len(a), len(b)

        if len_a < len_b:
            a = '0'*(len_b-len_a) + a
        else:
            b = '0'*(len_a-len_b) + b

        finallen = len(a)
        carry = 0
        res = ""
        for i in range(finallen-1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry
            currSum = str(total % 2)
            carry = total // 2
            res = currSum + res

        return str(carry)+res if carry == 1 else res

