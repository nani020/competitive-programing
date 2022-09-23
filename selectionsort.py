class Solution: 
    def selectionSort(self, arr,n):
         for i in range(n):
            min= i
            for j in range(i+1,len(arr)):
                if arr[min]>arr[j]:
                    min=j
            arr[i],arr[min]=arr[min],arr[i]
