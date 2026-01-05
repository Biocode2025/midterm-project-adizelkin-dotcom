file=open("data/AA_weights.txt","r")
file2=open("data/Bsub_proteins.fasta","r")
method=int(input("How would you like to calculate the protein Mass: Monoisotopic - 1 or Average - 2?"))
#מחלקת לשני מילונים 
monoisotopic={}
average={}
next(file)
for line in file:
  parts = line.split()
  code = parts[-3]                
  monoisotopic[code] = float(parts[-2])
  average[code] = float(parts[-1])
    
weights =[]  
names=[] 
place=0-1
#monoisotopic מחשב את המשקל של כל חלבון לפי 
if (method==1):
  fileW=open("Bsub_MW_Monoisotopic.txt","w")
  for line in file2:
    line = line.strip()
    if line.startswith(">"):
      place+=1
      weights.append(0)
      names.append("")
      names[place]=line
    else:
      for i in range (len(line)):
        weights [place]+=monoisotopic[line[i]]


#average מחשב את המשקל של כל חלבון
if (method==2):
  fileW=open("Bsub_MW_Average.txt","w")
  for line in file2:
    line = line.strip()
    if line.startswith(">"):
      place+=1
      weights.append(0)
      names.append("")
      names[place]=line
    else:
      for i in range (len(line)):
        weights[place]+=average[line[i]]

sum=0
heviest=lightest=0
#מדפיס את המשקל,מחשב ומדפיס ממוצה,את הכבד והקל ביותר
for i in range (len(weights)):
  fileW.write(str(names[i]))
  fileW.write("\n")
  fileW.write(str(weights[i]))
  fileW.write("\n") 
  sum+=weights [i]
  if(weights[heviest]<weights [i]):
    heviest=i
  if(weights[lightest] > weights[i]):
    lightest =i
print("the average wight for protein is:",sum/len(weights))
print("the heviest protein is:",names[heviest])
print(weights[heviest])
print("the lightest  protein is:",names[lightest])
print(weights[lightest])




file.close()
file2.close()
fileW.close()