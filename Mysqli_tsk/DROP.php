<?php
	$user = "root";
	$db_host="localhost";
	$pass = "passm";
 	$database=  "tinklapiux";
	$db=mysqli_connect($db_host, $user, $pass, $database) or die("Negalima atidaryti duombazes");
	$index = mysqli_real_escape_string($db, $_POST['Trinti']);
	$sql ="DROP TABLE $index";
	if (mysqli_query($db,$sql)){
		echo("Istryniau Stala:$index");
	}
	else{
		$sql="SELECT * as total FROM INFORMATION_SCHEMA.TABLES";
		$result2= mysqli_query($db,"SELECT count(*) as total1 FROM zmones WHERE Vardas like '$index'");
		while($row = mysqli_fetch_array($result2)) {
			$kiek1=$row['total1'];
			echo "labas<br>";
		}
	}
	mysqli_close($db);
?>
