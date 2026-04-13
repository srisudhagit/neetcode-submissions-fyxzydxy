class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                ind = stack.pop()
                result[ind] = i-ind

            stack.append(i)

        return result