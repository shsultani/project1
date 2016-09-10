"""
This python program is taking a series of photos taken on a tripod of an object
but with a man messing up the shot. And it will use a median filter to remove the 
man and create one seamless, perfectly taken photo wihout the man in the frame.
"""

from PIL import Image 


# here we will import the images and store them into variables img 
img1 = Image.open("Project1Images/1.png")
img2 = Image.open("Project1Images/2.png")
img3 = Image.open("Project1Images/3.png")
img4 = Image.open("Project1Images/4.png")
img5 = Image.open("Project1Images/5.png")
img6 = Image.open("Project1Images/6.png")
img7 = Image.open("Project1Images/7.png")
img8 = Image.open("Project1Images/8.png") 
img9 = Image.open("Project1Images/9.png") 

# use a list to store the images into an array to use later on for median filtering 
imgArray = [img1, img2, img3, img4, img5, img6, img7, img8, img9] 

redPixelList = []
greenPixelList = []
bluePixelList = [] 

# new image that the improved and edited image will be stored and displayed in
newImage = Image.new("RGB", img1.size, 0)

pictureWidth = 495
pictureHeight = 557

def medianOdd(myList): 
		arrayLength = len(myList)
		sortedValues = sorted(myList)
		middleIndex = ((arrayLength + 1) / 2) - 1
		return sortedValues[middleIndex]

for x in range(0, pictureWidth):
	for y in range(0, pictureHeight): 
		for image in imgArray:

			myRed, myGreen, myBlue = newImage.getpixel((x,y))
			
			redPixelList.append(myRed)
			"""
			greenPixelList.append(myGreen)
			bluePixelList.append(myBlue)

			
		medianOdd(redPixelList)
		medianOdd(greenPixelList)
		medianOdd(bluePixelList)
		

		
		newImage.putpixel((x,y), medianOdd(redPixelList))
		newImage.putpixel((x,y), medianOdd(greenPixelList))
		newImage.putpixel((x,y), medianOdd(bluePixelList))
		"""

print(newImage.getpixel((4,6)))

