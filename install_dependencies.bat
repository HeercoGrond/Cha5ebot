mkdir C:\Tools
powershell -Command "[Net.ServicePointManager]::SecurityProtocol = 'tls12, tls11, tls'; (New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.7.1/python-3.7.1.exe', 'C:\Tools\python-3.7.1.exe')"

C:\Tools\python-3.7.1.exe /quiet InstallAllUsers=1 TargetDir=C:\Tools\Python3.7.1 Include_pip=1 Include_test=0 PrependPath=1
C:\Tools\Python3.7.1 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite