switch={
	"MyName":{
		"en":"Masahiko AMANO",
		"ru":"Масахико АМАНО",
		"jp":"天人楽彦"
	},
	"Track":{
		"en":"Track",
		"ru":"Трек",
		"jp":"曲"
	},
	"Compil":{
		"en":"Compil",
		"ru":"Компил",
		"jp":"更集"
	},
	"Album":{
		"en":"Album",
		"ru":"Альбом",
		"jp":"収録"
	},
	"Info":{
		"en":"Info",
		"ru":"Инфа",
		"jp":"詳細"
	},
	"Original":{
		"en":"Original",
		"ru":"Оригинал",
		"jp":"原作"
	},
	"Order":{
		"en":"Ordered by",
		"ru":"Заказчик",
		"jp":"注文"
	},
	"ScriptWriter":{
		"en":"Scriptwriter",
		"ru":"Автор текста",
		"jp":"脚本家"
	},
	"Composition":{
		"en":"Composition",
		"ru":"Композиция",
		"jp":"作曲"
	},
	"Arrangement":{
		"en":"Arrangement",
		"ru":"Аранжировка",
		"jp":"編曲"
	},
	"Guitar":{
		"en":"Guitar",
		"ru":"Гитара",
		"jp":"ギター"
	},
	"Piano":{
		"en":"Piano",
		"ru":"Фортепиано",
		"jp":"ピアノ"
	},
	"Bayan":{
		"en":"Bayan",
		"ru":"Баян",
		"jp":"バヤン"
	},
	"Programming":{
		"en":"Programming",
		"ru":"Сводка",
		"jp":"プログラミング"
	},
	"Lyricist":{
		"en":"Lyrics",
		"ru":"Текст песенки",
		"jp":"作詞"
	},
	"CoverDesign":{
		"en":"Cover design",
		"ru":"Дизайн обложки",
		"jp":"カバーデザイン"
	},
	"Vocals":{
		"en":"Vocals",
		"ru":"Вокал",
		"jp":"ボーカル"
	},
	"Reading":{
		"en":"Reading",
		"ru":"Текст читает",
		"jp":"読み上げ"
	},
	"Key":{
		"en":"Key",
		"ru":"Тональность",
		"jp":"調号"
	},
	"BPM":{
		"en":"BPM",
		"ru":"BPM",
		"jp":"BPM"
	},
	"PubDate":{
		"en":"Publication date",
		"ru":"Дата публикации",
		"jp":"投稿年月日"
	},
	"Description":{
		"en":"Description",
		"ru":"Описание",
		"jp":"説明文"
	},
	"Tracklist":{
		"en":"Tracklist",
		"ru":"Треклист",
		"jp":"曲リスト"
	},
	"Lyrics":{
		"en":"Lyrics",
		"ru":"Текст песенки",
		"jp":"歌詞"
	},
	"dur":{
		"en":"-dur",
		"ru":"-мажор",
		"jp":"長調"
	},
	"moll":{
		"en":"-moll",
		"ru":"-минор",
		"jp":"短調"
	},
	"KeyCode":{
		"c":{
			"en":"c",
			"ru":"до",
			"jp":"ハ"
		},
		"cis":{
			"en":"cis",
			"ru":"до-диез",
			"jp":"嬰ハ"
		},
		"des":{
			"en":"des",
			"ru":"ре-бемоль",
			"jp":"変ニ"
		},
		"d":{
			"en":"d",
			"ru":"ре",
			"jp":"ニ"
		},
		"dis":{
			"en":"dis",
			"ru":"ре-диез",
			"jp":"嬰ニ"
		},
		"es":{
			"en":"es",
			"ru":"ми-бемоль",
			"jp":"変ホ"
		},
		"e":{
			"en":"e",
			"ru":"ми",
			"jp":"ホ"
		},
		"f":{
			"en":"f",
			"ru":"фа",
			"jp":"ヘ"
		},
		"fis":{
			"en":"fis",
			"ru":"фа-диез",
			"jp":"嬰ヘ"
		},
		"ges":{
			"en":"ges",
			"ru":"соль-бемоль",
			"jp":"変ト"
		},
		"g":{
			"en":"g",
			"ru":"соль",
			"jp":"ト"
		},
		"gis":{
			"en":"gis",
			"ru":"соль-диез",
			"jp":"嬰ト"
		},
		"as":{
			"en":"as",
			"ru":"ля-бемоль",
			"jp":"変イ"
		},
		"a":{
			"en":"a",
			"ru":"ля",
			"jp":"イ"
		},
		"b":{
			"en":"b",
			"ru":"си-бемоль",
			"jp":"変ロ"
		},
		"h":{
			"en":"h",
			"ru":"си",
			"jp":"ロ"
		}
	}
}

def lyrtable(lyrics,lang):
	lyrlang=lyrics['lang']
	if lang not in lyrics:lang='en'
	out='<table>'
	lyrics[lyrlang]=lyrics[lyrlang].split('\n')
	if lyrlang==lang:
		for line in lyrics[lyrlang]:
			out+='<tr><t'
			if line[0]=='>':out+=f'h>{line[1:]}</th'
			else:out+=f'd>{line}</td'
			out+='></tr>'
	elif 'romaji' in lyrics:
		lyrics['romaji']=lyrics['romaji'].split('\n')
		lyrics[lang]=lyrics[lang].split('\n')
		for orig,roma,trsl in [(lyrics[lyrlang][i],lyrics['romaji'][i],lyrics[lang][i])for i in range(len(lyrics[lyrlang]))]:
			out+='<tr><t'
			if orig==roma==trsl:
				if orig[0]=='>':out+=f'h class="original" colspan="3">{orig[1:]}</th'
				else:out+=f'd class="original" colspan="3">{orig}</td'
			elif orig==roma:
				if orig[0]=='>':out+=f'h class="original" colspan="2">{orig[1:]}</th'
				else:out+=f'd class="original" colspan="2">{orig}</td'
				out+='><t'
				if trsl[0]=='>':out+=f'h class="translation">{trsl[1:]}</th'
				else:out+=f'd class="translation">{trsl}</td'
			else:
				if orig[0]=='>':out+=f'h class="original">{orig[1:]}</th'
				else:out+=f'd class="original">{orig}</td'
				out+='><t'
				if roma[0]=='>':out+=f'h class="romaji">{roma[1:]}</th'
				else:out+=f'd class="romaji">{roma}</td'
				out+='><t'
				if trsl[0]=='>':out+=f'h class="translation">{trsl[1:]}</th'
				else:out+=f'd class="translation">{trsl}</td'
			out+='></tr>'
	else:
		lyrics[lang]=lyrics[lang].split('\n')
		for orig,trsl in [(lyrics[lyrlang][i],lyrics[lang][i])for i in range(len(lyrics[lyrlang]))]:
			out+='<tr><t'
			if orig==trsl:
				if orig[0]=='>':out+=f'h class="original" colspan="2">{orig[1:]}</th'
				else:out+=f'd class="original" colspan="2">{orig}</td'
			else:
				if orig[0]=='>':out+=f'h class="original">{orig[1:]}</th'
				else:out+=f'd class="original">{orig}</td'
				out+='><t'
				if trsl[0]=='>':out+=f'h class="translation">{trsl[1:]}</th'
				else:out+=f'd class="translation">{trsl}</td'
			out+='></tr>'
	out+='</table>'
	return out

def build_page(typ,ID,data,lang):
	global switch
	def alt(tag):
		if tag=='audio':
			if lang=='en':return f'Listen to <strong>«{data["Name"]}»</strong> <a href="{data["ReserveLink"]}" target="_blank">here</a>.'
			elif lang=='ru':return f'Слушать <strong>«{data["Name"]}»</strong> <a href="{data["ReserveLink"]}" target="_blank">здесь</a>.'
			elif lang=='jp':return f'<strong>「{data["Name"]}」</strong>を<a href="{data["ReserveLink"]}" target="_blank">聞く</a>。'
		elif tag=='img':
			if lang=='en':return f'«{data["Name"]}» — {switch[typ][lang]} Cover (Click to view fullsized)'
			elif lang=='ru':return f'«{data["Name"]}» — Обложка {switch[typ][lang]}а (Клик, чтобы глянуть фулл)'
			elif lang=='jp':return f'「{data["Name"]}」{switch[typ][lang]}カバー（クリックして完全版を見る）'
	# Generating title
	title=''
	if lang in ('en','ru'):title=f'{switch[typ][lang]} «{data["Name"]}»'
	elif lang=='jp':title=f'「{data["Name"]}」{switch[typ][lang]}'
	# Generating header
	header=''
	feat=''
	if 'Feat' in data:feat=f' <i>[feat. {data["Feat"]}]</i>'
	if lang in ('en','ru'):header=f'{switch[typ][lang]} <h1>«{data["Name"]}{feat}»</h1>'
	elif lang=='jp':header=f'<strong>「{data["Name"]}{feat}」</strong>{switch[typ][lang]}'
	# Generating <audio>
	audio=''
	if typ=='Track':
		audio=(
	f'''<audio class="content-audio" controls{" loop"*("Loop" in data)}>
          <source src="/files/audio/mp3/{ID}.mp3" type="audio/mpeg">
          {alt("audio")}
        </audio><hr>'''
)
	# Generating info
	info='<table>'
	for tag in data:
		if tag not in ('Name','ReserveLink','Feat','Key','Description','Tracklist','CoverID','Lyrics','Loop') and (tag!='Key' or lang=='en'):
			info+=f'<tr><td class="tag">{switch[tag][lang]}</td><td>{data[tag]}'
			if tag=='Key':
				if data[tag][0].isupper():info+='-dur'
				else:info+='-moll'
			info+='</td></tr>'
		elif tag=='Key' and lang!='en':
			if data[tag][0].isupper():mode='dur'
			else:mode='moll'
			info+=f'<tr><td class="tag">{switch[tag][lang]}</td><td>{switch["KeyCode"][data[tag].lower()][lang]}{switch[mode][lang]}</td></tr>'
	info+='</table>'
	if 'Description' in data:
		info+=f'<h3>{switch["Description"][lang]}</h3><div class="description">'
		if lang in data["Description"]:info+=data["Description"][lang]
		else:info+=data["Description"]["en"]
		info+='</div>'
	# Generating tracklist
	tracklist=''
	if 'Tracklist' in data:
		global json
		tracklist+=f'<hr><h2>{switch["Tracklist"][lang]}</h2><ol class="tracklist">'
		for track in data['Tracklist']:
			tracklist+='<li><a href="'
			if 'ExternalLink' in json['Tracks'][track]:tracklist+=json['Tracks'][track]['ExternalLink']
			else:tracklist+=f'../tracks/{track}'
			tracklist+=f'" target="_blank">{json["Tracks"][track]["Name"]}</a></li>'
	# Embedding cover
	if 'CoverID' in data:coverid=data['CoverID']
	else:coverid=ID
	cover=f'<hr><a href="/files/images/music/{coverid}.jpg" target="_blank"><img class="content-image" src="/files/images/music/preview/{coverid}.jpg" alt="{alt("img")}" title="{alt("img")}"></a>'
	# Generating lyrics
	lyrics=''
	if 'Lyrics' in data:
		lyrics=f'<hr><div class="lyrics"><h2>{switch["Lyrics"][lang]}</h2>'+lyrtable(data['Lyrics'].copy(),lang)+'</div>'
	# COMPLETED
	with open(f'../../../{lang}/music/{typ.lower()}s/{ID}.html','w',encoding='utf-8')as out:out.write(
f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <title>{title} | H1K0-CC</title>
  <link rel="shortcut icon" href="/favicon.png" type="image/png">
  <link rel="stylesheet" href="/files/style/general.css" type="text/css">
  <link rel="stylesheet" href="/files/style/content-page.css" type="text/css">
</head>
<body>
  <header>{header}</header>

  <div class="container">
    {audio}
    <div class="info">
      <h2>{switch["Info"][lang]}</h2>
      {info}
      {tracklist}
      {cover}
    </div>
    {lyrics}
  </div>

  <footer>
    © {switch["MyName"][lang]} a.k.a. H1K0, 2020''''''
    <!-- Yandex.Metrika counter -->
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
  </footer>
</body>
</html>'''
)


if __name__=='__main__':
	input('Press ENTER to start. ')
	from json import loads as load
	print('Loading JSON...')
	with open('../../json/music.json',encoding='utf-8')as file:json=load(file.read())
	print('Building track pages...')
	for ID in json["Tracks"]:
		if 'ExternalLink' in json['Tracks'][ID]:continue
		print(f'Track: {ID}:',end=' ')
		build_page('Track',ID,json["Tracks"][ID],'en')
		build_page('Track',ID,json["Tracks"][ID],'ru')
		build_page('Track',ID,json["Tracks"][ID],'jp')
		print('SUCCESS')
	print('Building compil pages...')
	for ID in json["Compils"]:
		print(f'Compil: {ID}:',end=' ')
		build_page('Compil',ID,json["Compils"][ID],'en')
		build_page('Compil',ID,json["Compils"][ID],'ru')
		build_page('Compil',ID,json["Compils"][ID],'jp')
		print('SUCCESS')
	print('Building album pages...')
	for ID in json["Albums"]:
		print(f'Album: {ID}:',end=' ')
		build_page('Album',ID,json["Albums"][ID],'en')
		build_page('Album',ID,json["Albums"][ID],'ru')
		build_page('Album',ID,json["Albums"][ID],'jp')
		print('SUCCESS')
	print('Building music homepages...')
	# Generating the full list
	lst=''
	for track in json["Tracks"]:
		if 'CoverLink' in json["Tracks"][track]:cover=json["Tracks"][track]['CoverLink']
		elif 'CoverID' in json["Tracks"][track]:cover=f'/files/images/music/preview/{json["Tracks"][track]["CoverID"]}.jpg'
		else:cover=f'/files/images/music/preview/{track}.jpg'
		if 'ExternalLink' in json["Tracks"][track]:url=json["Tracks"][track]['ExternalLink']
		else:url=f'music/tracks/{track}'
		lst+=f'<li class="track-card" style="background-image: url({cover})"><a href="{url}" target="_blank"><h3>{json["Tracks"][track]["Name"]}</h3>'
		if 'Feat' in json["Tracks"][track]:lst+=f'<h4>[feat. {json["Tracks"][track]["Feat"]}]</h4>'
		lst+='</a></li>'
	# Generating the list of compils
	compils=''
	for compil in json["Compils"]:compils+=f'<li class="track-card" style="background-image: url(/files/images/music/preview/{compil}.jpg)"><a href="music/compils/{compil}" target="_blank"><h3>{json["Compils"][compil]["Name"]}</h3></a></li>'
	# Generating the list of albums
	albums=''
	for album in json["Albums"]:albums+=f'<li class="track-card" style="background-image: url(/files/images/music/preview/{album}.jpg)"><a href="music/albums/{album}" target="_blank"><h3>{json["Albums"][album]["Name"]}</h3></a></li>'
	with open('../../../en/music.html','w',encoding='utf-8')as file:file.write(
f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>MUSIC | H1K0-CC</title>
  <link rel="shortcut icon" href="/favicon.png" type="image/png">
  <link rel="stylesheet" href="/files/style/general.css" type="text/css">
  <link rel="stylesheet" href="/files/style/home-page.css" type="text/css">
  <link rel="stylesheet" href="/files/style/music-page.css" type="text/css">
  <meta name="description" content="Let's listen to H1K0's music!">
  <meta name="keywords" content="Masahiko AMANO, H1K0, creation, music, composer, arranger, musician, bitmaker, DJ">
  <meta name="copyright" lang="en" content="Masahiko AMANO a.k.a. H1K0">
</head>
<body>
  <header>
    <nav>
      <a class="navbar" href="..">Home</a>
      <a class="navbar" href="profile">Profile</a>
      <div class="navbar active">
        Creations
        <ul class="navlist">
          <li class="navlist-item active"><a href>Music</a></li>
          <li class="navlist-item"><a href="photos">Photos</a></li>
          <li class="navlist-item"><a href="videos">Videos</a></li>
          <li class="navlist-item"><a href="articles">Articles</a></li>
          <li class="navlist-item"><a href="novels">Novels</a></li>
        </ul>
      </div>
    </nav>
    <img class="logo" src="/files/images/logo.svg" alt="H1K0 LOGO">
  </header>

  <div class="block">
  	<h1>All tracks</h1>
  	<ul class="section">
  	  {lst}
  	</ul>
  </div>
  <div class="block">
  	<h1>Compils</h1>
  	<p><strong>So, what compil(ation)s exactly are?</strong> Well, just like musical albums but periodically updated with new tracks.</p>
  	<ul class="section">
  	  {compils}
  	</ul>
  </div>
  <div class="block">
  	<h1>Albums</h1>
  	<ul class="section">
  	  {albums}
  	</ul>
  </div>
''''''
  <footer>
    <div class="flags-box">
      <a class="flag en" href title="English"></a>
      <a class="flag ru" href="../ru/music" title="Русский"></a>
      <a class="flag jp" href="../jp/music" title="日本語"></a>
    </div>
    <h3>© Masahiko AMANO a.k.a. H1K0, 2020</h3>
    <!-- Yandex.Metrika counter -->
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
  </footer>
</body>
</html>'''
)
	with open('../../../ru/music.html','w',encoding='utf-8')as file:file.write(
f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>МУЗЛИШКО | H1K0-CC</title>
  <link rel="shortcut icon" href="/favicon.png" type="image/png">
  <link rel="stylesheet" href="/files/style/general.css" type="text/css">
  <link rel="stylesheet" href="/files/style/home-page.css" type="text/css">
  <link rel="stylesheet" href="/files/style/music-page.css" type="text/css">
  <meta name="description" content="Погнали слушать музлишко H1K0!">
  <meta name="keywords" content="Масахико АМАНО, H1K0, творчество, шедевры, музыка, музлишко, композитор, аранжировщик, битмейкер">
  <meta name="copyright" lang="ru" content="Масахико АМАНО a.k.a. H1K0">
</head>
<body>
  <header>
    <nav>
      <a class="navbar" href=".">Домик</a>
      <a class="navbar" href="profile">Профиль</a>
      <div class="navbar active">
        Шедевры
        <ul class="navlist">
          <li class="navlist-item active"><a href>Музлишко</a></li>
          <li class="navlist-item"><a href="photos">Фотки</a></li>
          <li class="navlist-item"><a href="videos">Видосы</a></li>
          <li class="navlist-item"><a href="articles">Статейки</a></li>
          <li class="navlist-item"><a href="novels">Новеллы</a></li>
        </ul>
      </div>
    </nav>
    <img class="logo" src="/files/images/logo.svg" alt="H1K0 LOGO">
  </header>

  <div class="block">
  	<h1>Все треки</h1>
  	<ul class="section">
  	  {lst}
  	</ul>
  </div>
  <div class="block">
  	<h1>Компилы</h1>
  	<p><strong>Да кто такие эти ваши компилы?</strong> А это как альбомы, только периодически обновляющиеся и пополняющиеся новым музлишком.</p>
  	<ul class="section">
  	  {compils}
  	</ul>
  </div>
  <div class="block">
  	<h1>Альбомы</h1>
  	<ul class="section">
  	  {albums}
  	</ul>
  </div>
''''''
  <footer>
    <div class="flags-box">
      <a class="flag en" href="../en/music" title="English"></a>
      <a class="flag ru" href title="Русский"></a>
      <a class="flag jp" href="../jp/music" title="日本語"></a>
    </div>
    <h3>© Масахико АМАНО a.k.a. H1K0, 2020</h3>
    <!-- Yandex.Metrika counter -->
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
  </footer>
</body>
</html>'''
)
	with open('../../../jp/music.html','w',encoding='utf-8')as file:file.write(
f'''<!DOCTYPE html>
<html lang="jp">
<head>
  <meta charset="UTF-8">
  <title>音楽 | H1K0-CC</title>
  <link rel="shortcut icon" href="/favicon.png" type="image/png">
  <link rel="stylesheet" href="/files/style/general.css" type="text/css">
  <link rel="stylesheet" href="/files/style/home-page.css" type="text/css">
  <link rel="stylesheet" href="/files/style/music-page.css" type="text/css">
  <meta name="description" content="H1K0の音楽を聞こう！">
  <meta name="keywords" content="天人楽彦, H1K0, 作品, 俺サく, 音楽, 曲, 作曲家, 編曲家, 音楽家">
  <meta name="copyright" lang="jp" content="天人楽彦 a.k.a. H1K0">
</head>
<body>
  <header>
    <nav>
      <a class="navbar" href=".">ホーム</a>
      <a class="navbar" href="profile">プロフィール</a>
      <div class="navbar active">
        俺サく
        <ul class="navlist">
          <li class="navlist-item active"><a href>音楽</a></li>
          <li class="navlist-item"><a href="photos">写真</a></li>
          <li class="navlist-item"><a href="videos">動画</a></li>
          <li class="navlist-item"><a href="articles">記事</a></li>
          <li class="navlist-item"><a href="novels">小説</a></li>
        </ul>
      </div>
    </nav>
    <img class="logo" src="/files/images/logo.svg" alt="H1K0 LOGO">
  </header>

  <div class="block">
  	<h1>全曲</h1>
  	<ul class="section">
  	  {lst}
  	</ul>
  </div>
  <div class="block">
  	<h1>更集</h1>
  	<p><strong>さて、更集って何だろう？</strong>それはさ、時々<big>更</big>新されてる音楽収<big>集</big>のことだ。</p>
  	<ul class="section">
  	  {compils}
  	</ul>
  </div>
  <div class="block">
  	<h1>収録</h1>
  	<ul class="section">
  	  {albums}
  	</ul>
  </div>
''''''
  <footer>
    <div class="flags-box">
      <a class="flag en" href="../en/music" title="English"></a>
      <a class="flag ru" href="../ru/music" title="Русский"></a>
      <a class="flag jp" href title="日本語"></a>
    </div>
    <h3>© 天人楽彦 a.k.a. H1K0, 2020</h3>
    <!-- Yandex.Metrika counter -->
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
  </footer>
</body>
</html>'''
)
	print('=== COMPLETED ===')