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

  logo = makePicture('/home/wave/Desktop/filters/logo.png')
  pwidth = getWidth(logo)
  pheight = getHeight(logo)

  wPixel = makeColor(255, 255, 255) #Pixel to ignore in logo (this is white)


  for x in range(0, pwidth):
    for y in range(0, pheight):
      colorSource = getColor(getPixel(logo, x, y)) #get color pixel of source
      targetPixel = getPixel(target, x+targetX, y+targetY) #target pixel
      if(colorSource != wPixel):
        setColor(targetPixel, colorSource)




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
    pyCopy(pic, canvas, 0, 0)

    logoCopy(canvas, 0, height-250) #logo height 250

    show(canvas)
    return(canvas)
