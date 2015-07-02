<?php
	header("Access-Control-Allow-Origin: http://localhost/admin.html");
	$user = "root";
	$db_host="localhost";
	$pass = "";
 	$database=  "tinklapiux";
	$db=mysqli_connect($db_host, $user, $pass, $database) or die("Negalima atidaryti duombazes"); 

	$result1 = mysqli_query($db,"SHOW TABLES");
	while($row = mysqli_fetch_assoc($result1)) {
		foreach($row as $value){
			echo $value . '<hr>';
		}
	}
	mysqli_close($db);
?>