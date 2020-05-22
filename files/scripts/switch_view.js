function view(id){
	var elem=document.getElementById(id);
	if (elem.style.display!='block')elem.style.display='block';
	else elem.style.display='none';
}
function showfull(id){
	document.getElementsByTagName('header')[0].style.display='none';
	document.getElementsByClassName('gallery')[0].style.display='none';
	document.getElementsByClassName('full')[id].style.display='flex';
}
function hidefull(id){
	document.getElementsByTagName('header')[0].style.display='block';
	document.getElementsByClassName('gallery')[0].style.display='flex';
	document.getElementsByClassName('full')[id].style.display='none';
}