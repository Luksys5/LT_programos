<?php
	$user = "root";
	$db_host="localhost";
	$pass = "";
 	$database=  "tinklapiux";
	$db=mysqli_connect($db_host, $user, $pass, $database) or die("Negalima atidaryti duombazes");
	$index = mysqli_real_escape_string($db, $_POST['Trinti']);
	$kuris = mysqli_real_escape_string($db, $_POST['duom']);
	$result = mysqli_query($db,"SELECT count(*) as total FROM zmones WHERE Vardas='$index'");
	$perdaug=0;
	while($row = mysqli_fetch_array($result)) {
		if ($row['total'] >1){ 
			$kiek=$row['total'];
		}
	echo "<br>";
	}
	if ($kiek>1){
		echo($index . ' Rasta ' . $kiek. ' kartus.<br> Rinkis pagal kita indeksa ');
	}
	else{
		if ($kuris=="V"){
			mysqli_query($db,"DELETE FROM zmones WHERE Vardas='$index'");
			echo("Istryniau Varda: $index");
		}
		if ($kuris=="P"){
			mysqli_query($db,"DELETE FROM zmones WHERE Pavarde='$index'");
			echo("Istryniau Pavarde: $index");
		}
		if ($kuris=="G"){
			mysqli_query($db,"DELETE FROM zmones WHERE Gimimo_data='$index'");
			echo("Istryniau Gimimo_data: $index");
		}
	}
	mysqli_close($db);
?>