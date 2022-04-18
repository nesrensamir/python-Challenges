def StringChallenge(strParam):

  # code goes here
  errorArr=[]
  divIndex = [index for index in range(len(strParam)) if strParam.startswith('div>',index)]
  pIndex=[index for index in range(len(strParam)) if strParam.startswith('p>',index)]
  iIndex= [index for index in range(len(strParam)) if strParam.startswith('i>',index)]
  emIndex=[index for index in range(len(strParam)) if strParam.startswith('em>',index)]
  bIndex= [index for index in range(len(strParam)) if strParam.startswith('b>', index)]
  

  elemIndex=[divIndex,pIndex,iIndex,emIndex,bIndex]

  for i in range(0,5):
    if len(elemIndex[i])%2:
      errorArr.append(i) 
    
  for i in range (0,len(errorArr)):
    for j in range (0,len(errorArr)-1):
      if elemIndex[errorArr[j]][0]>elemIndex[errorArr[j]][0]:
        errorArr[j],errorArr[j+1]=errorArr[j+1],errorArr[j] 
 
  switcher = {
    0: 'div',
    1: 'p',
    2: 'i',
    3: 'em',
    4: 'b'
  }
  return switcher.get(errorArr[0] , 'nested correctly')
       

  

# keep this function call here 
print StringChallenge(raw_input())