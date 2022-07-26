class Solution:
    def fizzBuzz(self, t: int) -> List[str]:
    
        l=[]

        for i in range(1,t+1):
        
            if int(i%3==0 and i%5==0):
       
                  l.append('FizzBuzz')
            elif int(i)%5==0:
       
                    l.append('Buzz')
            elif int(i)%3==0:
        
                 l.append('Fizz')
    
            else:
                l.append(str(i))
      
    
        return l
