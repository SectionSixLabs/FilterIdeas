#Possible Filter Idea for the CSUMB-erize Instagram Filter
#What it does so far is just copy the CSUMB logo onto an chosen image
#Not sure what to do with the original image yet, Possibly make it monochrome
#Or possibly artified black / white...

def pyCopy(source, target, targetX, targetY): #source need be a makePicture object parameter
  #pic = makePicture(source)  #input course should be file directory path
  #above is commented out so that source is now a makepicture parameter
  #that way use functions that pipe into pyCopy

  pic = source
  pwidth = getWidth(pic)
  pheight = getHeight(pic)

  for x in range(0, pwidth):
    for y in range(0, pheight):
      colorSource = getColor(getPixel(pic, x, y)) #get color pixel of source
      targetPixel = getPixel(target, x+targetX, y+targetY) #target pixel
      setColor(targetPixel, colorSource)

def logoCopy(target, targetX, targetY): #source need be a makePicture object parameter
  #pic = makePicture(source)  #input course should be file directory path
  #above is commented out so that source is now a makepicture parameter
  #that way use functions that pipe into pyCopy

  logo = makePicture('/home/wave/Downloads/gitWorkspace/FilterIdeas/logo.png')
  pwidth = getWidth(logo)
  pheight = getHeight(logo)

  wPixel = makeColor(255, 255, 255) #Pixel to ignore in logo (this is white)


  for x in range(0, pwidth):
    for y in range(0, pheight):
      colorSource = getColor(getPixel(logo, x, y)) #get color pixel of source
      targetPixel = getPixel(target, x+targetX, y+targetY) #target pixel
      if(colorSource != wPixel):
        setColor(targetPixel, colorSource)

def advance(source):
  
  pic = source
  #make pic into black and white image
  pixels = getPixels(pic)
  for p in pixels:
    redP = getRed(p)
    blueP = getBlue(p)
    greenP = getGreen(p)
    averageP = redP*0.299 + greenP*0.587 + blueP*0.114
    makeGrey = makeColor(averageP, averageP, averageP)
    setColor(p, makeGrey)


  width = getWidth(pic)
  height = getHeight(pic)
   
  for x in range(0, width-1):
    for y in range(0, height-1):
      currentPixel = getPixel(pic, x, y)
      belowPixel = getPixel(pic, x, y+1)
      rightPixel = getPixel(pic, x+1, y)
      
      #luminescence 
      currentPixelLum = (getRed(currentPixel) + getGreen(currentPixel) + getBlue(currentPixel))/3
      belowPixelLum = (getRed(belowPixel) + getGreen(belowPixel) + getBlue(belowPixel))/3
      rightPixelLum = (getRed(rightPixel) + getGreen(rightPixel) + getBlue(rightPixel))/3
  
      #from trying various differenceValues, increasing number resulted in less filled in black pixels and vice versa
      differenceValue = 5
      if( abs(currentPixelLum - belowPixelLum) > differenceValue and abs(currentPixelLum - rightPixelLum) > differenceValue):
        setColor(currentPixel, black)

      if( abs(currentPixelLum - belowPixelLum) <= differenceValue and abs(currentPixelLum - rightPixelLum) <= differenceValue):
        setColor(currentPixel, white) 
  
  return pic


def filter():
    file = pickAFile()
    pic = makePicture(file)
    width = getWidth(pic)
    height = getHeight(pic)
    if(height < 250): #250 is logo height
      print("Image height too small")
      return None
    if(width < 685): #685 is logo width
      print("Image width is too small")
      return None

    canvas = makeEmptyPicture(width, height)
    pyCopy(advance(pic), canvas, 0, 0)

    logoCopy(canvas, 0, height-250) #logo height 250

    show(canvas)
    writePictureTo(canvas, '/home/wave/Downloads/gitWorkspace/FilterIdeas/filterOutput.jpg')
    return(canvas)
