import os

folderPath = "G:\My Drive\Grad Pica"

for filename in os.listdir(folderPath):
    if filename.endswith(".heic"):
            newFilename = os.path.splitext(filename)[0] + ".jpg"
	            os.rename(os.path.join(folderPath, filename), os.path.join(folderPath, newFilename))
