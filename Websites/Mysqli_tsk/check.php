<?php	
		
	$db=mysqli_connect("localhost", "root", "198700921019", "tinklapiux") or die("Negalima atidaryti duombazes");
	$sql = "SELECT name FROM users ";
	$rez = mysqli_query($db, $sql);
	while( $row = mysqli_fetch_array($rez) ){
		echo $row['name']."\n";
	}	
	
	mysqli_close($db);
?>
