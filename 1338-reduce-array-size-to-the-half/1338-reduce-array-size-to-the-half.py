class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        occurance={}
        for i in arr:
            try:
                occurance[i]+=1
            except:
                occurance[i]=1
        l=[]
        for key,value in occurance.items():
            l.append(value)
        l.sort(reverse=True)
        size=len(arr)
        c=0
        for j in range(size):
            c+=l[j]
            if c>=size//2:
                return j+1
        
        