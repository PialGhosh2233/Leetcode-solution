class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=len(digits)-1
        val=0
        b=0
        li=[]
        for i in digits:
            b=i*pow(10,c)
            val=val+b
            c=c-1
        val=val+1    
        x=str(val)
        for j in x:
            li.append(int(j))
        return li