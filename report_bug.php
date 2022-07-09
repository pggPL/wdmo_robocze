<?php
	$bug = '';
	$user = '';
	$mail = '';
	$chapter = '';
	$file = '';
	if(isset($_GET['bug'])){
		$bug = $_GET['bug'];
	}
	if(isset($_GET['user'])){
		$user = $_GET['user'];
	}
	if(isset($_GET['mail'])){
		$mail = $_GET['mail'];
	}
	if(isset($_GET['chapter'])){
		$chapter = $_GET['chapter'];
	}
	if(isset($_GET['file'])){
		$file = $_GET['file'];
	}

	mail("admin@wdmo.pl", "Wiadomość z formularza", "Od: ".$user."(".$mail.")\r\n Dotyczy: rodział ".$chapter." plik ".$file."\r\n  Wiadomość:\r\n\r\n ".$bug);

	echo "Wysłano...";
?>