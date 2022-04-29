# MeetUp DevOps - IaC Automation

# If somebody is still using Windows, you must configure Git-Bash in VSCODE

References
* https://medium.com/danielpadua/git-bash-with-vscode-593d5998f6be
* https://www.geeksforgeeks.org/how-to-integrate-git-bash-with-visual-studio-code/

# Once done (Linux or Windows with VSCODE), start this lab

You have two ways of connecting to GitHub (applicable for others Git Repositories / CICD tools)
* WAY 1 - Vía ssh keys (recommended)
* WAY 2 - Vía Token (Not recommended)

In this session we are going to execute our process using method 1. Nevertheless, at the end of this file, you will find an explanation to use Way 2 (token).

## Configure SSH Keys (WAY 1) and configure it GitHub (How we are going to work :D)

* Debemos evaluar si está corriendo el servidor de ssh en nuestro equipo:
```bash
eval $(ssh-agent -s)
```

* Create ssh key with the following command
```bash
ssh-keygen -f ~/.ssh/id_rsa -t rsa -N '' -C "david.petrocelli@cloudhesive.com"
```

* add to .gitignore file (avoid pushing this private key to the repo)

```bash
id_rsa.pub
id_rsa
id_dsa.pub
id_dsa
*.pem
*.key
```

* Import the SSH GitHub Key. Go to github.com → Settings → SSH and GPG keys → New SSH Key. Now save your private key to your computer.
```bash

cat ~/.ssh/id_rsa
.....
Once added 
SSH
ssh-rsa-unlu-class
SHA256: xxxxx
Added on Mar 19, 2022
Never used — Read/write
```
* Add to the credentials management
```bash
ssh-add ~/.ssh/id_rsa 
```

* Test ssh connection
```bash
ssh -T git@github.com

Attempts to ssh to GitHub

The authenticity of host 'github.com (20.201.28.151)' can't be established.
ECDSA key fingerprint is SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com,20.201.28.151' (ECDSA) to the list of known hosts.
Hi dpetrocelli! You've successfully authenticated, but GitHub does not provide shell access.
```

* Configure username and global configuration for our GIT Client

git config --global user.name "davidpetrocelli"
git config --global user.email "davidpetrocelli@cloudhesive.com"

git add . ; git commit -m "first push" ; git push

* Set the origin branch to our "remote" git

git remote -v
git remote set-url origin git@github.com:cloudhesive/CHStandardAutomationAndIaC.git

## OK, but if i need different SSH keys for different accounts? For example, personal accounts and Work account
- 2 or more ssh-keys, for example
 id_rsa  id_rsa_cloudhesive             -> private
 id_rsa_cloudhesive.pub  id_rsa.pub     -> public

(Obviously, each keys is already uploaded to GitHub)

- Create "config" file in $HOME/.ssh/ folder
```bash
#personal account
Host github.com-personal
        HostName github.com
        User git
        IdentityFile ~/.ssh/id_rsa

#cloudhesive account
Host github.com-cloudhesive
        HostName github.com
        User git
        IdentityFile ~/.ssh/id_rsa_cloudhesive
```

- Once configured, test your connections (pay attention to hostname changed)
```bash
ssh -T git@github.com-cloudhesive
Hi davidpetrocelli! You've successfully authenticated, but GitHub does not provide shell access.

ssh -T git@github.com-personal
Hi dpetrocelli! You've successfully authenticated, but GitHub does not provide shell access.
```

- It's time to clone
```bash
git clone git@github.com-cloudhesive:cloudhesive/CHStandardAutomationAndIaC.git
```

- It's time to push some change
```
git add . ; git commit -m "readme base" ; git push
```

## Once connected to GitHub (pull / push), start playing with GitHub Actions

GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline.

GitHub give to you Linux, Windows y macOS VMs to test, run and deploy your workloads ..
Something NICE -> You can host your own self-hosted worker nodes. ** (Expand it) **

To start playing with GitHub Actions 
In your repository, create the .github/workflows/ directory to store your workflow scripts. (x ej: .github/workflows/prueba.yml)

### Really "simple" test (Create pipeline to deploy an nginx pod to K8s)

Use a free K8s service:
https://cloud.okteto.com/#/spaces/dpetrocelli

* What you need and what you have to configure

** Obtain Base64 Kubeconfig from your K8s Cluster (could be this free service or whatever you want!) As you know is agnostic :).

In OKTETO follow this path. 

-> Developer Settings -> Personal Access Tokens -> 

** Now github go to project () -> settings ->  secrets -> actions -> 

https://github.com/cloudhesive/CHStandardAutomationAndIaC/actions/

And store this secret (KUBE_CONFIG_DATA). 
This token is going to be used as environment variable in the GitHub actions pipeline. 
(see that information in yaml file)

```bash
kube_config_data=$(cat Desktop/okteto-kube.config | base64)
```

** Check the GA yaml

** Run the simple pipeline and access the Nginx service 

# Configure GH Token to modify code and push it :)

## WAY 1 (Not recommended)
1. Login to GH 
2. Go to your profile (logo)
3. Go Settings
4. Developer settings
5. personal access tokens
6. new
7. name it -> full access
8. save your token :) 

# Now clean your current configure
```bash
git config --global user.name ""
git config --global user.email ""
git config -l
```
# Now configure your user (mail) and then paste the token
```bash
git config --global user.email "dmpetrocelli@gmail.com"
```

Lastly, to ensure the local computer remembers the token, we can enable caching of the credentials. This configures the computer to remember the complex token so that we dont have too.
```bash
git config --global credential.helper cache
#or 
git config credential.helper 'cache --timeout=<timeout>'
```
#If needed, you can later clear the token from the local computer by running
```bash
git config --global --unset credential.helper
