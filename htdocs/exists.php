<?php
	
	$db=mysqli_connect("localhost", "root", "", "tinklapiux") or die("Negalima atidaryti duombazes");
	
	if (isset($_GET["q"]) && $_GET["q"]!="") {
        $q = $_GET["q"];
    }else{echo("q undetected");}
	$result2 = mysqli_query($db,"SELECT count(*) as total FROM users WHERE Mail='$q'");
	if (!$result2) {
		printf("Error: %s\n", mysqli_error($db));
		exit();
	}
	while($row = mysqli_fetch_array($result2)) {
			$kiek1=$row['total'];
			if ($kiek1 >0){
				echo "true";
			}else{
				echo "false";
			}
	}
	
	
	mysqli_close($db);
?>