import sys, random, math

fileName =  ["   set v 3","     set x 1","asfasf   ymove 2  #note","    add x 1"," if x < 3 asfasf","      xmove 5","   printloc"]
fileLines = []
xPosition = 0
yPosition = 0
lineCounter = 0
programLine = 0
variableChecker = 0
totalLines = 9
goToCommandTrue = 0
linesWithLabels = []
commandLines = ["ymove","xmove",'printloc','if','goto','set','add','sub','halt']
commandLineCounter = 0
lineList = []
foundLabel = 0
labelLine = {}
dictWithLabels = {}
dictOfVariables = {}
xyVariableChecker = 0
for fileLine in fileName:
    lineCounter = lineCounter +1
    fileLine = fileLine.lower()
    fileLines.append(fileLine.split())
while programLine < lineCounter:
    while commandLineCounter < 9:
        if fileLines[programLine][0] == commandLines[commandLineCounter]:  
            lineList.append(programLine)
            labelLine[programLine] = False
            break
        commandLineCounter = commandLineCounter +1
        if(commandLineCounter == 9):
            linesWithLabels.append(programLine)
            labelLine[programLine] = True
            dictWithLabels[fileLines[programLine][0]] = programLine
    programLine = programLine +1
    commandLineCounter = 0
totalLines = programLine
lineCounter = 0
print(fileLines)
while(lineCounter < totalLines):
    commandString = 0
    
    if(labelLine[lineCounter] == True):
       commandString = 1;
   
   
    if (fileLines[lineCounter][commandString] == 'ymove'):
        try:                     
           yPosition = yPosition + int(fileLines[lineCounter][commandString+1])
        except:    
              yPosition = yPosition + int(dictOfVariables[fileLines[lineCounter][commandString+1]])
              
        if(yPosition < 0 or yPosition > 32):
            print("You are off the table x position: ",xPosition, " y position: ", yPosition )
            exit()
        xyVariableChecker = 0

    if (fileLines[lineCounter][commandString] == 'xmove'):
        print(fileLines[lineCounter][commandString+1])
        for subVal in dictOfVariables:
            if fileLines[lineCounter][commandString+1] in subVal:
                xPosition = int(dictOfVariables[fileLines[lineCounter][commandString+1]])
                xyVariableChecker = 1
        if(xyVariableChecker == 0):
            xPosition = xPosition + int(fileLines[lineCounter][commandString+1])
        if(xPosition < 0 or xPosition > 32):
            print("You are off the table x position: ",xPosition, " y position: ", yPosition )
            exit()
        xyVariableChecker = 0

    if (fileLines[lineCounter][commandString] == 'add'):
        for subVal in dictOfVariables:
            if fileLines[lineCounter][commandString+1] in subVal:
                dictOfVariables[fileLines[lineCounter][commandString+1]] = int(fileLines[lineCounter][commandString+2]) + int(dictOfVariables[fileLines[lineCounter][commandString+1]])
                xCounter = int(fileLines[lineCounter][commandString+2]) + int(dictOfVariables[fileLines[lineCounter][commandString+1]])
        print(dictOfVariables)    

    if (fileLines[lineCounter][commandString] == 'printloc'):
        print("printloc ", "x = ", xPosition, " y = ", yPosition)

    if (fileLines[lineCounter][commandString] == 'if'):
        if(fileLines[lineCounter][commandString+2] == '<'):
                      
            try:
                firstNumber = int(dictOfVariables.get(fileLines[lineCounter][commandString+1]))

            except:
                firstNumber = int(fileLines[lineCounter][commandString+1])
            
            try:
                secondNumber = int(dictOfVariables.get(fileLines[lineCounter][commandString+3]))
            except:
                secondNumber = int(fileLines[lineCounter][commandString+3])

            if(firstNumber < secondNumber):
                lineCounter = int(dictWithLabels[fileLines[lineCounter][commandString+4]])
                goToCommandTrue = 1
            
        if(fileLines[lineCounter][commandString+2] == '>'):
            try:
                firstNumber = int(dictOfVariables.get(fileLines[lineCounter][commandString+1]))

            except:
                firstNumber = int(fileLines[lineCounter][commandString+1])
            
            try:
                secondNumber = int(dictOfVariables.get(fileLines[lineCounter][commandString+3]))
            except:
                secondNumber = int(fileLines[lineCounter][commandString+3])

            if(firstNumber > secondNumber):
                lineCounter = int(dictWithLabels[fileLines[lineCounter][commandString+4]])
                goToCommandTrue = 1

        if(fileLines[lineCounter][commandString+2] == '=='):
            try:
                firstNumber = int(dictOfVariables.get(fileLines[lineCounter][commandString+1]))
            except:
                firstNumber = int(fileLines[lineCounter][commandString+1])
            try:
                secondNumber = int(dictOfVariables.get(fileLines[lineCounter][commandString+3]))
            except:
                secondNumber = int(fileLines[lineCounter][commandString+3])

            if(firstNumber == secondNumber):
                lineCounter = int(dictWithLabels[fileLines[lineCounter][commandString+4]])
                goToCommandTrue = 1
        if(fileLines[lineCounter][commandString+2] == '!='):
            try:
                firstNumber = int(dictOfVariables.get(fileLines[lineCounter][commandString+1]))

            except:
                firstNumber = int(fileLines[lineCounter][commandString+1])
            
            try:
                secondNumber = int(dictOfVariables.get(fileLines[lineCounter][commandString+3]))
            except:
                secondNumber = int(fileLines[lineCounter][commandString+3])

            if(firstNumber != secondNumber):
                lineCounter = int(dictWithLabels[fileLines[lineCounter][commandString+4]])
                goToCommandTrue = 1

    if (fileLines[lineCounter][commandString] == 'goto'):
        for subVal in dictWithLabels:
            if fileLines[lineCounter][commandString+1] in subVal:
                lineCounter = int(dictWithLabels[fileLines[lineCounter][commandString+1]])
                goToCommandTrue = 1;
                
    if (fileLines[lineCounter][commandString] == 'set'):
        ##print("this should be the variable")
        dictOfVariables[fileLines[lineCounter][commandString+1]] = int(fileLines[lineCounter][commandString+2])
        ##print(dictOfVariables)
    

    if (fileLines[lineCounter][commandString] == 'sub'):
        for subVal in dictOfVariables:
            if fileLines[lineCounter][commandString+1] in subVal:
                dictOfVariables[fileLines[lineCounter][commandString+1]] = int(dictOfVariables[fileLines[lineCounter][commandString+1]]) - int(fileLines[lineCounter][commandString+2])  
      

    if (fileLines[lineCounter][commandString] == 'halt'):
        exit()

    commandString = 0
    if(goToCommandTrue != 1):
       lineCounter = lineCounter+1
    goToCommandTrue = 0
exit()


