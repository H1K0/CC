from os import listdir
from exifread import process_file as load

def exif(image):
	with open(image,'rb')as img:data=load(img)
	out={}
	for tag in (
					'Image Model',
					'EXIF LensModel',
					'EXIF DateTimeOriginal',
					'EXIF ExposureTime',
					'EXIF FNumber',
					'EXIF ISOSpeedRatings',
					'EXIF FocalLength'
):
		try:
			if   tag=='Image Model':out['Camera']=str(data[tag])
			elif tag=='EXIF LensModel':out['Lens']=str(data[tag])
			elif tag=='EXIF DateTimeOriginal':out['DateTime']=str(data[tag]).replace(':','-',2)
			elif tag=='EXIF ExposureTime':out['Shutter Speed']=f'{data[tag]} s'
			elif tag=='EXIF FNumber':
				if '/' in str(data[tag]):out['Aperture']=f'f/{round(int(str(data[tag]).split("/")[0])/int(str(data[tag]).split("/")[1]),1)}'
				else:out['Aperture']=f'f/{data[tag]}'
			elif tag=='EXIF ISOSpeedRatings':out['ISO']=str(data[tag])
			elif tag=='EXIF FocalLength':
				if '/' in str(data[tag]):out['Focal Length']=f'{round(int(str(data[tag]).split("/")[0])/int(str(data[tag]).split("/")[1]),1)} mm'
				else:out['Focal Length']=f'{data[tag]} mm'
		except Exception as e:print(e)
	return out

if __name__=='__main__':
	print('Let\'s test!\n')
	for img in listdir('../../images/albums/golden-february'):
		print(img)
		try:data=exif(f'../../images/albums/golden-february/{img}')
		except Exception as e:print(e)
		for tag in data:print(f'{tag}: {data[tag]}')
	input()