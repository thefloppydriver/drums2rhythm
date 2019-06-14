from shutil import copy2

global finalstring
global beforetherhythm
global aftertherhythm
global songerror
global therhythmisdone
global startHere
global oof
global woof
global doof
global poof

copy2('notes.chart', 'notes.chartbackup')

oof = False
woof = False
with open('notes.chart', 'r') as f:
    while oof == False:
        try:
            if '[ExpertDrums]' in next(f):
                ##print('Found the drums!!')
                oof = True
                poof = True
        except StopIteration:
            print('NO DRUMS')
            exit()
            break
        
with open('notes.chart', 'r') as f:
    while woof == False:
        try:
            if '[ExpertDoubleRhythm]' in next(f):
                ##print('Found the rhythm!!')
                oof = True
        except StopIteration:
            ##print('NO RHYTHM')
            woof=True

with open('notes.chart', 'r') as f:
    while not '[ExpertDrums]' in next(f):
        pass
    while not '{' in next(f):
        pass
    ##print("[ExpertDoubleRhythm]")
    finalstring = "[ExpertDoubleRhythm]" + '\n'
    ##print('{')
    finalstring = finalstring + '{' + '\n'
    for line in f:
        #line will be now the next line after the one that contains '[ExpertDrums] /n {'
        if '}' in line:
            ##print('}')
            ##finalstring = finalstring + "}" + '\n'
            break
        
        if "E" not in line:
            timestamp, equal, SorN, note, starpowerlength = line.split()

            if note != "0":
                newnote=str(int(note) - 1)
            if note == "0":
                newnote="4"
            
            newline = timestamp+" "+equal+" "+SorN+" "+newnote+" "+starpowerlength
            ##print("  "+newline)
            finalstring = finalstring + "  " + newline + '\n'

        if "E" in line:
            ##print("  "+line.strip())
            finalstring = finalstring + "  " + line.strip() + '\n'
        
##finalstring = finalstring + "" + '\n'
##        if '}' in next(f):
##            break

##input("press enter to print FINALSTRING")
##   print(finalstring)

##with open("placeholder_newfile.chart", "w") as text_file:
##    print(finalstring, file=text_file)







songerror=False
beforetherhythm = '[Song]' + '\n'
aftertherhythm = '\n'
therhythmisdone=False
therhythmhasstarted=False
startHere=False
doof=False
poof=False
with open('notes.chart', 'r') as f:
    ##while not '[ExpertDoubleRhythm]' in next(f):
    ##    beforetherhythm = beforetherhythm + line
    for line in f:
        if songerror==True:
            if '[ExpertDoubleRhythm]' in line or '[ExpertKeyboard]' in line or '[ExpertDrums]' in line:
                break
            beforetherhythm = beforetherhythm + line
        if songerror==False:
            songerror=True
        
    ##while not '}' in next(f):
    ##    aftertherhythm = aftertherhythm + line

with open('notes.chart', 'r') as f:
    for line in f:
        if woof == False:
            if '[ExpertDoubleRhythm]' in line: # and startHere==False:
                therhythmhasstarted=True
        if doof == False:
            if woof == True:
                #print('woof is True')
                if '[ExpertKeyboard]' in line:
                    print('[ExpertKeyboard] Found!!')
                    therhythmisdone = True
                    doof = True
        if poof == False:
            if woof == True:
                if '[ExpertDrums]' in line:
                    print('[ExpertDrums] Found!!')
                    therhythmisdone = True
                    poof = True
        #if '[ExpertKeyboard]' in line and therhythmhasstarted==False:
        #    startHere=True
        if therhythmhasstarted==True:
            if '}' in line:
                therhythmisdone=True
                therhythmhasstarted=False
        if therhythmisdone == True: # or startHere == True:
            #startHere=False
            aftertherhythm = aftertherhythm + line
            
        
##print(beforetherhythm)
##print(finalstring)
##print(aftertherhythm)
   
with open("notes.chart", "w") as text_file:
    print(beforetherhythm+finalstring+'}'+aftertherhythm, file=text_file)
##print(beforetherhythm+'before')
##print(finalstring+'during')
##print(aftertherhythm+'after')
