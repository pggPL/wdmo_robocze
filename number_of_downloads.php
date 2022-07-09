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
	  header("Location: contents.html");
	} 

	$sql = "SELECT * FROM IPs WHERE 1";
	$result = $conn->query($sql);


	$conn->close();



	echo $result->num_rows;
?>