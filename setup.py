#for windows you need to download: winpcap: http://www.win10pcap.org/download/
import sys,setuptools,os,subprocess,platform
with open("README.md", "r") as fh:
    long_description = fh.read()

termux=False

if os.path.isdir('/home/')==True:
    if os.geteuid() == 0:
        #if not os.getenv("SUDO_USER"):
        if os.getenv("SUDO_USER"):
            pm="apt"
            for x in ["apt","yum","pacman","dnf","zypper","brew"]:
                if subprocess.call(["which", x], stdout=subprocess.PIPE, stderr=subprocess.PIPE)==0:
                    pm=x
                    break
            os.system('sudo '+pm+' install sshpass -y')
            os.system('sudo '+pm+' install tor -y')
    else:
       print('\n\nYou didn\'t the installation run with root privilege !\nYou will have to install the following packages manually: sshpass , tor\n\n\n')

adr=False

if os.path.isdir('/data/data')==True:
    adr=True

if os.path.isdir('/data/data/com.termux/')==True:
    termux=True
    os.system('pkg install openssh -y')
    os.system('pkg install sshpass -y')
    os.system('pkg install tor -y')

if termux==False:
   if  sys.version_info < (3,0):
    os.system('pip uninstall dnspython -y')
    os.system('pip install dnspython')
   else:
    os.system('pip3 uninstall dnspython -y')
    os.system('pip3 install dnspython')

#protobuf==3.6.1

if  sys.version_info < (3,0):
    req=["furl","future","xtelnet>=2.1.6","requests","PySocks","bs4","pymysql==0.9.3","scapy==2.4.0","stem","google","colorama","dnspython"]
    if adr==True:
        req=["furl","future","xtelnet>=2.1.6","requests","PySocks","bs4","pymysql==0.9.3","scapy==2.4.0","google","colorama","dnspython"]
    if termux==True:
       req=["furl","future","xtelnet>=2.1.6","requests","PySocks","bs4","pymysql==0.9.3","scapy==2.4.0","google","colorama","dnspython"]
else:
    req=["furl","future","xtelnet>=2.1.6","requests","PySocks","bs4","pymysql","kamene==0.32","stem","google","colorama","dnspython"]
    if adr==True:
        req=["furl","future","xtelnet>=2.1.6","requests","PySocks","bs4","pymysql","kamene==0.32","google","colorama","dnspython"]
    if termux==True:
        req=["furl","future","xtelnet>=2.1.6","requests","PySocks","bs4","pymysql","kamene==0.32","google","colorama","dnspython"]


if (sys.platform == "win32") or( sys.platform == "win64"):
    req+=["win_inet_pton"]

if hasattr(os, 'PyShadowString'):
  if  os.name==os.PyShadowString('java', 'nt'):
    req+=["win_inet_pton"]

req+=['jsbeautifier','tldextract']
if platform.system()=='Java':
    if "stem" in req:
        req.remove("stem")
    if "scapy==2.4.0" in req:
      req.remove('scapy==2.4.0')
    if "jsbeautifier" in req:
      req.remove('jsbeautifier')


setuptools.setup(
    name="bane",
    version="5.0.0",
    author="AlaBouali",
    author_email="ala.bouali.1997@gmail.com",
    description="cyber security library, penetration testing module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlaBouali/bane",
    python_requires=">=2.7",
    install_requires=req,
    packages=setuptools.find_packages(),
    license="MIT License",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License ",
    ],
)
