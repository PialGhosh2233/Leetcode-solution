class Solution:
    def reverse(self, x: int) -> int:
        r=0
        if x>0:
          while x>0:
            re=x%10
            r =(r*10)+re
            x = x//10
        elif x<0:
           x=x*-1
           while x>0:
            re=x%10
            r =(r*10)+re
            x = x//10
           r=r*-1       
        if r>=-2147483648 and r<=2147483647:
            return r
        else:
            return 0
