<?php
	$user = "root";
	$db_host="localhost";
	$pass = "198700*921019";
 	$database=  "tinklapiux";
	$db=mysqli_connect($db_host, $user, $pass, $database) or die("Negalima atidaryti duombazes");
	// Check connection
	if (mysqli_connect_errno()) {
echo "Connected to MySQL<br>";
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}
	$Vardas = mysqli_real_escape_string($db, $_POST['Vardas']);
	$Pavarde = mysqli_real_escape_string($db, $_POST['Pavarde']);
	$Pastas = mysqli_real_escape_string($db, $_POST['Pastas']);
	$slapt = mysqli_real_escape_string($db, $_POST['slapt']);
	$sql="INSERT INTO users VALUES ('$Vardas', '$Pavarde', '$Pastas', '$slapt' )";
	//echo ("Pridetas user $Vardas, $Pavarde ");
	if (!mysqli_query($db,$sql)) {
		die('Error: ' . mysqli_error($db));
	}
	#$db=mysqli_connect("localhost", "root", "$pass", "tinklapiux") or die("Negalima atidaryti duombazes");
	//$Email = mysqli_real_escape_string($db,$_POST["Pastas"]);
	//$result = mysqli_query($db,"SELECT Name FROM users WHERE Mail = '$Pastas'");
		//if($result === TRUE) {
	header('Location: http://localhost/test.html');
	//	}
	
	
	mysqli_close($db);
	
	

?>
