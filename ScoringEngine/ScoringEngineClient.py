
import socket

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




scoringEngineConfigFile = "C:\\Users\\DevClientAdmin\\Desktop\\ScoringEngineConfig v0.01.txt"


#=========================FUNCTIONS===========================

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
def getUsername():
    pass

##
def enablePersistence():
    pass

##
def disablePersistence():
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

#print(setConfigValue("C:\\Users\\DevClientAdmin\\Desktop\\testConfig.txt", "idea.max.content.load.filesize", 10000, '='))

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
#====================== Main Functions =======================
#=============================================================

## Runs each validation function and performs any needed parsing or validation of returned data.
def runEvaluationCycle():
    pass

## Run after the evaluation cycle. Pools all valuable data or changes and formats them for transmission back to the server
def organizeDataForTransit():
    pass

def run():
    pass


































