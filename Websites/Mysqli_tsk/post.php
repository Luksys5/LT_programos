<?php
  if( $_POST["name"] || $_POST["age"] || $_POST["surname"])
  {
	$txt = "vartotojas ".$_POST["name"]." ".$_POST["surname"]." metai ".$_POST["age"]."\n";
	if(!file_put_contents("vartotojai.txt", $txt, FILE_APPEND)){
		$myfile = fopen("vartotojai.txt", "w");
		fwrite($myfile, $txt);
	}
	#echo $_FILES['img']['name'];
	$info = pathinfo($_FILES['img']['name']);
	$ext = $info['extension']; 
	$newname = "newname.".$ext; 
	$target = './'.$newname;
	move_uploaded_file( $_FILES['img']['tmp_name'], $target);
	echo $txt;
    exit();

  }
?>