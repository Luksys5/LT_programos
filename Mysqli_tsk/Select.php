<?php
	$db=mysqli_connect("localhost", "root", "", "tinklapiux") or die("Negalima atidaryti duombazes");
	$result = mysqli_query($db,"SELECT * FROM zmones WHERE Vardas='Lukas'");
	while($row = mysqli_fetch_array($result)) {
	echo $row['Vardas'];
	echo "<br>";
	}

	mysqli_close($db);

?>