import sys
import os
import shutil
import time
from SonarClass import SonarqubeAnalyzer as sa
from ScriptBuilder import ScriptBuilder

# COMANDO PARA INICIALIZAR EL SCANNEO DE SONARQUBE.
# mvn compile -Dmaven.test.skip=true sonar:sonar -Dsonar.projectKey=$sonar_project_key -Dsonar.sources="." -Dsonar.host.url=$sonar_host_url -Dsonar.login=$sonar_username -Dsonar.password=$sonar_password -Dsonar.projectVersion=1.0 -Dsonar.sources=src/main -Dsonar.sourceEncoding=UTF-8 -Dsonar.language=java -Dsonar.java.binaries=target/classes -Dsonar.coverage.jacoco.xmlReportPaths=target/site/jacoco-ut/jacoco.xml

# HARCODED VARS:
sonarHost="http://localhost:9090"
projectKey="hello-world"
sonarUser="admin" 
sonarPwd="adminadmin"
sources = "src/main"

directory = os.getcwd()
binary = shutil.which("mvn")
# command = "compile -Dmaven.test.skip=true {}:{} -Dsonar.host.url={}".format(
#     sonarUser, 
#     sonarPwd, 
#     hostUrl
# )

sb = ScriptBuilder()
command = "sonar:sonar -Dsonar.projectKey={} -Dsonar.sources={} -Dsonar.host.url={} -Dsonar.login={} -Dsonar.password={}".format(projectKey, sources, sonarHost, sonarUser, sonarPwd)
sonarRunner = "cd {} ; {} {}".format(directory, binary, command)
#print (sonarRunner)
try:
    sonar=sb.runner(sonarRunner)
    # get task id 
    if (sonar[0]==0):
        # FIRST GET TASK ID
        checkr="task?id="
        grep=sb.grep(sonar[1].splitlines(),checkr, True)
        regex = "'{}'.split('{}')[1].strip()".format(grep,checkr)
        
        sonarTaskId= sb.check_result(regex)
        
        # SECOND, GET AnalysisID 
        sonarAnalysisId="{}/api/ce/task?id={}".format(sonarHost,sonarTaskId)
        analysisId=None
        
        # Wait until SQ has finished the analysis (based on analysisID)
        loop=0
        while (loop<5):
            response = sb.curl(sonarAnalysisId, sonarUser, sonarPwd).json()
            
            if (response["task"]["status"] == "SUCCESS"):
                analysisId=response["task"]["analysisId"]
                break
            else:
                time.sleep(5)
            loop+=1
        # Once success, GET QG Result
        qg="{}/api/qualitygates/project_status?analysisId={}".format(sonarHost,analysisId)
        response = sb.curl(qg, sonarUser, sonarPwd).json()

        sb.printer("OK", "Sonarqube QG", response["projectStatus"]["status"])
      
    else:
        print ("Sonarqube is stopped or miss-configured")
        exit(1)
except Exception as err:
    print (err)
    exit (1)

