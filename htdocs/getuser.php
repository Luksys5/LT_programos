<?php
	$db=mysqli_connect("localhost", "root", "", "tinklapiux") or die("Negalima atidaryti duombazes");
	$result = mysqli_query($db,"SELECT * FROM users WHERE Mail='luksys7@yahoo.com'");
	while($row = mysqli_fetch_array($result)) {
	echo $row['Mail'];
	echo "<br>";
	}
	

	

	
	mysqli_close($db);
?>