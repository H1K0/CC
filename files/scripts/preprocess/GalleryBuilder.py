from EXIFer import exif
from PreviewMaker import make_previews
from os import access,F_OK,mkdir
from os.path import dirname,basename

def build(name,link,lnth,lang,phlist=[]):
	def alt_title():
		if lang=='en':return f'alt="{name} -> Photo #{i+1}" title="{name} -> Photo #{i+1} (Click to view fullsized)"'
		if lang=='ru':return f'alt="{name} -> Фото №{i+1}" title="{name} -> Фото №{i+1} (Кликни, чтобы глянуть фулл)"'
		if lang=='jp':return f'alt="{name} -> 写真第{i+1}枚" title="{name} -> 写真第{i+1}枚（クリックして完全版を見る）"'
	if phlist:
		lnth=len(phlist)
		if lang=='en':title=f'Photos from {name} | H1K0-CC'
		elif lang=='ru':title=f'Фотки от {name} | H1K0-CC'
		else:title=f'{name}の写真 | H1K0-CC'
	else:
		link='albums/'+link
		if lang=='en':title=f'Album «{name}» | Masahiko AMANO a.k.a. H1K0'
		elif lang=='ru':title=f'Альбом «{name}» | Масахико АМАНО a.k.a. H1K0'
		else:title=f'「{name}」写真アルバム | 天人楽彦 a.k.a. H1K0'
	gallery=''
	for i in range(lnth):
		if phlist:
			link=dirname(phlist[i]).replace('../../images/','')
			ph=basename(phlist[i])
		else:ph=str(i+1).rjust(3,"0")+'.jpg'
		full=f'<img src="/files/images/{link}/{ph}" alt="{ph}"><div class="exif"><table>'
		info=exif(f'../../images/{link}/{ph}')
		for tag in info:
			full+='<tr itemprop="exifData" itemscope itemtype="http://schema.org/PropertyValue">'
			if lang=='ru':
				if tag=='Camera':full+=f'<td class="tag" itemprop="name">Камера</td><td class="value" itemprop="value" itemprop="value">{info[tag]}</td>'
				elif tag=='Lens':full+=f'<td class="tag" itemprop="name">Объектив</td><td class="value" itemprop="value">{info[tag]}</td>'
				elif tag=='DateTime':full+=f'<td class="tag" itemprop="name">Дата и время</td><td class="value" itemprop="value">{info[tag]}</td>'
				elif tag=='Resolution':full+=f'<td class="tag" itemprop="name">Разрешение</td><td class="value" itemprop="value">{info[tag]}</td>'
				elif tag=='Shutter Speed':full+=f'<td class="tag" itemprop="name">Выдержка</td><td class="value" itemprop="value">{info[tag].replace("s","сек")}</td>'
				elif tag=='Aperture':full+=f'<td class="tag" itemprop="name">Диафрагма</td><td class="value" itemprop="value">{info[tag]}</td>'
				elif tag=='Focal Length':full+=f'<td class="tag" itemprop="name">Фокусное расстояние</td><td class="value" itemprop="value">{info[tag]}</td>'
				else:full+=f'<td class="tag" itemprop="name">{tag}</td><td class="value" itemprop="value">{info[tag]}</td>'
			elif lang=='jp':
				if tag=='Camera':full+=f'<td class="tag" itemprop="name">カメラ</td><td class="value" itemprop="value">{info[tag]}</td>'
				elif tag=='Lens':full+=f'<td class="tag" itemprop="name">レンズ</td><td class="value" itemprop="value">{info[tag]}</td>'
				elif tag=='DateTime':full+=f'<td class="tag" itemprop="name">日付時刻</td><td class="value" itemprop="value">{info[tag]}</td>'
				elif tag=='Resolution':full+=f'<td class="tag" itemprop="name">解像度</td><td class="value" itemprop="value">{info[tag]}</td>'
				elif tag=='Shutter Speed':full+=f'<td class="tag" itemprop="name">シャッター速度</td><td class="value" itemprop="value">{info[tag]}</td>'
				elif tag=='Aperture':full+=f'<td class="tag" itemprop="name">開口</td><td class="value" itemprop="value">{info[tag]}</td>'
				elif tag=='Focal Length':full+=f'<td class="tag" itemprop="name">焦点距離</td><td class="value" itemprop="value">{info[tag]}</td>'
				else:full+=f'<td class="tag" itemprop="name">{tag}</td><td class="value" itemprop="value">{info[tag]}</td>'
			else:full+=f'<td class="tag" itemprop="name">{tag}</td><td class="value" itemprop="value">{info[tag]}</td>'
			full+='</tr>'
		full+='</table></div></div>'
		gallery+=f'<li class="photo" onclick=\'showfull();document.getElementsByClassName("full")[0].innerHTML=`{full}`\' itemscope itemtype="http://schema.org/ImageObject"><link itemprop="contentUrl" href="/files/images/{link}/{ph}"><img itemprop="thumbnail" src="/files/images/{link}/preview/{ph}" {alt_title()}></li>'

	data=(
f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
	<meta charset="UTF-8">
	<title>{title}</title>
	<link rel="shortcut icon" href="/favicon.png" type="image/png">
	<link rel="stylesheet" href="/files/style/general.css" type="text/css">
	<link rel="stylesheet" href="/files/style/gallery.css" type="text/css">
</head>
<body>
	<header>{name}</header>
	<ul class="gallery">
	{gallery}
	</ul>
	<script type="text/javascript" src="/files/scripts/switch_view.js"></script>
    <div class="full" onclick="hidefull()"></div>
    <!-- Yandex.Metrika counter -->''''''
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
		if not access(f'../../../{lang}/photos/dates/{name[:4]}',F_OK):mkdir(f'../../../{lang}/photos/dates/{name[:4]}')
		if not access(f'../../../{lang}/photos/dates/{name[:4]}/{name[5:7]}',F_OK):mkdir(f'../../../{lang}/photos/dates/{name[:4]}/{name[5:7]}')
		with open(f'../../../{lang}/photos/dates/{name[:4]}/{name[5:7]}/{name[-2:]}.html','w',encoding='utf-8')as out:out.write(data)
	else:
		with open(f'../../../{lang}/photos/{link}.html','w',encoding='utf-8')as out:out.write(data)


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
				make_previews(f'../../images/albums/{link}')
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
					make_previews(f'../../images/albums/{album["link"]}')
				except Exception as e:print(e)
				else:print(f'{album["name_en"]}: SUCCESS')