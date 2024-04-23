import time


def logMessage(logFilePath, message):
    """ Logs and prints a message"""
    with open(logFilePath, "a") as f:
        currentTime = time.time()
        timeStamp = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(currentTime)))
        message = timeStamp + ": " + message + "\n"
        print(message)
        f.write(message)