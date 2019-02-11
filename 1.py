listS=[]
while True:
  subject=input("What subjects do you have:(Enter 0 to finish)\n")
  if subject == "0":
    break
  listS.append(subject)

for z in range(len(listS)):
  print(str(z+1)+"."+listS[z])


AskS=input("What's your favourite subject\n")

AskC=input("What's your most challenging subject\n")


ze = listS[int(a)-1]

print("Your favourite subject is", ze)
print("Your most challenging subject", ze)
