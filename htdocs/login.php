<!DOCTYPE html>
<html>
	<head>
		<title>Profile</title>
		<meta charset="utf-8">
		<meta name="description" content="Vartotojas">
		<script src="javascripts/jquery-1.11.1.min.js" type="text/javascript"></script>
	<style type="text/css">
			@import url("login.css");
	</style>
	<script>
	$(document).ready(function(){
		$("#nuotrauka").width($("#img").width);
		$("#Surname").html('labas');
	});
	</script>
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
		<div id="main" class="section">
			<div id="img" >
				<img id="nuotrauka" src="gera.jpg" >	
			</div>
			<div id="profile" >
				<div id = "Name"><h3>Name</h3></div><br>
				<div id = "Surname"><h3>Surame</h3></div><br>
				<div id = "Mail"><h3>Mail</h3></div><br>
				<button id="passw">Change password</button>
				ciaprofke
			</div>
		</div>
		<div>
	</body>
</html>