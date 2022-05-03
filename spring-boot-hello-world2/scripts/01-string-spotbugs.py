import sys
import os
import shutil

sys.path.append(".")
from ScriptBuilder import ScriptBuilder

# [STEP 1] - Instantiate the builder class
try:
    string = sys.argv[1]
    print ("LASTRINGEEEEEEEE: "+string)
    try: 
        sb = ScriptBuilder()
        # SPOT -> BUGINSTANCE
        checkr="BugInstance size is"
        grep=sb.grep(string.splitlines(),checkr, True)

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
        grep=sb.grep(string.splitlines(),checkr, True)
        regex = "'{}'.split('{}')[1].strip()".format(grep, checkr)
        result= sb.check_result(regex)
        sb.printer("0",checkr,result)
    except Exception as err: 
        print (err)
        exit (1) 

except:
    print ("variables not passed")



