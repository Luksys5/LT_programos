<?php
	$Name = $_POST['Vardas'];
	$Sname = $_POST['Pavarde'];
	$mail = $_POST['Pastas'];
	$pass = $_POST['slapt'];
	$dbhandle = mysql_connect("localhost", "root", "198700921019") or die("Unable to connect to MySQL");
	$selected = mysql_select_db("tinklapiux", $dbhandle);
	$rez = mysql_query("SELECT * FROM users");
	$exists = 1;
	echo $Name.' '.$Sname.' '.$mail.' '.$pass;
	while($row = mysql_fetch_array($rez)){
		if ( $exists != $row{'id'} ){
			echo 'smth '.$exists." ".$row{'id'}." ";
			$Ins = mysql_query("INSERT INTO users VALUES('$exists', '$Name', '$Sname', '$mail', '$pass', NULL);");
		}       
		$exists += 1;
	}
	$Ins = mysql_query("INSERT INTO users VALUES(NULL, '$Name', '$Sname', '$mail', '$pass', NULL);");
	//echo "<script type='text/javascript'>alert('Your account has been created!');</script>";
	header('Location: http://localhost/VesCalc/Vesiculewebpage.html' );
?>
