userInput=input("Entere your message that you want to save : ")
#with open('data.txt','w') as file:
    #file.write(userInput)

with open('data.txt','a') as file:
    file.write(userInput +'/n')