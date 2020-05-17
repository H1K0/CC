from PIL import Image
from os import listdir,access,F_OK,mkdir
from os.path import dirname

def make_previews(path):
	if path[-1]not in('/','\\'):path+='/'
	path=dirname(path)
	if not access(path+'/preview',F_OK):mkdir(path+'/preview')
	for file in listdir(path):
		if file[-4:]=='.jpg':
			pic=Image.open(f'{path}/{file}')
			win,hin=pic.size
			if win>1000 and hin>1000:
				if win>=hin:
					wout=1000
					hout=1000*hin//win
				else:
					wout=1000*win//hin
					hout=1000
				pic.resize((wout,hout)).save(f'{path}/preview/{file}')
				print()
				print(f'File: {path}/{file}')
				print(f'Input size:  {win}x{hin} px')
				print(f'Output size: {wout}x{hout} px')

if __name__=='__main__':
	print('=== PreviewMaker ===\n © Masahiko AMANO a.k.a. H1K0, 2020')
	while 1:
		print('\nDirectory to make previews:')
		req=input('../../images/')
		try:make_previews('../../images/'+req)
		except Exception as e:print(e)
		else:print('SUCCESS')