def MathChallenge(strParam):
  # code goes here  
  res=""
  for i in range(len(strParam)//2 ,0 ,-1):
    if len(strParam)%i :
      continue;
    string=strParam[0:i]
    res=string 
    rNumber=(len(strParam)//i)-1 

    for j in range (rNumber):
      string =string+res 
    if string == strParam : 
      return res 
  return -1      

# keep this function call here 
print MathChallenge(raw_input()) 



""""
Have the function MathChallenge(str) take the str parameter being passed and determine if there is some substring K that can be repeated N > 1 times to produce the input string exactly as it appears. Your program should return the longest substring K, and if there is none it should return the string -1.

For example: if str is "abcababcababcab" then your program should return abcab because that is the longest substring that is repeated 3 times to create the final string. Another example: if str is "abababababab" then your program should return ababab because it is the longest substring. If the input string contains only a single character, your program should return the string -1.
""""