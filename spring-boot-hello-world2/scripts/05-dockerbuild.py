import sys
import os
import shutil
import unicodedata
import re
sys.path.append(".")
from ScriptBuilder import ScriptBuilder

# [STEP 1] - Instantiate the builder class
sb = ScriptBuilder()

# --------------------------------------------------------
# STAGE 5 - Build Docker image ()
# --------------------------------------------------------
directory = os.getcwd()
binary = shutil.which("docker")
command = "build . -t dpetrocelli/prueba"
dockerBuild = "cd {} ; {} {}".format(directory, binary, command)
dockerResult=sb.runner(dockerBuild)

#Ask for Failures:
try:
    checkr="Successfully built"
    grep=sb.grep(dockerResult[1].splitlines(),checkr, True)
    
    regex = "'{}'.split(' ')[0].strip()".format(grep)
    result = sb.check_result(regex)
    
    sb.printer("Successfully", "build docker image", result)
except Exception as err: 
    print (err)
    exit (1)

# Docker login in line 
command = "login --user dpetrocelli --password Osito1104** ; docker push dpetrocelli/prueba:latest"
dockerPush = "cd {} ; cd .. ; {} {}".format(directory, binary, command)
pushResult=sb.runner(dockerPush)

#Ask for Failures:
try:
    checkr="digest: "
    grep=sb.grep(pushResult[1].splitlines(),checkr, True)
    
    regex = "'{}'.split(':')[3].strip()".format(grep)
    result = sb.check_result(regex)
    print (result)
    #sb.printer("Successfully", "build docker image", result)
except Exception as err: 
    print (err)
    exit (1)




