def GraphChallenge(strArr):
  
  src= strArr[1]
  NofNodes= int(strArr[0])
  des= strArr[NofNodes]
  paths= []
  for i in range(NofNodes+1 , len(strArr)): 
    rel= strArr[i].split("-")
    if rel[0]==src:
        paths.append(rel) 
  for k in range (0,len(paths)):
    if paths[k][len(paths[k])-1] == des:
      count=0
      continue;
    else:
      for i in range (NofNodes+1,len(strArr)):
        rel=strArr[i].split("-")
        if rel[0]==paths[k][len(paths[k])-1]:
          paths[k].append(rel[1])
   # sort paths
  for i in range(0, len(paths)-1):
    for j in range(0,len(paths)-i-1):
      if len(paths[j]) >len(paths[j+1]):
        paths[j],paths[j+1]=paths[j+1],paths[j]
        
        
      
  #output
  return ("-".join(paths[0]))  
   


# keep this function call here 
print GraphChallenge(raw_input())