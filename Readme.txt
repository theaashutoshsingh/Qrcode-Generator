###################################### STEPS TO GENERATE CODE IN PYTHON ##############################
STEP 1: First of all we need to install qrcode module
        1st Method:-Open VScode and type: import subprocess; subprocess.run(["pip","install","qrcode"])
        2nd Method:-Open command prompt ant type: pip install qrcode
		3rd Method:-import subprocess
					import sys

					# sys.executable points exactly to the active Python interpreter running this code
					subprocess.run([sys.executable, "-m", "pip", "install", "qrcode"])
STEP 2: Type the code
        import qrcode as qr
	img=qr.make("Here Put the link you want to generate of")
	img.save("save.png")
STEP 3: Run
######################################################################################################
Created by: Aasutosh Pratap Singh
Date: 2026/06/14
###################################################################################################### 
