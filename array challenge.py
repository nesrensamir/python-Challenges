def ArrayChallenge(strArr):

  # code goes here 
  testArr=[]
  secTestArr=[]
  testFirstPart=[]
  firstPart=""

  testSecondPart=[]
  secondPart="" 

  firstItemList= list(strArr[0])
  secondItemList= strArr[1].split(",")
  for i in range(len(firstItemList)):
    testArr.append(firstItemList[i])
    for k in range (len(secondItemList)):
      if ''.join(testArr) == secondItemList[k]:
        testFirstPart.append(secondItemList[k]) 
  firstPart=max(testFirstPart)   
  testArr=[]
  secTestArr=firstItemList[len(firstPart):]
  for i in range (len(secTestArr)):
    testArr.append(secTestArr[i])
    for k in range (len(secondItemList)):
      if ''.join(testArr)==secondItemList[k]:
        testSecondPart.append(secondItemList[k])
  secondPart=max(testSecondPart)

  
  if firstPart and secondPart :
   
    return(",".join([firstPart,secondPart]))
  else :
    return ("not possible")  
  
    
       
    


  #print(strArr[1].split(","))
  #return strArr

# keep this function call here 
print ArrayChallenge(raw_input())