class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def decimalToBinary(n):
           return bin(n).replace("0b","")
        def binaryToDecimal(binary):
            decimal, i = 0, 0
            while(binary != 0):
               dec = binary % 10
               decimal = decimal + dec * pow(2, i)
               binary = binary//10
               i += 1
            return decimal
        n=binaryToDecimal(int(a))
        m=binaryToDecimal(int(b))
        x=n+m
        y=str(decimalToBinary(x))
        return y