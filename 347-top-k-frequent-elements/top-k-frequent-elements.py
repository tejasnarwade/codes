class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topkfreq = []
        freq : dict[int,int]={}
        for n in nums:
            freq[n] = freq.get(n,0)+1
        srted_freq = dict(sorted(freq.items(), key=lambda item: item[1],reverse=True))
        for key,val in srted_freq.items():
            if k!=0:
                topkfreq.append(key)
                k-=1
        return topkfreq
        