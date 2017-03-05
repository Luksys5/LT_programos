<!DOCTYPE html>
<html>
	<head>
		<title>Profile</title>
		<meta charset="utf-8">
		<meta name="description" content="Vartotojas">
		<script src="javascripts/jquery-1.11.1.js" type="text/javascript"></script>
	<style type="text/css">
			@import url("login.css");
	</style>
	<script>
		function hideme(){
			$("#profile").hide();
		}
	</script>
	<script>
	function toggleVisibility(newSection) {
		//$(".section").not("#" + newSection).hide();
		$("#" + newSection).show();
	}
	</script>
	</head>
	<body > 
		
		<div id="top">
			<h1>
				<img id="linei" src="whitegrey.jpg">
				<div id="title">Vesicules base background</div>
				<div id="user">
				<?php
				// $db=mysqli_connect("localhost", "root", "", "tinklapiux") or die("Negalima atidaryti duombazes");
				// $Email = mysqli_real_escape_string($db,$_POST["Pastas"]);
				// $result = mysqli_query($db,"SELECT Name, Surname FROM users WHERE Mail = '$Email'");
				// if($result === FALSE) {
					// echo($Email);
					// die(mysql_error()); // TODO: better error handling
				// }
				// while($row = mysqli_fetch_array($result)) {
					// echo($row['Name']." ".$row['Surname']);
				// }
				// 
				?>
				</div>
				<img id="topi" src="Grey.jpg">
				
			</h1>
		</div>
		<img id="linei2" src="whitegrey.jpg">
		<div id="left">
			<table cellpadding="3" cellspacing="3" border="3">
				<tr><td><a href="" style="text-decoration: none;color: black;">Main</a></td></tr>
				<tr><td><a href="" onclick = "toggleVisibility('profile');" style="text-decoration: none;color: black;">Profile</a></td></tr>
				<tr><td><a href="" onclick = "hideme();" style="text-decoration: none;color: black;">Information</a></td></tr>
				<tr><td><a href="" style="text-decoration: none;color: black;">Support</a></td></tr>
			</table>
		</div>
		<img id="lefti" src="white.jpg">
		<div id="main" class="section"></div>
		<div id="profile" >
			<img id="nuotrauka" src="gera.jpg">	
			<div id = "Name"><h3>Name</h3></div>
			<div id = "Surname"></div>
			<div id = "Mail"></div>
			<button id="passw">Change password</button>
			ciaprofke
		</div>
		<div>
	</body>
</html>
