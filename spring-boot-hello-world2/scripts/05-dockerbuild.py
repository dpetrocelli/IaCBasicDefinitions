import sys
import os
import shutil
import unicodedata
import re
sys.path.append(".")
from ScriptBuilder import ScriptBuilder

dockerUser= sys.argv[1]
dockerPwd= sys.argv[2]
appName= sys.argv[3]

# [STEP 1] - Instantiate the builder class
sb = ScriptBuilder()

# --------------------------------------------------------
# STAGE 5 - Build Docker image ()
# --------------------------------------------------------
directory = os.getcwd()
binary = shutil.which("docker")

try: 
    command = "build . -t {}/{}".format(dockerUser, appName)
    dockerBuild = "cd {} ; {} {}".format(directory, binary, command)
    dockerResult=sb.runner(dockerBuild)
    print ("IMAGE {}:{} SUCCESFULLY BUILD".format(dockerUser, appName))
except Exception as err: 
    print ("Error building image")
    print (err)
    
# #Ask for Failures:
# try:
#     checkr="Successfully built"
#     grep=sb.grep(dockerResult[1].splitlines(),checkr, True)
    
#     regex = "'{}'.split(' ')[0].strip()".format(grep)
#     result = sb.check_result(regex)
    
#     sb.printer("Successfully", "build docker image", result)
# except Exception as err: 
#     print (err)
#     exit (1)

# Docker login in line 
try: 
    command = "login --user {} --password {} ; docker push {}/{}:latest".format(dockerUser, dockerPwd, dockerUser, appName)
    dockerPush = "cd {} ; {} {}".format(directory, binary, command)
    pushResult=sb.runner(dockerPush)
    print ("IMAGE {}:{} SUCCESFULLY PUSHED".format(dockerUser, appName))
except Exception as err: 
    print ("Error pusshing image")
    print (err)
# #Ask for Failures:
# try:
#     checkr="digest: "
#     grep=sb.grep(pushResult[1].splitlines(),checkr, True)
    
#     regex = "'{}'.split(':')[3].strip()".format(grep)
#     result = sb.check_result(regex)
#     print (result)
#     #sb.printer("Successfully", "build docker image", result)
# except Exception as err: 
#     print (err)
#     exit (1)




