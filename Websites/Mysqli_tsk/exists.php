<?php	
		
	$db=mysqli_connect("localhost", "root", "198700921019", "tinklapiux") or die("Negalima atidaryti duombazes");
	
	if (isset($_GET["q"]) && $_GET["q"]!="") {
		$mail = $_GET["q"];
	}else{
		echo("q undetected");
	}
	$sql = "SELECT name, surname, COUNT(*) as total
		FROM users WHERE mail='$mail'";
	$result2 = mysqli_query($db,$sql);
	if (!$result2) {
		printf("Error: %s\n", mysqli_error($db));
		exit();
	}
	while($row = mysqli_fetch_array($result2)) {
		$kiek1=$row['total'];
		if ($kiek1 > 0){
			echo $row['name']." ".$row['surname'];
		}else{
			echo "false";
		}
	}
	
?>
