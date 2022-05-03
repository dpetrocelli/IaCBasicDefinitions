import sys
import os
import shutil

sys.path.append(".")
from ScriptBuilder import ScriptBuilder

# [STEP 1] - Instantiate the builder class
sb = ScriptBuilder()

# (GUARDO, BKP # regex = "sbResult[1].split(i)[1].split(""\n"")[0].rstrip()")
# --------------------------------------------------------
# STAGE 1 - Code Review and Analysis (MVN SPOTBUGS SESSION)
# --------------------------------------------------------

# [STEP 2 it] - Define associated commands (binary, directory, command to be run, pattern looked at, regex evaluation)
directory = os.getcwd()
binary = shutil.which("mvn")
command = "spotbugs:check -Ddetail=true"
spotbugs = "cd {} ; cd .. ; {} {}".format(directory, binary, command)
sbResult=sb.runner(spotbugs)

# Result -> 0 -> exit status
#        -> 1 -> stdout result
#        -> 2 -> stderr result

# Now it's time to iterate asking for text Results


try: 
    # SPOT -> BUGINSTANCE
    checkr="BugInstance size is"
    grep=sb.grep(sbResult[1].splitlines(),checkr, True)

    # REGEX 
    # -> convert to int
    # -> String to be analyzed (grep result)
    # -> String pattern (ALWAYS WITH '' single quotes)
    regex = "'{}'.split('{}')[1].strip()".format(grep,checkr)
    result= sb.check_result(regex)
    
    sb.printer("0", checkr, result)
except Exception as err: 
    print (err)
    exit (1) 

try:  
    # SPOT -> ErrorSizeIS
    checkr="Error size is"
    grep=sb.grep(sbResult[1].splitlines(),checkr, True)
    regex = "'{}'.split('{}')[1].strip()".format(grep, checkr)
    result= sb.check_result(regex)
    sb.printer("0",checkr,result)
except Exception as err: 
    print (err)
    exit (1) 
