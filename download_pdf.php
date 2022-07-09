<?php
	$servername = "sql48.lh.pl";
	$username = "serwer61148_wdmo";
	$password = "KTK2009ktk";
	$dbname = "serwer61148_wdmo";

	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) {
	  die("Connection failed: " . $conn->connect_error);
	  header("Location: https://github.com/pggPL/wdmo/raw/main/main.pdf");
	} 

	$sql = "INSERT INTO log (ip, time, type) VALUES ('".$_SERVER['REMOTE_ADDR']."', '".date("Y-m-d h:i:sa")."', 'pdf')";
	$conn->query($sql);


	$sql = "SELECT IP FROM IPs WHERE IP = '".$_SERVER['REMOTE_ADDR']."'";
	$result = $conn->query($sql);

	if($result->num_rows == 0){
		$sql = "INSERT INTO IPs (IP) VALUES ('".$_SERVER['REMOTE_ADDR']."')";
		$conn->query($sql);
	}

	$conn->close();



	header("Location: https://github.com/pggPL/wdmo/raw/main/main.pdf")
?>