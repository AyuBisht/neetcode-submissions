class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map={}
        freq=[[] for i in range(len(nums) +1 )]

        for n in nums:
            map[n] = map.get(n,0) + 1
        
        for i,j in map.items():
            freq[j].append(i)
        
        res = []

        for i in range(len(freq)-1 , 0, -1):
            for n in freq[i]:
                res.append(n)
                if(len(res) == k):
                    return res
                

        
        
        


        