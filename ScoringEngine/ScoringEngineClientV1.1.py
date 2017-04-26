
import socket
import getpass
import time
from datetime import datetime
import math
import requests
import hashlib

#======================GLOBAL VARIABLES=======================

# region ENUMERATED CHALLENGE TYPES
# Writen as 'CT_<Challenge name/type>
CT_PORT_CLOSE = 0
CT_PORT_OPEN = 0
CT_DELETE_MALWARE = 0
CT_FIND_FILE = 0
CT_REMOVE_BLOATWARE = 0
CT_ = 0
CT_ = 0
CT_ = 0
CT_ = 0
CT_ = 0
CT_ = 0
CT_ = 0
CT_ = 0
CT_ = 0
CT_ = 0
CT_ = 0
CT_ = 0
CT_ = 0
CT_ = 0
CT_ = 0


# endregion

evaluationInterval = 10 # Time, in seconds, between evaluations periods.

#scoringEngineConfigFile = "C:\\Users\\DevClientAdmin\\Documents\\GitHub\\ChallengeScoringEngine\\ScoringEngine\\ScoringEngineConfig v0.01.txt"
scoringEngineConfigFile = "ScoringEngineConfig v0.01.txt"

hashChunkSize = int(1024 * 8 * 8)


#=========================FUNCTIONS===========================

##Function Template
"""
##
def ():
    pass
"""

#=============================================================
#===================== General Functions =====================
#=============================================================
# region General Functions

def findIndexOfAllOccurancesInString(mainString, occureStr):
    return list(filter((lambda x: x is not -1), (map((lambda x: x if mainString[x] is occureStr else -1), range(len(mainString))))))



# endregion
#=============================================================
#================ System Operation Functions =================
#=============================================================
# region System Operation Functions

##
def getLoggedInUsername():
    return getpass.getuser()

## Returns a list of all user accounts on the system
def getAllUserAccounts():
    pass

## Returns a list of all inactive user accounts on the system
def getInactiveUserAccounts():
    pass

##
def enablePersistence():
    pass

##
def disablePersistence():
    pass

##
def checkPersistence():
    pass

##
def readConfigValue(filePath, settingName, sep=None):
    if filePath is not '' and filePath is not None and settingName is not '' and settingName is not None:
        with open(filePath, 'r') as file:
            lines = file.readlines()
            configLine = list(filter(lambda line: settingName in line, lines))[0].replace('\n', '')
            if sep is None:
                if configLine.count('='):
                    parsedValue = configLine.split("=")[1]
                else:
                    parsedValue = configLine.partition(settingName)[2]
            else:
                parsedValue = configLine.partition(sep)[2]

            parsedValue = parsedValue.replace('\t', '')
            parsedValue = parsedValue.replace(' ', '')
            return parsedValue
    else:
        return 0

#readConfigValue("C:\\Program Files (x86)\\JetBrains\\PyCharm Community Edition 2016.3.3\\bin\\idea.properties", "idea.max.content.load.filesize")
#readConfigValue("C:\\Users\\DevClientAdmin\\Desktop\\testConfig.txt", "idea.max.content.load.filesize", '=')

##
def validateConfigValue(filePath, settingName, settingValue, sep=None):
    curValue = readConfigValue(filePath, settingName, sep)
    return True if curValue == str(settingValue) else False

#print(validateConfigValue("C:\\Users\\DevClientAdmin\\Desktop\\testConfig.txt", "idea.max.content.load.filesize", 20000, '='))

##
def setConfigValue(filePath, settingName, settingValue, sep=None):
    try:
        settingValue = str(settingValue)
        curValue = readConfigValue(filePath, settingName, sep)
        if readConfigValue(filePath, settingName, sep) == settingValue:
            return True
        else:
            lines = []
            with open(filePath, 'r') as file:
                lines = file.readlines()
                localIndex = list(filter(lambda x: settingName in lines[x], range(len(lines))))[0]
                newConfigValue = lines[localIndex].split(settingName)[1].replace(curValue, settingValue)
                newConfigLine = settingName + newConfigValue
                lines[localIndex] = newConfigLine
            with open(filePath, 'w') as file:
                file.writelines(lines)
            return True
    except Exception as e:
        print("Error: While setting config {} to {} in file {}, the following exception was thrown:\n\n{}\n\n".format(settingName, settingValue, filePath, e))
        return False

print(setConfigValue("testConfig.txt", "idea.max.content.load.filesize", 10000, '='))

# endregion
#=============================================================
#==================== Network Functions ======================
#=============================================================
# region Network Functions

##
def sendPacket():
    pass

##
def sendACK():
    pass

##
def sendSYN():
    pass

##
def encryptData():
    pass

##
def establishConnection():
    pass

##
def initializeChallengeDataTransfer():
    pass

##
def endChallengeDataTransfer():
    pass

##
def sendFormattedChallengeData():
    pass

##
def uploadFile():
    pass

##
def downloadFile():
    pass

# endregion
#=============================================================
#================ Challenge Control Functions ================
#=============================================================
# region Challenge Control Functions

## Adds the given challenge entry data to the appropriate challenge list to be checked on the evaluation cycle
def addChallenge():
    pass

## Permanently removes the challenge on the given name and type
def removeChallenge():
    pass

## Enables a challenge of the given name and type
def enableChallenge():
    pass

## Disables a challenge of the given name and type
def disableChallenge():
    pass

## Loads challenges from a properly formatted file with the given file name
def loadChallengesFromFile():
    pass

# endregion
#=============================================================
#============== Port Check and Control Functions =============
#=============================================================
# region Port Check and Control Functions

## Scans and reports all open ports on the machine, using nmap, returning an iterable list of open ports
def checkPorts():
    pass

# endregion
#=============================================================
#================ Service Monitoring Functions ===============
#=============================================================
# region Service Monitoring Functions

## Includes a supported service in the list of services hosted by this box
def includeService():
    pass

##
def removeService():
    pass

##
def checkServices():
    pass

##
def addServicePort():
    pass

##
def removeServicePort():
    pass

##
def checkServicePorts():
    pass

# endregion
#=============================================================
#============== Malware File Existence Functions =============
#=============================================================
# region Malware File Existence Functions

## Checks if all enabled file challenges still exist, returning a list of the file challenge names, who's
## designated file does not exist.
def validateFileExistence():
    pass

## Checks if a single file at the provided path exists, and if so returns true, otherwise returns false
def checkFileExistence(filePath):
    pass

# endregion
#=============================================================
#================= Windows Setting Functions =================
#=============================================================
# region Windows Setting Check and Control Functions

## Runs appropriate validation of all enabled Windows Setting Challenges, and returns a list of challenge
## names which do not validate
def validateWindowsSettings():
    pass

## Runs appropriate validation against the provided Windows Setting Challenge name
def checkWindowsSetting():
    pass

# endregion
#=============================================================
#================= Scheduled Task Functions ==================
#=============================================================
# region Scheduled Task Check and Control Functions

## Checks if each Scheduled Task Challenge is Enabled, Disabled, or Deleted, and returns a list of Challenge
## Names which are either Disabled or Deleted, along with the Challenge Name, formated like such:
## [(Name1, Status1), (Name2, Status2),...]
def validateTaskStatuses():
    pass

## Checks if a task of the given name is a valid name, and if so, whether that task is Enabled, Disabled, or
## Deleted, returning the status or -1 if the given name is invalid.
def checkTaskStatus():
    pass

# endregion
#=============================================================
#================== Major Malware Functions ==================
#=============================================================
# region Major Malware Check and Control Functions

## Validates that all copies of LittleBoy still exist, but if not, throws an exception(Type needs to be determined)
def validateLittleboy():
    pass

## Validates that all copies of H-Bomb still exist, but if not, throws an exception(Type needs to be determined)
def validateHBomb():
    pass

## Uses provided functions to validate the existance of all Backdoor Challenges
def countBackdoors():
    pass

# endregion
#=============================================================
#===================== Challenge Classes =====================
#=============================================================

class challengeBase:
    def __init__(self, ID=None, basePointValue=None, bContinuous=False, continuousPointInterval=evaluationInterval, parentChallengeList=[]):
        self.parentChallengeList        = parentChallengeList
        self.challengeID                = ID
        self.challengePointValue        = 0 # Point value sent to scoring server. Calculated based on time for continuous challenges, otherwise a flat value if non-continuous.
        self.basePointValue             = basePointValue # Point value used to calculate final challenge point value. Added as a flat value for non-continuous challenges
        self.bCompleted                 = False
        self.bContinuous                = bContinuous
        self.continuousPointInterval    = continuousPointInterval # Time interval, in milliseconds, upon which challenge point value is based.
        self.evaluate                   = self._evaluationFunc_

        self._intervalStartTime         = None

    def _evaluationFunc_(self):
        return True

    def _completeChallenge_(self):
        if not self.bCompleted:
            if not self.bContinuous:
                self.challengePointValue = self.basePointValue
                self.bCompleted = True
            else:
                self.bCompleted = True
                self._intervalStartTime = time.time()

    def _newInterval_(self):
        newIntervalStartTime = time.time()
        timeInterval = newIntervalStartTime - self._intervalStartTime
        self.challengePointValue += timeInterval / self.continuousPointInterval * self.basePointValue
        self._intervalStartTime = newIntervalStartTime

    def _printData_(self):
        print("Challenge ID: {}\nChallenge Point Value: {}\nBase Point Value: {}\nCompleted?: {}\nContinuous?: {}\nContinuous Point Interval: {} sec\n".format(
            self.challengeID,
            self.challengePointValue,
            self.basePointValue,
            self.bCompleted,
            self.bContinuous,
            self.continuousPointInterval
        ))

    def evaluateChallenge(self):
        if self.evaluate():
            if not self.bCompleted:
                self._completeChallenge_()
            elif self.bContinuous:
                self._newInterval_()
            return True
        else:
            if self.bCompleted:
                self.bCompleted = False
                self.intervalStartTime = None
            return False

class httpChallengeL2(challengeBase):
    def __init__(self, IP=None, URL=None ,port=80, ID=None, basePointValue=None, bContinuous=False, continuousPointInterval=evaluationInterval, parentChallengeList=[]):
        challengeBase.__init__(self, ID, basePointValue, bContinuous, continuousPointInterval, parentChallengeList)
        self.evaluate           = self.evaluateHTTP
        self.IP                 = IP
        self.URL                = URL
        self.port               = port
        self.newWebHash         = None

        if IP is None:
            if URL is None:
                print("Error: and IP or URL must be given for challenge with ID: {}".format(ID))
        else:
            if URL is None:
                self.URL = "http://{}".format(self.IP)
                #self.URL = self.IP

        response = requests.get(self.URL, stream=True)
        self.originalWebHash    = self.hashRawWebResponse(response)
        self.originalBannerHash = self.hashBannerGrab(response)

    ##
    def evaluateHTTP(self):
        response = requests.get(self.URL, stream=True)
        #print("Original Hash: {}\nNew Hash: {}\n".format(self.originalHash, self.newHash))
        return self.evaluateRawWebResponse(response)

    ##
    def evaluateBannerGrab(self, response):
        pass
    """
    def grabBanner(self):
        response = requests.get(self.URL, stream=True)
        print(response.headers)



        try:
            s = socket.socket()
            s.connect((self.URL.replace("http://", ""), self.port))
            #httpGet = 'GET / HTTP/1.1\nHost: {}\n\n'.format(self.URL.replace("http://", "")).encode('utf-8')
            httpGet = b'HEAD / HTTP/1.1\n\n'
            #print("Http Get: %s" % httpGet)
            s.sendall(httpGet)
            banner = s.recv(1024)

        except Exception as e:
            print(e)
            return None
        finally:
            s.close()

        return banner
        """
    ##
    def hashBannerGrab(self, response):
        banner = response.headers
        bannerData = ''
        bannerKeys = ["Server", "Content-Type"]

        for key in bannerKeys:
            if banner.__contains__(key):
                bannerData += key + banner[key]

        h = hashlib.sha1()
        h.update(bannerData.encode("utf-8"))

        #print("BannnerData: {}\nHex Digest: {}\n".format(bannerData, h.hexdigest()))
        return h.hexdigest()

        """
        print(banner.keys())
        if banner.__contains__("Date"):
            banner.pop("Date")
        if banner.__contains__("Set-Cookie"):
            banner.pop("Set-Cookie")
        if banner.__contains__("Last-Modified"):
            banner.pop("Last-Modified")
        if banner.__contains__("X-Deity"):
            banner.pop("X-Deity")

        print(banner.keys())
        #banner.pop("")


        allData = ''
        for val in banner:
            bannerData += val + banner[val]
        banner = allData.encode("utf-8")
        print(banner)
        h = hashlib.sha1()
        h.update(banner)

        #print(h.hexdigest())
        print("Bannner: {}\nHex Digest: {}\n".format(banner, h.hexdigest()))
        return h.hexdigest()
        """

    ##
    def evaluateRawWebResponse(self, response):
        self.newWebHash = self.hashRawWebResponse(response)
        return True if self.newWebHash == self.originalWebHash else False

    ##
    def hashRawWebResponse(self, response, chunkSize=16):
        h = hashlib.sha1()
        chunk = ''
        chunk = chunk.zfill(chunkSize)

        while len(chunk) == chunkSize:
            chunk = response.raw.read(chunkSize)
            h.update(chunk)

        return h.hexdigest()


#=============================================================
#====================== Main Functions =======================
#=============================================================

challengeServices = []

## Runs each validation function and performs any needed parsing or validation of returned data.
def runEvaluationCycle():
    completedChallenges = list(filter((lambda x: x.evaluateChallenge()), challengeServices))


## Run after the evaluation cycle. Pools all valuable data or changes and formats them for transmission back to the server
def organizeDataForTransit():
    pass

def run():




    challengeServices.clear()
    print("start time1: {}\n".format(datetime.now()))

    #challengeServices.append(httpChallengeL2(URL="http://www.google.com", basePointValue=3000, ID=0, bContinuous=True, continuousPointInterval=100))
    challengeServices.append(httpChallengeL2(URL="http://requests.readthedocs.io", basePointValue=3000, ID=0, bContinuous=True,
                                             continuousPointInterval=100))
    testBase = challengeServices[0]
    runEvaluationCycle()
    numCycles = 30
    sleepTime = .1

    startTime = time.time()
    for i in range(numCycles):
        time.sleep(sleepTime)
        runEvaluationCycle()
        #testBase._printData_()
    endTime = time.time()


    estimatedRunTime = numCycles * sleepTime
    trueRunTime = endTime - startTime
    totalExtraTime = trueRunTime - estimatedRunTime
    extraTimePerCycle = totalExtraTime / numCycles * 1000000
    pointsPerCycle = testBase.challengePointValue / numCycles
    estimatedPointGain = testBase.basePointValue / testBase.continuousPointInterval * numCycles * sleepTime
    estimatedPointsPerSecond = testBase.basePointValue / testBase.continuousPointInterval
    #extraTimePerCycle = (testBase.challengePointValue - estimatedPointGain) / numCycles * 1000000

    printData = "\nCompletion Date: {}\n\n# Cycles: {}\nSleep Time: {}\nEstimated Run Time: {}\nTrue Run Time: {}\nTotal Extra Time(seconds): {}\nExtra Time/Cycle(nanoseconds): {}\nTotal Points: {}\nPoints/Cycle: {}\nEstimated Point Gain: {}\nEstimated Points / Second: {}\n\n".format(
        datetime.now(),
        numCycles,
        sleepTime,
        estimatedRunTime,
        trueRunTime,
        totalExtraTime,
        extraTimePerCycle,
        testBase.challengePointValue,
        pointsPerCycle,
        estimatedPointGain,
        estimatedPointsPerSecond
    )
    print(printData)

    with open("testLog001.txt", "a") as file:
        file.write("================================================================================================\n")
        file.write("================================================================================================\n")
        file.write(printData)

for i in range(20):
    run()

































