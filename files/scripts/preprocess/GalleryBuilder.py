from EXIFer import exif
from os.path import dirname,basename

def build(name,link,lnth,lang,phlist=[]):
	def alt_title():
		if lang=='en':return f'alt="{name} -> Photo #{i+1}" title="{name} -> Photo #{i} (Click to view fullsized)"'
		if lang=='ru':return f'alt="{name} -> Фото №{i+1}" title="{name} -> Фото №{i} (Кликни, чтобы глянуть фулл)"'
		if lang=='jp':return f'alt="{name} -> 写真第{i+1}枚" title="{name} -> 写真第{i}枚（クリックして完全版を見る）"'
	if phlist:
		lnth=len(phlist)
		if lang=='en':title=f'Masahiko AMANO -> Photos from {name}'
		elif lang=='ru':title=f'Масахико АМАНО -> Фотографии от {name}'
		else:title=f'天人楽彦 -> {name}の写真'
	else:
		link='albums/'+link
		if lang=='en':title=f'Masahiko AMANO -> Album «{name}»'
		elif lang=='ru':title=f'Масахико АМАНО -> Альбом «{name}»'
		else:title=f'天人楽彦 -> アルバム「{name}」'
	data=(
f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
	<meta charset="UTF-8">
	<title>{title}</title>
	<link rel="shortcut icon" href="{"../"*bool(phlist)}../../files/images/icon.png" type="image/png">
	<link rel="stylesheet" href="{"../"*bool(phlist)}../../files/style/album.css">
</head>
<body>
	<header>{name}</header>'''
)
	for i in range(lnth):
		if phlist:
			link=dirname(phlist[i]).replace('../../images/','')
			ph=basename(phlist[i])
		else:ph=str(i+1).rjust(3,"0")+'.jpg'
		data+=(
f'<div class="photo"><a class="link" href="{"../"*bool(phlist)}../../files/images/{link}/{ph}" target="_blank"><img src="{"../"*bool(phlist)}../../files/images/{link}/preview/{ph}" {alt_title()}><ul class="exif">'
)
		info=exif(f'../../images/{link}/{ph}')
		for tag in info:
			if lang=='ru':
				if tag=='Camera':data+=f'<li><div class="tag">Камера</div><div class="value">{info[tag]}</div></li>'
				elif tag=='Lens':data+=f'<li><div class="tag">Объектив</div><div class="value">{info[tag]}</div></li>'
				elif tag=='DateTime':data+=f'<li><div class="tag">Дата и время</div><div class="value">{info[tag]}</div></li>'
				elif tag=='Shutter Speed':data+=f'<li><div class="tag">Выдержка</div><div class="value">{info[tag].replace("s","сек")}</div></li>'
				elif tag=='Aperture':data+=f'<li><div class="tag">Диафрагма</div><div class="value">{info[tag]}</div></li>'
				elif tag=='Focal Length':data+=f'<li><div class="tag">Фокусное расстояние</div><div class="value">{info[tag]}</div></li>'
				else:data+=f'<li><div class="tag">{tag}</div><div class="value">{info[tag]}</div></li>'
			elif lang=='jp':
				if tag=='Camera':data+=f'<li><div class="tag">カメラ</div><div class="value">{info[tag]}</div></li>'
				elif tag=='Lens':data+=f'<li><div class="tag">レンズ</div><div class="value">{info[tag]}</div></li>'
				elif tag=='DateTime':data+=f'<li><div class="tag">日付時刻</div><div class="value">{info[tag]}</div></li>'
				elif tag=='Shutter Speed':data+=f'<li><div class="tag">シャッター速度</div><div class="value">{info[tag]}</div></li>'
				elif tag=='Aperture':data+=f'<li><div class="tag">開口</div><div class="value">{info[tag]}</div></li>'
				elif tag=='Focal Length':data+=f'<li><div class="tag">焦点距離</div><div class="value">{info[tag]}</div></li>'
				else:data+=f'<li><div class="tag">{tag}</div><div class="value">{info[tag]}</div></li>'
			else:data+=f'<li><div class="tag">{tag}</div><div class="value">{info[tag]}</div></li>'
		data+='</ul></a></div>'
	data+=(
'''<!-- Yandex.Metrika counter -->
    <script type="text/javascript" >
       (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
       m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
       (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

       ym(62113489, "init", {
            clickmap:true,
            trackLinks:true,
            accurateTrackBounce:true,
            webvisor:true
       });
    </script>
    <noscript><div><img src="https://mc.yandex.ru/watch/62113489" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
    <!-- /Yandex.Metrika counter -->
</body>
</html>'''
)
	if phlist:
		with open(f'../../../{lang}/photos/date/{name}.html','w',encoding='utf-8')as out:out.write(data)
	else:
		with open(f'../../../{lang}/albums/{link}.html','w',encoding='utf-8')as out:out.write(data)


if __name__=='__main__':
	print('=== GalleryBuilder ===\n © Masahiko AMANO a.k.a. H1K0, 2020')
	while 1:
		print('\n== Let\'s make gallery! ==\nMake manually or from JSON file?\nType anything to build manually or just press ENTER to build from JSON.')
		ans=input()
		if ans:
			print('\n= NEW GALLERY =')
			link=input('Link: ')
			lnth=int(input('Length: '))
			en_name=input('English name:  ')
			ru_name=input('Russian name:  ')
			jp_name=input('Japanese name: ')
			try:
				build(en_name,link,lnth,'en')
				build(ru_name,link,lnth,'ru')
				build(jp_name,link,lnth,'jp')
			except Exception as e:print(e)
			else:print(f'{en_name}: SUCCESS')
		else:
			try:
				from json import loads as load
				with open('../../json/albums.json',encoding='utf-8')as json:albums=load(json.read())
			except Exception as e:
				print(e)
				continue
			for album in albums:
				try:
					build(album["name_en"],album["link"],album["lnth"],'en')
					build(album["name_ru"],album["link"],album["lnth"],'ru')
					build(album["name_jp"],album["link"],album["lnth"],'jp')
				except Exception as e:print(e)
				else:print(f'{album["name_en"]}: SUCCESS')