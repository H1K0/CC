from PIL import Image
from os import listdir,access,F_OK,mkdir
from os.path import dirname

def main(path):
	if path[-1]not in('','\\'):path+='/'
	path=dirname(path)
	for file in listdir(path):
		if file[-4:]=='.jpg':
			pic=Image.open(f'{path}/{file}')
			win,hin=pic.size
			if win>=hin:
				wout=1000
				hout=int(1000/win*hin)
			else:
				wout=int(1000/hin*win)
				hout=1000
			pic.resize((wout,hout)).save(f'{path}/preview/{file}')
			print()
			print(f'File: {path}/{file}')
			print(f'Input size:  {win}x{hin} px')
			print(f'Output size: {wout}x{hout} px')

print('Directory to make previews (type # to exit):')
req=input('../images/')
while req!='#':
	try:main('../images/'+req)
	except Exception as e:print(e)
	else:
		print('\n')
		print('Directory to make previews (type # to exit):')
		req=input('../images/')