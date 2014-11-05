<?php
				$db=mysqli_connect("localhost", "root", "", "tinklapiux") or die("Negalima atidaryti duombazes");
				$Email = mysqli_real_escape_string($db,$_POST["Pastas"]);
				$result = mysqli_query($db,"SELECT Name FROM users WHERE Mail = '$Email'");
				if($result === FALSE) {
				echo($Email);
				die(mysql_error()); // TODO: better error handling
				}
				while($row = mysqli_fetch_array($result)) {
					echo($row['Name']);
				}
?>