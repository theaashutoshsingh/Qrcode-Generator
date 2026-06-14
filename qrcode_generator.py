#import subprocess; subprocess.run(["pip","install","qrcode"])

import qrcode as qr
img=qr.make("https://www.aashutoshsingh.com.np/")
img.save("Profile.png")