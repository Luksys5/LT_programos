function setCookie(cname, cvalue) {
	var d = new Date();
    d.setTime(d.getTime() + (3600*1000));
	var expires = "; expires=" + d.toGMTString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
}
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) != -1) return c.substring(name.length, c.length);
    }
    return null;
}
function add(name,value){
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0){ c = c.substring(nameEQ.length,c.length);
			value = c+','+value;
			setCookie(name,value)
			return c;
		}
		else c="add bullshit";
	}
	return c;
}
function checkCookie(name,value) {
	if(getCookie(name) == null){setCookie(name,value);
	}else{
		var drink = add(name,value);
	}
}
function delCookie(name){
	value = getCookie(name);
	document.cookie = name + "=" + value + ";expires=Thu, 01 Jan 1970 00:00:01 GMT"; 
}
