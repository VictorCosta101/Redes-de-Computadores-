import subprocess
display = subprocess.check_output("dir ", shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
print(display)
