class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n=len(arr)
        kn=[]
        def pan(arr,n):
            kn.append(n)
            L1=arr[:n]
            L2=arr[n:]
            L1.reverse()
            arr=L1+L2
            return arr 
        while n>1:
            if arr[0]==n:
                arr=pan(arr,n)
            elif arr[n-1]!=n:
                idx=arr.index(n)
                arr=pan(arr,idx+1)
                arr=pan(arr,n)
            n-=1
        return kn

        