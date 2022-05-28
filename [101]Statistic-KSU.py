import os
# os.system('cls')

def main():
    import time
    def clearList(x):
        x = []
    def makeListOfPrintAt(x): #Make a list of print >> paramenter == list[] >> list that you want to print
        n=0 #make line counter
        for i in range(1,len(x)+1): #print every element at that lost
            print(f'[{i}] {x[n]}')
            time.sleep(0.05)
            n+=1
        n=0 #reset line counter #
    def checkSelectionAtList(x): #Check inputed answer >> parameter == list[] >> to take length of that list
        while True:
            a = input('   Choose then press ENTER: ')
            try:
                a = int(a)
            except:
                continue
            if a in range(1, len(x)+1):
                break
        print('\n', end='')
        return a
    def printToFile(fileName, messageToPrint): # (file name == str'') , (messageToPrint == list[])
        def timingMessage(message, sleepTime): #sleep time = 0.1
            print(f'{message}', end='')
            time.sleep(sleepTime + 0.9)
            print('.', end='')
            time.sleep(sleepTime)
            print('.', end='')
            time.sleep(sleepTime)
            print('.')
            time.sleep(sleepTime)
        # -----head----- #
        f = open(f'{fileName}.txt', 'a+')
        # timingMessage('Please wait while proces', 0.1)    # >>optional<<
        # -----body-----#
        for i in messageToPrint:
            f.write(i)
            f.write('\n')
        f.write('='*100 + '\n')
        # -----close-----#
        f.close()
    def userAnswerIsNUM(Ques):
        while True:
            answer = input(Ques)
            try:
                answer = eval(answer)
                return answer
            except:
                continue


    #--------------------------------<<Chapter 1 Section>>--------------------------------#
    def ch1_main():
        rawDataCH1 = [] # main list of data before sort
        #how many items/elements
        while True:
            numOfData = input('How many elements you have in raw data: ')
            if numOfData > '0':
                try:
                    numOfData = int(numOfData)
                    break
                except:
                    continue
            else:
                continue
        #insert elements step > based on (how many items/elements)
        for i in range(1, numOfData+1):
            while True:
                ch1_element = input(f'add >>{i}<< element: ')
                try:
                    ch1_element = eval(ch1_element)
                    break
                except:
                    continue
            rawDataCH1.append(ch1_element)
        #-------------------re-order data
        rawDataCH1 = sorted(rawDataCH1)
        print(f'\nRaw Data: ', end='')
        for i in rawDataCH1:
            print(f'{i}, ', end='')
        print('\b\b\n',end='')


        #--------------------def section
        def ch1_mean(data):
            n = len(data)
            mean = sum(data) / n
            return mean
        def ch1_median(data):
            if len(data) % 2 == 0:
                xa = int( len(data) / 2 )
                xb = int( xa + 1 )
                median = (data[xa-1] + data[xb-1]) / 2
                return median
            else:
                xi = int((len(data)+1) / 2)
                return data[xi-1]
        def ch1_mode(data):
            # find mode(s)
            from collections import Counter
            c = Counter(data)
            modeList = [k for k, v in c.items() if v == c.most_common(1)[0][1]]

            if len(modeList) != len(data):
                #print mode(s)
                print('  mode[x̂]: ', end='')
                for i in modeList:
                    print(f'x̂={i}, ', end='')
                print('\b\b\n', end='')

            elif len(modeList) == len(data):
                print('  mode[x̂]: no mode')
        def ch1_Quartiles(r, data):

            n = len(data)

            # step 1:
            ch1_qr = (r * (n + 1)) / 4
            k = int(ch1_qr)
            s = ch1_qr - k

            # step 2:
            if s == 0 or s == 0.0:
                ch1_Qr = data[k - 1]
            else:
                ch1_Qr = data[k - 1] + s * (data[k] - data[k - 1])

            # step 3:
            return ch1_Qr
        def ch1_variance(data):
            n = len(data)
            mean = sum(data) / n
            deviations = [(x - mean) ** 2 for x in data]
            variance = sum(deviations) / n
            return variance
        def ch1_stdev(data):
            import math
            var = ch1_variance(data)
            std_dev = math.sqrt(var)
            return std_dev
        def ch1_CV(sd, mean):
            if mean == 0 or mean == 0.0:
                return '[NO CV, mean=0]'
            else:
                CV = sd/mean *100
                return CV
        def ch1_LF(Q1, Q3, Xs):
            LF = Q1 - 1.5*( Q3 - Q1 )
            if LF < Xs:
                return f'{LF}, No extrema from left'
            elif LF > Xs:
                return f"{LF}, There's extrema from left"
            elif LF == Xs:
                return f'{LF}, No extrema from left'
        def ch1_HF(Q1, Q3, Xl):
            HF = Q3 + 1.5 * (Q3 - Q1)
            if HF > Xl:
                return f'{HF}, No extrema from right'
            elif HF < Xl:
                return f"{HF}, There's extrema from right"
            elif HF == Xl:
                return f'{HF}, No extrema from right'


        #----------------------------------------------print section
        pMean = f'  mean[µ] = {(ch1_mean(rawDataCH1))}'
        pMedian = f'  median[x] = {(ch1_median(rawDataCH1))}'
        pVariance = f'  var(x)= {ch1_variance(rawDataCH1)}'
        pStandardDeviation = f'  standard deviation[s] = {ch1_stdev(rawDataCH1)}'
        pCV = '  CV = ' + "{:.2f}".format(ch1_CV(ch1_stdev(rawDataCH1), ch1_mean(rawDataCH1))) + '%'
        pQ1 = f'  Q{1}: {ch1_Quartiles(1, rawDataCH1)}'
        pQ2 = f'  Q{2}: {ch1_Quartiles(2, rawDataCH1)}'
        pQ3 = f'  Q{3}: {ch1_Quartiles(3, rawDataCH1)}'
        pLF = f'  LF = {ch1_LF( ch1_Quartiles(1, rawDataCH1) , ch1_Quartiles(3, rawDataCH1), rawDataCH1[0] )}'
        pHF = f'  HF = {ch1_HF( ch1_Quartiles(1, rawDataCH1) , ch1_Quartiles(3, rawDataCH1), rawDataCH1[-1])}'
        pFMessgae = '#>>note: if Q2 does not equal median then contact developer to solve this problem<<#'

        # -----Terminal print----- #
        pauseTimeBetweenLines = 0.1
        print(pMean)
        time.sleep(pauseTimeBetweenLines)
        print(pMedian)
        time.sleep(pauseTimeBetweenLines)
        ch1_mode(rawDataCH1)
        time.sleep(pauseTimeBetweenLines)
        print(pVariance)
        time.sleep(pauseTimeBetweenLines)
        print(pStandardDeviation)
        time.sleep(pauseTimeBetweenLines)
        print(pCV)
        time.sleep(pauseTimeBetweenLines)
        # Quartiles
        for i in range(1,4):
            print(f'  Q{i}: {ch1_Quartiles(i, rawDataCH1)}')
            time.sleep(pauseTimeBetweenLines)
        # HF and LF
        print(pLF)
        time.sleep(pauseTimeBetweenLines)
        print(pHF)
        time.sleep(pauseTimeBetweenLines)
        print(pFMessgae)
        time.sleep(pauseTimeBetweenLines)
        try:
            clearList(rawDataCH1)
        except:
            print('[ERROR while wipe list of data, restart projram]')
        print('<<---------------------------------Chapter 1 end--------------------------------->>\n')



        # -----TXT print----- #
        chapter1 = [f'Raw data: {rawDataCH1}', pMean, pMedian, pVariance, pStandardDeviation, pCV, pQ1, pQ2, pQ3, pLF, pHF, pFMessgae]

        try:
            printToFile('Chapter 1', chapter1)
        except:
            print('    [ERROR while printing result into .txt file]\n')

    #--------------------------------<<Chapter 2 Section>>--------------------------------#
    def ch2_0000():
        print('How many ways with replacement')
    # def ch2_0001():
    # def ch2_0100():
    # def ch2_0101():
    #--------------World List Chapter 2--------------#
    ch2_classA = ['How many ways...','What is the probability...']
    ch2_class00 = ['with replacement', 'without replacement']
    ch2_class01 = []
    #--------------------------------<<Chapter 3 Section>>--------------------------------#

    #--------------------------------<<Chapter 4 Section>>--------------------------------#
    def ch4_mainµ(): # µ without p >> Null Hypothesis
        import math

        #-----Input-----#
        mean = userAnswerIsNUM('mean =  ')
        segma = userAnswerIsNUM('Standard deviation = ')
        sampleSize = userAnswerIsNUM('Sample size(n) = ')
        levelOfSignificance = userAnswerIsNUM('Level of significance = ')
        µ0 = userAnswerIsNUM('µ0: ')
        makeListOfPrintAt(['More than', 'Less than', "Doesn't equal"])
        H1 = checkSelectionAtList(['More than', 'Less than', "Doesn't equal"])

        #-----Body-----#

        #z-Calcuated
        try:
            z0 = ( (mean - µ0) * math.sqrt(sampleSize) ) / (segma)
            z0 = eval(format(z0, '.3f'))
        except:
            z0 = True




        #z-Table  / ant format() function will return str not int
        if H1 == 1:
            z = format(1 - levelOfSignificance, '.4f')
            zTable = userAnswerIsNUM('Z-table for Z-' + z + '= ')
        elif H1 == 2:
            z = format(1 - levelOfSignificance, '.4f')
            zTable = userAnswerIsNUM('Z-table for Z-' + z + '= ')
        elif H1 == 3:
            zMax = format((1 - levelOfSignificance) / 2, '.4f') #str not int
            zMin = '-' + zMax #str not int
            zTableMax = userAnswerIsNUM(f'Z-table for Z-{zMax}= ')
            zTableMin = userAnswerIsNUM(f'Z-table for Z-{zMin}= ')
        else:
            print('Something got wrong with z-table')
            zTable = 0

        #Decision
        decision = ''
        if H1 == 1 and z0 != True:
            if z0 > zTable:
                decision = f"  We reject H0 at {levelOfSignificance} level of significance."
            else:
                decision = f"  We don't reject H0 at {levelOfSignificance} level of significance."
        elif H1 == 2 and z0 != True:
            if z0 < (-zTable):
                decision = f"  We reject H0 at {levelOfSignificance} level of significance."
            else:
                decision = f"  We don't reject H0 at {levelOfSignificance} level of significance."
        elif H1 == 3 and z0 != True:
            if zTableMin < z0 < zTableMax:
                decision = f"  We don't reject H0 at {levelOfSignificance} level of significance."
            else:
                decision = f"  We reject H0 at {levelOfSignificance} level of significance."
        elif z0 == True:
            decision = "  Projram can't reject or not reject based on 0 s.d"

        #-----Output-----#
        def calcH1(H1):
            if H1 == 1:
                return f'  H1: µ > {µ0}'
            elif H1 == 2:
                return f'  H1: µ < {µ0}'
            elif H1 == 3:
                return f'  H1: µ ≠ {µ0}'
        f_H0 = f'  H0: µ = {µ0}'
        f_H1 = calcH1(H1)
        if z0 == True:
            f_z0 = f'  z0 = **(Standard deviation = 0) so z0 Does not exist'
        else:
            f_z0 = f'  z0 = ({mean}-{µ0}) / ({segma}/{math.sqrt(sampleSize)}) = {z0}'

        chapter4 = [f_H0, f_H1, f_z0, decision]

        # -----Terminal Output-----#
        os.system('cls')
        print('#--------------------<< Result >>--------------------#')
        for i in chapter4:
            print(i)
            time.sleep(0.1)
        print('#-----------------<< end of result >>-----------------#')

        # -----TXT Output-----#
        printToFile('Chapter 4', chapter4)
        #reset
        z0 = False
    def ch4_mainP():
        print('[Sorry no data for while]')
    def ch4_nameOfSample():
        def checkSampleSize(x):
            if x > 30:
                return f"n = {x} > 30, it's normal distribution"
            elif x <= 30 and x > 0:
                return f"n = {x}, it's not normal distribution"
            elif x <= 0:
                return f"n is sample, if there's no sample so there's no name"
            else:
                return f"[{x} NOT defined]"
        n = userAnswerIsNUM('sample size(n) = ')
        nameOFsample = checkSampleSize(n)
        print(nameOFsample) #terminal print
        printToFile('Chapter 4', [f'Name of n= {n}', nameOFsample]) #txt print
    #--------------------------------<<Chapter 5 Section>>--------------------------------#


    #--------------Print Chapters--------------# #[not important]#
    chapterListNum = ['1', '2', '3', '4', '5']
    #print section
    for i in range(1,6):
        print(f'[{i}] Chapter {i}')
        time.sleep(0.1)

    #input section
    while True:
        chType = input('Press number to choose chapter then press ENTER:  ')
        if chType in chapterListNum:
            break

    #--------------Welcome List Generator--------------# #[not important]#
    welcomePhrase = []
    sideDashs = "-"*18
    for i in range(1,6):
        welcomePhrase.append(f'<<{sideDashs}Chapter {i}{sideDashs}>>')

    #--------------[main]--------------#
    if chType == '1':
        print(f'\n{welcomePhrase[0]}')
        ch1_main()
    elif chType == '2':
        print(f'\n{welcomePhrase[1]}')
        print('[NO DATA UNTIL NOW]')
        # #classA
        # makeListOfPrintAt(ch2_classA)
        # ch2_type_classA = checkSelectionAtList(ch2_classA)
        # #class00
        # if ch2_type_classA == 1:
        #     makeListOfPrintAt(ch2_class00)
        #     ch2_type_class00 = checkSelectionAtList(ch2_class00)
        # # class01
        # elif ch2_type_classA == 2:
        #     makeListOfPrintAt(ch2_class01)
        #     ch2_type_class01 = checkSelectionAtList(ch2_class01)
        print('<<---------------------------------Chapter 2 end--------------------------------->>\n')
    elif chType == '3':
        print(f'\n{welcomePhrase[2]}')
        print('[NO DATA UNTIL NOW]')
        print('<<---------------------------------Chapter 3 end--------------------------------->>\n')
    elif chType == '4':
        print(f'\n{welcomePhrase[3]}')
        makeListOfPrintAt(['µ >> Hypothesis Test', 'P >> Hypothesis Test', 'Name of sample'])
        ch4_type = checkSelectionAtList(['µ >> Hypothesis Test', 'P >> Hypothesis Test', 'Name of sample'])
        if ch4_type == 1:
            ch4_mainµ()
        elif ch4_type == 2:
            print('[NO DATA UNTIL NOW]')
            # ch4_mainP()
        elif ch4_type == 3:
            ch4_nameOfSample()
        print('<<---------------------------------Chapter 4 end--------------------------------->>\n')
    elif chType == '5':
        print(f'\n{welcomePhrase[4]}')
        print('[NO DATA UNTIL NOW]')
        print('<<---------------------------------Chapter 5 end--------------------------------->>\n')

# start here
print('# Based on Statistic subject at King Saud Universiy >> [101stat]')
print('# Coded by Ammar - Common First Year at KSU')
print('# please check this source code through github.com/ammarKSU/stat101\n')

while True:
    main()

