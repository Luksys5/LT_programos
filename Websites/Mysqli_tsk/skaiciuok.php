<?php
	$Proc = $_GET['Procent'];
	$proc = explode(",",$Proc);	
	$Konc = $_GET['koncent'];
	$konc = explode(",",$Konc);
	$Mols = $_GET['Molsvor'];
	$mols = explode(",",$Mols);
	$Names = $_GET['name'];
	$names = explode(",",$Names);
	$mase = $_GET['mase'];
	$counts = count($proc);
	
	$suma=0; $massW = 0; $Tmass = 0;  $TVolume = 0; $TotalVol = array_pad(array(),$counts,0); 
	for($i = 0;$i<$counts;$i++){
		$num = abs($mols[$i]*$proc[$i]*$mase);
		$rum = abs($mols[$i]*$proc[$i]);
		$suma += $rum;
		$TotalVol[$i] = abs($num/$konc[$i])*1000;
	}
	for($i = 0;$i<$counts;$i++){
		$TotalVol[$i] = abs($TotalVol[$i]/$suma);
		$massW = abs($TotalVol[$i]*$konc[$i]);
		$Tmass += ($massW);
		$TVolume += $TotalVol[$i];
		if($i == 0) echo("Required Volume of lipids solution:");
		echo("<br>&nbsp&nbsp&nbsp&nbsp".$names[$i].":".substr($TotalVol[$i],0,6)." μl");
	}
	echo("<br>Total mass of lipid mixture:".substr(($Tmass/1000),0,6)." mg");
	echo("<br>Total Volume of lipid mixture: ".substr(($TVolume/1000),0,6)." ml");
	
?>
