<?php

	$user = "root";
	$db_host="localhost";
	$pass = "";
 	$database=  "tinklapiux";
	$db=mysqli_connect($db_host, $user, $pass, $database);
	$username= mysqli_real_escape_string($db, $_POST['username']);
	$password=mysqli_real_escape_string($db, $_POST['password']);
	$sql="SELECT COUNT(*) as total FROM zmones WHERE Vardas='$username'";
	$result=mysqli_query($db,$sql);
	while($row=mysqli_fetch_array($result)){
		$kiek=$row['total'];
	}
	
	
	if (mysqli_connect_errno()) {
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}

?>