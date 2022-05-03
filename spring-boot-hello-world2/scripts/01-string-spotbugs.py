import sys
import os
import shutil

sys.path.append(".")
from ScriptBuilder import ScriptBuilder

# [STEP 1] - Instantiate the builder class
try:
    
    with open(os.getcwd()+"/scripts/spotbugs.txt") as f:
        lines = f.readlines()
    lines = ''.join(lines)
    print(lines)
    try: 
        sb = ScriptBuilder()
        # SPOT -> BUGINSTANCE
        checkr="BugInstance size is"
        grep=sb.grep(lines.splitlines(),checkr, True)

        # REGEX 
        # -> convert to int
        # -> String to be analyzed (grep result)
        # -> String pattern (ALWAYS WITH '' single quotes)
        regex = "'{}'.split('{}')[1].strip()".format(grep,checkr)
        result= sb.check_result(regex)
        print(result)
        
        sb.printer("0", checkr, result)
    except Exception as err: 
        print("asdfasdfasfas")
        print (err)
        exit (1) 

    try:  
        # SPOT -> ErrorSizeIS
        checkr="Error size is"
        grep=sb.grep(lines.splitlines(),checkr, True)
        regex = "'{}'.split('{}')[1].strip()".format(grep, checkr)
        result= sb.check_result(regex)
        sb.printer("0",checkr,result)
    except Exception as err: 
        print("asdfasdfasfas2")
        print (err)
        exit (1) 

except Exception as err:
    print (err)
    print ("variables not passed")



