def calcRedundantBits(m): 
  
 ##Going to use (2**i >= m + i + 1)
 ##repeat and above 0, then return meeting equation value
    for i in range(m): 
        if(2 ** i >= m + i + 1): 
            return i 
  
  
def posRedundantBits(data, s): 
  
  #Redundant bits are placed in positions corresponding to power of 2.
    a = 0
    b = 1
    c = len(data)
    d = ''

    #  when the power was 2, then input 0.
    # if not, then add data.

    for i in range(1, c + s + 1): 
        if(i == 2 ** a): 
            d = d + '0'
            a += 1
        else: 
            d = d + data[-1 * b] 
            b += 1
   #The result is reversed, because the positions are counted backwards.
    return d[::-1] 
  
  
def calcParityBits(arr, r): 
    m = len(arr) 
  
  #Iterate from 0 to r-1 to find the parity bit for rth.
    for i in range(r): 
        valu = 0
        for j in range(1, m + 1): 

            #To find out parity bit, 
            #going to use array or Bitwise OR when position is 1.
            if(j & (2**i) == (2**i)): 
                valu = valu ^ int(arr[-1 * j]) 
                    # [-1 * j] is gave, 
                    #because the array is inverted.

        arr = arr[:m- (2**i)] + str(valu) + arr[m- (2**i) +1:] 
    return arr 
  
  
def detectError(ar, ab): 
    n = len(ar) 
    shin = 0
  
    # One more time for Calculate parity bits.
    for i in range(ab): 
        val = 0
        for j in range(1, n + 1): 
            if(j & (2**i) == (2**i)): 
                val = val ^ int(ar[-1 * j]) 


        #Make a new binary with no adding parity bits
        shin = shin + val*(10**i) 
  
    # Change to demical
    return int(str(shin), 2) 
  
  #Please enter the data to send.
data = '1011001'
  
  #Redundant bits is essential for calculate the number.
m = len(data) 
r = calcRedundantBits(m) 
  
  # Decide redundant bit place.
ar = posRedundantBits(data, r) 

#Decide Parity bits.
ar = calcParityBits(ar, r) 
  
# Transfer the data.
print("Data transferred is " + ar)    


# Change the bit value to simulate transmission errors.
ar = '11101001110'
print("Error data is " + ar) 
Co = detectError(ar, r) 
# Error is in 10th place.
print("Position of the error is " + str(Co)) 