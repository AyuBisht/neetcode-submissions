class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #stores val,idx

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackVal, stackIndx = stack.pop()
                res[stackIndx] = i - stackIndx
            stack.append([t,i])
        return res
