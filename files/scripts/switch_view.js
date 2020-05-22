function view(id){
	var elem=document.getElementById(id);
	if (elem.style.display!='block')elem.style.display='block';
	else elem.style.display='none';
}
function showfull(){
	document.getElementsByTagName('header')[0].style.display='none';
	document.getElementsByClassName('gallery')[0].style.display='none';
	document.getElementsByClassName('full')[0].style.display='flex';
}
function hidefull(){
	document.getElementsByClassName('full')[0].style.display='none';
	document.getElementsByClassName('full')[0].innerHTML='';
	document.getElementsByTagName('header')[0].style.display='block';
	document.getElementsByClassName('gallery')[0].style.display='flex';
}