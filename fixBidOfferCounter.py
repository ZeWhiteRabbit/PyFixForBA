import os

path = 'ENTER FILE PATH'

bidAndOffer = 0
onlyBid = 0
onlyOffer = 0
exceptions = 0
lineCount = 0
mdMessageCounter = 0

filelist = os.listdir(path)
for file in filelist:
    exeptionList = []
    if file.endswith('.log'):
        with open(path + file, 'r') as log:
            for line in log:
                line = line.split('')
                lineCount = lineCount + 1
                if '35=W' in line:
                    mdMessageCounter = mdMessageCounter + 1
                    exception = True
                    if '269=0' in line and '269=1' in line:
                        bidAndOffer = bidAndOffer + 1
                        exception = False
                        #print('\n','[BIDS&OFFERS]:',line)
                    if '269=0' not in line and '269=1' in line:
                        onlyOffer = onlyOffer + 1
                        exception = False
                        #print('\n','[BIDS]:', line)
                    if '269=1' not in line and '269=0' in line:
                        onlyBid = onlyBid + 1
                        exception = False
                        #print('\n','[OFFERS]:',line)
                    if exception:
                        exception = exception + 1
                        exeptionList.append(line)
                        #print('\n','[DEBUG]','[EXEPTIONS]:',line)

        print('\n','[FILE]:', file)
        print(' [RESULTS]:')
        # print(' # of messages containing 35=W:', mdMessageCounter)
        print(' # of messages containing ONLY Bids:', onlyBid)
        print(' # of messages containing ONLY Offers:', onlyOffer)
        print(' # of messages containing BOTH Bids and Offers:', bidAndOffer)
        # print(' # of messages containing EXEPTION:', exeption)
        # print('\n',' [EXEPTIONS]:','\n',*exeptionList, sep='\n')
