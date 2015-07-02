<?php
	$user = "root";
	$db_host="localhost";
	$pass = "";
 	$database=  "tinklapiux";
	$db=mysqli_connect($db_host, $user, $pass, $database) or die("Negalima atidaryti duombazes");
	$vardas = mysqli_real_escape_string($db, $_POST['Keisti']);
	$vardas1 = mysqli_real_escape_string($db, $_POST['Ka']);
	$pavarde = mysqli_real_escape_string($db, $_POST['Keisti1']);
	$pavarde1 = mysqli_real_escape_string($db, $_POST['Ka1']);
	
	$result1 = mysqli_query($db,"SELECT count(*) as total1 FROM zmones WHERE Vardas='$vardas'");
	$result2= mysqli_query($db,"SELECT count(*) as total2 FROM zmones WHERE Vardas='$pavarde'");
	while($row = mysqli_fetch_array($result1)) {
		$kiek1=$row['total1'];
	}
	while($row = mysqli_fetch_array($result2)) {
		$kiek2=$row['total2'];	
	echo "<br>";
	}
	if ($kiek1>1 || $kiek2>1){
		if (!isset($_POST['keist1']) && !isset($_POST['keist2'])) {
		echo('Keisdami uzrasykite ir kita indeksa');
		}
	}
	else{
		if (isset($_POST['keist1'])) {
		
			mysqli_query($db,"UPDATE zmones SET Vardas='$vardas'
			WHERE Vardas='$vardas1'");
			echo($vardas.' pakeistas i '.$vardas1 );
			echo "<br>";
		}
		if (isset($_POST['keist2'])) {
		
			mysqli_query($db,"UPDATE zmones SET Pavarde='$pavarde'
			WHERE Pavarde='$pavarde1'");
			echo($pavarde.' pakeista i ' . $pavarde1);
			echo "<br>";
		}
	}
	if (isset($_POST['keist1']) && isset($_POST['keist2'])) {
		mysqli_query($db,"UPDATE zmones SET Vardas='$vardas'
		WHERE Vardas='$vardas1'");
		echo($vardas.' pakeistas i '.$vardas1 );
		echo "<br>";
		mysqli_query($db,"UPDATE zmones SET Pavarde='$pavarde'
		WHERE Pavarde='$pavarde1'");
		echo($pavarde.' pakeista i ' . $pavarde1);
	}
		
	
	mysqli_close($db);
?>
