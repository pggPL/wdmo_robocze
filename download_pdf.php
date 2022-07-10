<?php
	// Create connection
	$conn = pg_connect("host=/var/run/postgresql dbname=wdmo user=wdmo password=1234");
	// Check connection
	if (!$conn) {
	  die("Connection failed: " . $conn->connect_error);
	  header("Location: https://github.com/pggPL/wdmo/raw/main/main.pdf");
	} 

	$sql = "INSERT INTO log (ip, time, type) VALUES ('".$_SERVER['REMOTE_ADDR']."', '".date("Y-m-d h:i:sa")."', 'pdf')";
	pg_exec($conn, $sql);


	$sql = "SELECT IP FROM IPs WHERE IP = '".$_SERVER['REMOTE_ADDR']."'";
	$result = pg_exec($conn, $sql);

	if(pg_num_rows($result) == 0){
		$sql = "INSERT INTO IPs (IP) VALUES ('".$_SERVER['REMOTE_ADDR']."')";
		$result = pg_exec($conn, $sql);
	}

	pg_close($conn);


	header("Location: https://github.com/pggPL/wdmo/raw/main/main.pdf")
?>