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
# STAGE 6 - Deploy in K8s ()
# --------------------------------------------------------
directory = os.getcwd()
binary = shutil.which("kubectl")
namespace = "dpetrocelli"
user=os.getlogin()
kubeconfig = "'/home/{}/.kube/config'".format(user)

deployment="deployment.yaml"
command = "--kubeconfig={} apply -f {} -n {}".format(kubeconfig,deployment,namespace) 
kctl = "cd {} ; {} {}".format(directory,binary, command)

kctlRunner=sb.runner(kctl)

try:
    checkr="deployment"
    grep=sb.grep(kctlRunner[1].splitlines(),checkr, True)
    print (grep)
    
except:
    pass
    

service="service.yaml"
command = "--kubeconfig={} apply -f {} -n {}".format(kubeconfig,deployment,namespace) 
kctl = "cd {} ; {} {}".format(directory,binary, command)

kctlRunner=sb.runner(kctl)

try:
    checkr="deployment"
    grep=sb.grep(kctlRunner[1].splitlines(),checkr, True)
    print (grep)
    
except:
    pass

