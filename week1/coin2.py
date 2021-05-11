

def change(amount,length,coins,cache):   
    if length ==0    :  return 0
    if(amount == 0)     :  return 1
    
    
    
    if (amount,length )in cache:
        return cache[(amount,length)]
    
    result = change(amount,length-1,coins[:-1],cache)
    
    if  amount-coins[length-1] >=0 :
        result = result + change(amount-coins[-1],length,coins,cache)
    
    
    cache[amount, length] = result
    
    return result

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return change(amount,len(coins),coins,{})