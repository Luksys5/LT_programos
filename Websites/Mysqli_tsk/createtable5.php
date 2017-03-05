	<?php
	$user = "root";
	$db_host="localhost";
	$pass = "passm";
 	$database= "tinklapiux";
	$db=mysqli_connect($db_host, $user, $pass, $database) or die("Negalima atidaryti duombazes");
	if (mysqli_connect_errno()) {
		echo "Failed to connect to MySQL: " . mysqli_connect_error();
	}
	echo ' tuscias';
	$Pavadinimas = mysqli_real_escape_string($db, $_POST['Pavadinimas']);
	$laukas1= mysqli_real_escape_string($db, $_POST['Pirmas']);
	$laukas2= mysqli_real_escape_string($db, $_POST['Antras']);
	$laukas3= mysqli_real_escape_string($db, $_POST['Trecias']);
	$laukas4= mysqli_real_escape_string($db, $_POST['Ketvirtas']);
	$laukas5= mysqli_real_escape_string($db, $_POST['Penktas']);
	$sql="SELECT * FROM $Pavadinimas";
	if (mysqli_query($db,$sql))
	{
		echo( 'Stalas tokiu pavadinimu jau egzistuoja');
	}
	else
	{
		$sql="CREATE TABLE $Pavadinimas(
			PID INT NOT NULL AUTO_INCREMENT, 
			PRIMARY KEY(PID),
			$laukas1 CHAR(30),
			$laukas2 CHAR(30),
			$laukas3 CHAR(30),
			$laukas4 CHAR(30),
			$laukas5 CHAR(30))";
	
		if (mysqli_query($db,$sql)) 
		{
			echo "Database $Pavadinimas CREATED successfully";
		}
	}
	mysqli_close($db);
	
?>

	

