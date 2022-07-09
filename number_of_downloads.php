<?php
	
	$servername = "sql48.lh.pl";
	$username = "serwer61148_wdmo";
	$password = "KTK2009ktk";
	$dbname = "serwer61148_wdmo";

	// Create connection
	$conn = pg_connect("host=/var/run/postgresql dbname=wdmo user=wdmo password=1234");
	// Check connection
	if (!$conn) {
	  die("Connection failed: " . $conn->connect_error);
	  header("Location: contents.html");
	} 

	$sql = "SELECT * FROM IPs WHERE 1";
	$result = pg_exec($conn, $sql);


	pg_close($conn);



	echo $result->num_rows;
?>