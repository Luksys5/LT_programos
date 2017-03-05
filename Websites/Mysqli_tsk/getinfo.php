<?php
	
	$db=mysqli_connect("localhost", "root", "", "tinklapiux") or die("Negalima atidaryti duombazes");
	
	if (isset($_GET["Past"]) && $_GET["Past"]!="") {
        $q = $_GET["Past"];
    }else{echo("Past undetected");}
	$result1 = mysqli_query($db,"SELECT Name as name From users WHERE Mail='$q'");
	$result2 = mysqli_query($db,"SELECT Surname as sname From users WHERE Mail='$q'");
	$result3 = mysqli_query($db,"SELECT Mail as mail From users  WHERE Mail='$q'");
	while($row = mysqli_fetch_array($result1)) {
			$Name=$row['name'];
			echo($Name.' ');
	}
	while($row = mysqli_fetch_array($result2)) {
			$Surname=$row['sname'];
			echo($Surname.' ');
	}
	while($row = mysqli_fetch_array($result3)) {
			$Mail=$row['mail'];
			echo($Mail);
	}
	mysqli_close($db);
?>