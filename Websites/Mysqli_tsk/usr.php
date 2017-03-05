<?php
$Name = $_POST['name'];
$Sname = $_POST['surname'];
$mail = $_POST['mail'];
$pass = $_POST['passw'];
$dbhandle = mysql_connect("localhost", "root", "passm") or die("Unable to connect to MySQL");
$selected = mysql_select_db("tinklapiux", $dbhandle);
$rez = mysql_query("SELECT * FROM users");
$exists = 1;
echo $Name.' '.$Sname.' '.$mail.' '.$pass;
while($row = mysql_fetch_array($rez)){
	if ( $exists != $row{'id'} ){
	echo 'smth '.$exists." ".$row{'id'}." ";
		$Ins = mysql_query("INSERT INTO users VALUES('$exists', '$Name', '$Sname', '$mail', '$pass', NULL);");
		exit;
	}	
	$exists += 1;
}
#$Ins = mysql_query("INSERT INTO users VALUES( NULL, '$Name', '$Sname', '$mail', '$pass', NULL);");

#		$Ins = mysql_query("INSERT INTO users VALUES('$exists', '$Name', '$Sname', '$mail', '$pass', NULL);");
#		#exit;
#	}else{
#		$cc += 1	
#	}	
#	$exists += 1;	
	
}
##echo " ".$exists;
#if($exists == 0){
#	$Ins = mysql_query("INSERT INTO users VALUES(NULL, '$Name', '$Sname', '$mail', '$pass', NULL);");
#}
#while($row = mysql_fetch_array($rez)){
#	echo $row{'user_id'};
#	echo $row{'user_mail'};
##}
#header('Location: del_usr.html');
?>
