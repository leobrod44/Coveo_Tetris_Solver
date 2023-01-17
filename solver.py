from game_interface import Answer, GameMessage, TotemAnswer
from typing import List, Literal, Tuple

class Solver:
    def init(self):

        pass
    def get_answer(self, game_message: GameMessage) -> Answer:

        total_totem = [0, 0, 0, 0, 0, 0, 0]
        totems = []
        usedPositions = []
        finaltotems = []
        questionTotems = []
        question = game_message.payload
        for i in range(len(question.totems)):
            questionTotems.append(question.totems[i].shape)

        print(*questionTotems, sep = ", ")
        iLetter = [(0,0), (1,0), (2,0), (3,0)]
        jLetter = [(0,0),(1,0), (2,0), (2,1)]
        lLetter = [(0,1),(0,0), (1,0), (2,0)]
        tLetter = [(0,0), (1,0), (1,1), (2,0)]
        sLetter = [(0,0), (1,0), (1,1), (2,1)]
        zLetter = [(0,1), (1,1), (1,0), (2,0)]
        oLetter = [(0, 0), (0, 1), (1, 0), (1, 1)]
        for i in range(len(questionTotems)):
            if questionTotems[i] == "L":
                total_totem[0] += 1
                totems.append(lLetter)
            elif questionTotems[i] == "J":
                total_totem[1] += 1
                totems.append( jLetter)
            elif questionTotems[i] == "I":
                total_totem[2] += 1
                totems.append(iLetter)
            elif questionTotems[i] == "T":
                total_totem[3] += 1
                totems.append(tLetter)
            elif questionTotems[i] == "S":
                total_totem[4] += 1
                totems.append(sLetter)
            elif questionTotems[i] == "Z":
                total_totem[5] += 1
                totems.append(zLetter)
            else:
                total_totem[6] += 1
                totems.append(oLetter)
        print(total_totem)
        print(*totems, sep=", ")
        currentTotem = totems[0]
        currentList = []
        print(*currentTotem, sep=", ")
        totemnum = 0
        found = False
        for t in range(len(questionTotems)):
            found = False
            currentTotem = totems[t]
            print(totems[t])
            for n in range(100):
                if found == True:
                    break
                print("n entered",n)
                for m in range(100):
                    if found == True:
                        break
                    print("m entered", m)
                    for i in range(len(currentTotem)):
                        alreadyThere = False
                        temptot = (currentTotem[i][0]+n, currentTotem[i][1]+m)
                        currentList.append(temptot)
                        for k in range(len(usedPositions)):
                            if temptot[0]==usedPositions[k][0] and temptot[1]==usedPositions[k][1]:
                                currentList=[]
                                alreadyThere= True
                                break
                        if alreadyThere==True:
                            break
                        if i==3:
                            usedPositions.extend(currentList)
                            finaltotems.append(TotemAnswer(questionTotems[t], coordinates=currentList))
                            totemnum+=1
                            found = True
                            print(*finaltotems, sep = ", ")

                    currentList = []
                    if found == True:
                        break
        answer = Answer(finaltotems)
        print("Sending Answer:", answer)
        return answer