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

print("Your favourite subject is", listS[int(AskS)-1])
print("Your most challenging subject", listS[int(AskC)-1]))
