###SurfLink (revise)
###This program pulls photos from Upload folder, watermarks photos, and saves new copy in Ocean Beach Watermark folder
###And sorts files in Ocean Beach Upload Folder by modified date and moves to Ocean Beach Backup folder
###And sorts watermarked files in Ocean Beach Watermark Folder by modified date and saves under Ocean Beach Folder

#Import Required Libraries
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from zipfile import ZipFile
import glob, shutil, os, time, sys
from os import path

#Key
database = 'C:/Users/Kristina Stodder/Dropbox/Apps/SurfLink'
oceanbeach_data = '/Ocean Beach Database'
mavericks_data = '/Mavericks Database'
teahupoo_data = '/Teahupoo Database'

#KEY
watermark = '/Watermark'
upload = '/Upload'
backup = '/Backup'
zip_archive = '/Zip Archive'


##Extracts photos from zip file in Uploads folder and saves in spot Uploads folder
#If file begins with spot name, move from Uploads folder to spot Upload folder
for name in glob.glob(database+'/Uploads/Ocean Beach*'):
        shutil.move(name, database+oceanbeach_data+upload)
for name in glob.glob(database+'/Uploads/Mavericks*'):
        shutil.move(name, database+mavericks_data+upload)
for name in glob.glob(database+ '/Uploads/Teahupoo*'):
        shutil.move(name, database+teahupoo_data+upload)
print('Zipfile moved to Spot Upload folder')



########OCEAN BEACH###############
#Unzip to new folder with datetime name and move the zip to Ocean Beach Zip Archive folder
for z in glob.glob(database+oceanbeach_data+upload+'/*.zip'):
        yz=z[-17:-13]
        mz=z[-12:-10]
        dz=z[-9:-7]
        idz=z[-7:-4]
        with ZipFile(z) as zip:
            zip.extractall(database+oceanbeach_data+upload+'/Ocean Beach '+yz+'-'+mz+'-'+dz+idz)
        shutil.move(z, database+oceanbeach_data+zip_archive)
print('Files extracted & zipfile archived')

#Move files in new folder and renames as jpg 
i=10
for j in glob.glob(database+oceanbeach_data+upload+'/**/*'):
    i+=1
    for f in glob.glob(database+oceanbeach_data+upload+'/*'):
        yj=f[-13:-9]
        mj=f[-8:-6]
        dj=f[-5:-3]
        nj=f[-3:]
        os.rename(j, database+oceanbeach_data+upload+'/Ocean Beach '+yj+'-'+mj+'-'+dj+nj+str(i)+'.jpg')
        if j != database+oceanbeach_data+upload+'/Ocean Beach '+yj+'-'+mj+'-'+dj+nj+str(i)+'.jpg':
                break
print('Renaming Complete')

#10sec checkpoint
print('10 sec pause')
time.sleep(10)
print('Continuing on')

#Move empty folder to Ocean Beach Zip Archive
for e in glob.glob(database+oceanbeach_data+upload+'/?????????????????????????'):
        shutil.move(e, database+oceanbeach_data+zip_archive)
print('Empty Folder Archived')

#10sec checkpoint
print('10 sec pause')
time.sleep(10)
print('Continuing on')

##Pulls photos from Ocean Beach Upload folder, watermarks photos, and saves new copy in Ocean Beach Watermark folder


#Define u_photo & w_photo
for file in os.listdir(database+oceanbeach_data+upload):
    
    u_photo = database+oceanbeach_data+upload+'/'+file
    w_photo = database+oceanbeach_data+watermark+'/'+file

#Create an Image Object from an Image
    photo = Image.open(u_photo).convert('RGBA')
    txt = Image.new('RGBA', photo.size, (255,255,255,0))
    width, height = photo.size

#Define Watermark Text
    draw = ImageDraw.Draw(txt)
    text = "SurfPhotoLink"
    font = ImageFont.truetype('arial.ttf', 300)
    textwidth, textheight = draw.textsize(text,font)

#Calculate the x,y coordinates of the text
    margin = 1000
    x = width - textwidth - margin
    y = height - textheight - margin

#Draw watermark in the bottom right corner
    draw.text((x, y), text, fill=(255,255,255, 125), font=font)

#Save watermarked image
    watermarked = Image.alpha_composite(photo, txt)
    watermarked.save(w_photo, "PNG")
    print("Moving {}".format(file))
print('Watermarking Complete')

#10sec checkpoint
print('10 sec pause')
time.sleep(10)
print('Continuing on')

#Moves jpgs from Ocean Beach Watermark folder to Ocean Beach folder
for filename in glob.glob(database+oceanbeach_data+watermark+'/*.jpg'):
        shutil.move(filename, database+oceanbeach_data+'/Ocean Beach')
print('Jpgs moved from Ocean Beach Watermark folder to Ocean Beach folder')

#10sec checkpoint
print('10 sec pause')
time.sleep(10)
print('Continuing on')


#Moves jpgs from Ocean Beach Upload folder to Ocean Beach Backup folder
for filename in glob.glob(database+oceanbeach_data+upload+'/*.jpg'):
        shutil.move(filename, database+oceanbeach_data+backup)
print('Jpgs moved from Ocean Beach Upload folder to Ocean Beach Backup folder')




########MAVERICKS###############
#Unzip to new folder with datetime name and move the zip to Mavericks Zip Archive folder
for z in glob.glob(database+mavericks_data+upload+'/*.zip'):
        yz=z[-17:-13]
        mz=z[-12:-10]
        dz=z[-9:-7]
        idz=z[-7:-4]
        with ZipFile(z) as zip:
            zip.extractall(database+mavericks_data+upload+'/Mavericks '+yz+'-'+mz+'-'+dz+idz)
        shutil.move(z, database+mavericks_data+zip_archive)
print('Files extracted & zipfile archived')

#Move files in new folder and renames as jpg 
i=10
for j in glob.glob(database+mavericks_data+upload+'/**/*'):
    i+=1
    for f in glob.glob(database+mavericks_data+upload+'/*'):
        yj=f[-13:-9]
        mj=f[-8:-6]
        dj=f[-5:-3]
        nj=f[-3:]
        os.rename(j, database+mavericks_data+upload+'/Mavericks '+yj+'-'+mj+'-'+dj+nj+str(i)+'.jpg')
        if j != database+mavericks_data+upload+'/Mavericks '+yj+'-'+mj+'-'+dj+nj+str(i)+'.jpg':
                break
print('Renaming Complete')

#10sec checkpoint
print('10 sec pause')
time.sleep(10)
print('Continuing on')

#Move empty folder to Mavericks Zip Archive
for e in glob.glob(database+mavericks_data+upload+'/???????????????????????'):
        shutil.move(e, database+mavericks_data+zip_archive)
print('Empty Folder Archived')

#10sec checkpoint
print('10 sec pause')
time.sleep(10)
print('Continuing on')

##Pulls photos from Mavericks Upload folder, watermarks photos, and saves new copy in Mavericks Watermark folder


#Define u_photo & w_photo
for file in os.listdir(database+mavericks_data+upload):
    
    u_photo = database+mavericks_data+upload+'/'+file
    w_photo = database+mavericks_data+watermark+'/'+file

#Create an Image Object from an Image
    photo = Image.open(u_photo).convert('RGBA')
    txt = Image.new('RGBA', photo.size, (255,255,255,0))
    width, height = photo.size

#Define Watermark Text
    draw = ImageDraw.Draw(txt)
    text = "SurfPhotoLink"
    font = ImageFont.truetype('arial.ttf', 300)
    textwidth, textheight = draw.textsize(text,font)

#Calculate the x,y coordinates of the text
    margin = 1000
    x = width - textwidth - margin
    y = height - textheight - margin

#Draw watermark in the bottom right corner
    draw.text((x, y), text, fill=(255,255,255, 125), font=font)

#Save watermarked image
    watermarked = Image.alpha_composite(photo, txt)
    watermarked.save(w_photo, "PNG")
    print("Moving {}".format(file))
print('Watermarking Complete')

#10sec checkpoint
print('10 sec pause')
time.sleep(10)
print('Continuing on')

#Moves jpgs from Mavericks Watermark folder to Mavericks folder
for filename in glob.glob(database+mavericks_data+watermark+'/*.jpg'):
        shutil.move(filename, database+mavericks_data+'/Mavericks')
print('Jpgs moved from Mavericks Watermark folder to Mavericks folder')

#10sec checkpoint
print('10 sec pause')
time.sleep(10)
print('Continuing on')


#Moves jpgs from Mavericks Upload folder to Mavericks Backup folder
for filename in glob.glob(database+mavericks_data+upload+'/*.jpg'):
        shutil.move(filename, database+mavericks_data+backup)
print('Jpgs moved from Mavericks Upload folder to Mavericks Backup folder')




########TEAHUPO'O###############
#Unzip to new folder with datetime name and move the zip to Teahupoo Zip Archive folder
for z in glob.glob(database+teahupoo_data+upload+'/*.zip'):
        yz=z[-17:-13]
        mz=z[-12:-10]
        dz=z[-9:-7]
        idz=z[-7:-4]
        with ZipFile(z) as zip:
            zip.extractall(database+teahupoo_data+upload+'/Teahupoo '+yz+'-'+mz+'-'+dz+idz)
        shutil.move(z, database+teahupoo_data+zip_archive)
print('Files extracted & zipfile archived')

#Move files in new folder and renames as jpg 
i=10
for j in glob.glob(database+teahupoo_data+upload+'/**/*'):
    i+=1
    for f in glob.glob(database+teahupoo_data+upload+'/*'):
        yj=f[-13:-9]
        mj=f[-8:-6]
        dj=f[-5:-3]
        nj=f[-3:]
        os.rename(j, database+teahupoo_data+upload+'/Teahupoo '+yj+'-'+mj+'-'+dj+nj+str(i)+'.jpg')
        if j != database+teahupoo_data+upload+'/Teahupoo '+yj+'-'+mj+'-'+dj+nj+str(i)+'.jpg':
                break
print('Renaming Complete')

#10sec checkpoint
print('10 sec pause')
time.sleep(10)
print('Continuing on')

#Move empty folder to Teahupoo Zip Archive
for e in glob.glob(database+teahupoo_data+upload+'/??????????????????????'):
        shutil.move(e, database+teahupoo_data+zip_archive)
print('Empty Folder Archived')

#10sec checkpoint
print('10 sec pause')
time.sleep(10)
print('Continuing on')

##Pulls photos from Teahupoo Upload folder, watermarks photos, and saves new copy in Teahupoo Watermark folder


#Define u_photo & w_photo
for file in os.listdir(database+teahupoo_data+upload):
    
    u_photo = database+teahupoo_data+upload+'/'+file
    w_photo = database+teahupoo_data+watermark+'/'+file

#Create an Image Object from an Image
    photo = Image.open(u_photo).convert('RGBA')
    txt = Image.new('RGBA', photo.size, (255,255,255,0))
    width, height = photo.size

#Define Watermark Text
    draw = ImageDraw.Draw(txt)
    text = "SurfPhotoLink"
    font = ImageFont.truetype('arial.ttf', 300)
    textwidth, textheight = draw.textsize(text,font)

#Calculate the x,y coordinates of the text
    margin = 1000
    x = width - textwidth - margin
    y = height - textheight - margin

#Draw watermark in the bottom right corner
    draw.text((x, y), text, fill=(255,255,255, 125), font=font)

#Save watermarked image
    watermarked = Image.alpha_composite(photo, txt)
    watermarked.save(w_photo, "PNG")
    print("Moving {}".format(file))
print('Watermarking Complete')

#10sec checkpoint
print('10 sec pause')
time.sleep(10)
print('Continuing on')

#Moves jpgs from Ocean Beach Watermark folder to Teahupoo folder
for filename in glob.glob(database+teahupoo_data+watermark+'/*.jpg'):
        shutil.move(filename, database+teahupoo_data+'/Teahupoo')
print('Jpgs moved from Teahupoo Watermark folder to Teahupoo folder')

#10sec checkpoint
print('10 sec pause')
time.sleep(10)
print('Continuing on')


#Moves jpgs from Teahupoo Upload folder to Teahupoo Backup folder
for filename in glob.glob(database+teahupoo_data+upload+'/*.jpg'):
        shutil.move(filename, database+teahupoo_data+backup)
print('Jpgs moved from Teahupoo Upload folder to Teahupoo Backup folder')


####Program Complete line
print('Program Complete!')

