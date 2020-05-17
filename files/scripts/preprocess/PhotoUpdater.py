from EXIFer import exif
from PreviewMaker import make_previews
from GalleryBuilder import build
from os import listdir
from os.path import isdir,dirname

def scan(path):
	global scandata
	if path[-1]not in('/','\\'):path+='/'
	for item in listdir(path):
		if item!='preview' and isdir(path+item):
			scan(path+item)
		elif item[-4:]=='.jpg' and item!='cover.jpg':
			dt=exif(path+item)['DateTime']
			if not any([i[1]==dt for i in scandata]):scandata.append([path+item,dt])

if __name__=='__main__':
	input('Update? Press ENTER to start. ')
	scandata=[]
	print('Start scanning albums...')
	scan('../../images/albums/')
	print('Completed.')
	print('Start scanning other photos...')
	scan('../../images/photos/')
	print('Completed.')
	print('Sorting by datetime...')
	scandata.sort(key=lambda ph:ph[1])
	print('Completed.')
	print('Removing time remaining only date...')
	scandata=list(map(lambda ph:[ph[0],ph[1].split()[0]],scandata))
	print('Completed.')
	print('Making dictionary "date:[photos]"...')
	dates={}
	for ph in scandata:
		if ph[1] in dates.keys():dates[ph[1]].append(ph[0])
		else:dates[ph[1]]=[ph[0]]
	print('Building HTMLs...')
	for date in dates.keys():
		try:
			build(date,0,0,'en',dates[date])
			build(date,0,0,'ru',dates[date])
			build(date,0,0,'jp',dates[date])
		except Exception as e:print(e)
	print('Completed.')
	print('Updating previews...')
	make_previews('../../images/photos')
	print('Completed.')
	print('Building UL for photo page...')
	ul={}
	for date in dates.keys():
		year,month,day=date.split('-')
		if year in ul.keys():
			if month in ul[year].keys():ul[year][month].append(day)
			else:ul[year][month]=[day]
		else:
			ul[year]={}
			ul[year][month]=[day]
	out=''
	for year in list(ul.keys())[::-1]:
		out+=f'{" "*6}<li class="year">\n{" "*8}<h3 class="year-value" onclick="view(\'{year}\')">{year}</h3>\n{" "*8}<ul class="months" id="{year}">\n'
		for month in list(ul[year].keys())[::-1]:
			out+=f'{" "*10}<li class="month">\n{" "*12}<h3 class="month-value" onclick="view(\'{year}-{month}\')">{month}</h3>\n{" "*12}<ul class="days" id="{year}-{month}">\n'
			for day in ul[year][month][::-1]:
				out+=f'{" "*14}<li class="day"><a href="photos/date/{year}-{month}-{day}" target="_blank"><h3 class="day-value">{day}</h3></a></li>\n'
			out+=f'{" "*12}</ul>\n{" "*10}</li>\n'
		out+=f'{" "*8}</ul>\n{" "*6}</li>\n'
	with open('out.html','w',encoding='utf-8')as html:html.write(out)
	print('Completed.')
	input()