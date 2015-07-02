	<?php
	$user = "root";
	$db_host="localhost";
	$pass = "";
 	$database=  "tinklapiux";
	$db=mysqli_connect($db_host, $user, $pass, $database) or die("Negalima atidaryti duombazes");
	if (mysqli_connect_errno()) {
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}

	mysqli_query($db,"CREATE TABLE Zmones(
			ID int,
			username varchar(255),
			password varchar(255),
			ElPastas varchar(255)
			);");
	if( mysqli_query($db,"SELECT * FROM Persons")!=null){
		echo ("Prideta Dbz");
	}

	
	
	mysqli_close($db);
	
	

?>
