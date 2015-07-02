<?php
$id = $_POST['id'];
echo $id." istrintas";
$dbhandle = mysql_connect("localhost", "root", "passm") or die("Unable to connect to MySQL");
$selected = mysql_select_db("tinklapiux", $dbhandle);
$Ins = mysql_query("DELETE FROM users WHERE user_id = $id;");
#if (!mysqli_query($db, $sql)){
#	die('Exists'.mysqli_error($db));
#}

#while($row = mysql_fetch_array($rez)){
#	echo $row{'user_id'};
#	echo $row{'user_mail'};
#}
?>
