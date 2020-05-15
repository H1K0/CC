window.onload=function(){
	var body_content=`<header>${title}</header><input class="back-btn" type="button" onclick="history.back();" `
	if (lang=='en') body_content+=`value="Back"/>`;
	else if (lang=='ru') body_content+=`value="Назад"/>`;
	else if (lang=='jp') body_content+=`value="戻る"/>`;
	for (let i = 1; i <= len; i++) {
		body_content+=`<div class="photo"><a href="../../files/images/albums/${link}/${(i<100)?'0':''}${(i<10)?'0':''}${i}.jpg" target="_blank"><img src="../../files/images/albums/${link}/preview/${(i<100)?'0':''}${(i<10)?'0':''}${i}.jpg" `;
		if (lang=='en') body_content+=`alt="${title}: Photo #${i}" title="${title}: Photo #${i} (Click to view fullsized)"></a></div>`;
		else if (lang=='ru') body_content+=`alt="${title}: Фото №${i}" title="${title}: Фото №${i} (Кликни, чтобы глянуть фулл)"></a></div>`;
		else if (lang=='jp') body_content+=`alt="${title}: 第${i}写真" title="${title}: 第${i}写真（クリックして完全版を見る）"></a></div>`;
	}
	document.body.innerHTML=body_content;
};