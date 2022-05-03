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
# STAGE 4 - Build APP (MVN Build SESSION)
# --------------------------------------------------------
directory = os.getcwd()
binary = shutil.which("mvn")
command = "clean package -DskipTests"
mvnBuild = "cd {} ; {} {}".format(directory, binary, command)
buildResult=sb.runner(mvnBuild)

#Ask for Failures:
try:
    checkr="BUILD SUCCESS"
    grep=sb.grep(buildResult[1].splitlines(),checkr, True)
    
    regex = "'{}'.split(' ')[2].strip()".format(grep)
    result = sb.check_result(regex)
    
    sb.printer("SUCCESS", checkr, result)
except Exception as err: 
    print (err)
    exit (1)


