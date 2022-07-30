class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurance={}
        for i in nums:
            try:
                occurance[i]+=1
            except:
                occurance[i]=1
        l=[]
        for key,value in occurance.items():
            l.append([value,key])
        l.sort(reverse=True)    
        a=[]    
        for j in range(k):
            a.append(l[j][1])
    
        return a
   

        
        