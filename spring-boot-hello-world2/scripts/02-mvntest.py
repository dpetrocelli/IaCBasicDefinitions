import sys
import os
import shutil
import unicodedata
import re
sys.path.append(".")
from ScriptBuilder import ScriptBuilder

# [STEP 1] - Instantiate the builder class
print ("builder")
sb = ScriptBuilder()

# --------------------------------------------------------
# STAGE 2 - Unit Test Code (MVN TEST SESSION)
# --------------------------------------------------------

directory = os.getcwd()
binary = shutil.which("mvn")
command = "test"
mvnTest = "cd {} ; {} {}".format(directory, binary, command)
testResult=sb.runner(mvnTest)


Ask for Failures:
try:
    checkr="Failures:"
    grep=sb.grep(testResult[1].splitlines(),checkr, True)
    print ("ELGRE: {}".format(grep))
    # regex = "'{}'.split('{}')[1].split(',')[0].strip()".format(grep, checkr)
    # result = sb.check_result(regex)

    # sb.printer("0", checkr, result)
except Exception as err: 
    print (err)
    exit (1)


# #Ask for Errors:

# try:
#     checkr="Errors:"
#     grep=sb.grep(testResult[1].splitlines(),checkr, True)
#     regex = "'{}'.split('{}')[1].split(',')[0].strip()".format(grep, checkr)
    
#     result = sb.check_result(regex)
#     sb.printer("0", checkr, result)
# except Exception as err: 
#     print (err)
#     exit (1)
    
    
# # # Ask for Skipped:

# try:
#     checkr="Skipped:"
#     grep=sb.grep(testResult[1].splitlines(),checkr, True)
    
#     regex = "('{}'.split('{}')[1].strip())".format(grep, checkr)
    
#     result = sb.check_result(regex)
#     sb.printer("0", checkr, result)
#     # ansi_escape = re.compile(r'\x1bm')
    
#     # ansi_escape.sub('', result)
#     # print (int(result))
#     #sb.printer(result, checkr, result)
# except Exception as err: 
#     print (err)
#     exit (1)