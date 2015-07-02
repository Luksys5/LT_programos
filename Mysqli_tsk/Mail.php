<?php	
		
$to = "tutkus7@inbox.lt";
$subject = "My subject";
$txt = "Hello world!";
$headers = "From: webmaster@example.com" . "\r\n" ."CC: somebodyelse@example.com";

mail($to,$subject,$txt,$headers);

?>
