
# Python3 implementation of the approach 
import sys 
  
# Function that returns True if the array 
# can be made increasing or decreasing 
# after rotating it in any direction 
def isPossible(a, n): 
  
    # If size of the array is less than 3 
    if (n <= 2): 
        return True; 
  
    flag = 0; 
      
    # Check if the array is already decreasing 
    for i in range(n - 2): 
        if (not(a[i] > a[i + 1] and 
                a[i + 1] > a[i + 2])):  
            flag = 1; 
            break; 
          
    # If the array is already decreasing 
    if (flag == 0): 
        return True; 
  
    flag = 0; 
      
    # Check if the array is already increasing 
    for i in range(n - 2):  
        if (not(a[i] < a[i + 1] and 
                a[i + 1] < a[i + 2])):  
            flag = 1; 
            break; 
          
    # If the array is already increasing 
    if (flag == 0): 
        return True; 
  
    # Find the indices of the minimum 
    # and the maximum value 
    val1 = sys.maxsize; mini = -1;  
    val2 = -sys.maxsize; maxi = -1; 
    for i in range(n):  
        if (a[i] < val1):  
            mini = i; 
            val1 = a[i]; 
          
        if (a[i] > val2):  
            maxi = i; 
            val2 = a[i]; 
      
    flag = 1; 
      
    # Check if we can make array increasing 
    for i in range(maxi): 
        if (a[i] > a[i + 1]):  
            flag = 0; 
            break; 
  
    # If the array is increasing upto max index 
    # and minimum element is right to maximum 
    if (flag == 1 and maxi + 1 == mini):  
        flag = 1; 
          
        # Check if array increasing again or not 
        for i in range(mini, n - 1): 
            if (a[i] > a[i + 1]):  
                flag = 0; 
                break; 
              
        if (flag == 1): 
            return True; 
      
    flag = 1; 
      
    # Check if we can make array decreasing 
    for i in range(mini): 
        if (a[i] < a[i + 1]):  
            flag = 0; 
            break; 
          
    # If the array is decreasing upto min index 
    # and minimum element is left to maximum 
    if (flag == 1 and maxi - 1 == mini):  
        flag = 1; 
  
        # Check if array decreasing again or not 
        for i in range(maxi, n - 1): 
            if (a[i] < a[i + 1]):  
                flag = 0; 
                break; 
          
        if (flag == 1): 
            return True; 
      
    # If it is not possible to make the 
    # array inreasing or decreasing 
    return False; 
  
# Driver code 
while(1):
    n = int(input())
    a=input()
    a=list(map(int,a.split(",")))
      
    if (isPossible(a, n)): 
        print("Yes"); 
    else: 
        print("No");
