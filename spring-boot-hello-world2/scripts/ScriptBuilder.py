import sys
import os
import platform
import subprocess
import re
import psutil
import pwd
import shutil
import requests
from colorama import Fore, Style

# OS Calls from python doc: https://hackernoon.com/calling-shell-commands-from-python-ossystem-vs-subprocess-mc253z4f
class ScriptBuilder:

    def __init__ (self):
        pass 
    
    def runner (self, args):
            proc = subprocess.run(args,shell=True,capture_output=True)
            return [proc.returncode, proc.stdout.decode("utf-8"), proc.stderr.decode("utf-8")]
    
    # def runner (self, args):
    #     process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #     output, error = process.communicate()
        
    #     return [process.returncode, process.stdout, process.stderr]
    
    def grep (self, string, grepCmd, multiline):
        grepResult = []
        for idx, line in enumerate(string):
            if (grepCmd in line):
                grepResult.append(line)
        if (multiline):
            return grepResult[len(grepResult)-1]
        else:
            return grepResult[0]
    
    def curl (self, url, user=None, pwd=None):
        response = None
        try:
            if (user and pwd):
                response = requests.get(url, auth=(user, pwd))
            else:
                response = requests.get(url)
            
         
        except requests.exceptions.RequestException as e:
            print(e)
        return response
    
    
    def check_result (self, regex):
        # If run status Ok (exit code 0)
                return (eval(regex))
              
    def printer (self, startPattern, eval, result):
        if (result.startswith("{}".format(startPattern))):
            print (Fore.BLUE +"Evaluating: \"{}\" // result: {} ".format(eval, result))
            
        else:
            print ("ERRORASO")
            exit (1)
        #print (Fore.BLUE +" PUTO {} - Evaluating \{}/ - No Errors Found".format(text, eval))
        #     print (Fore.RESET)

            
