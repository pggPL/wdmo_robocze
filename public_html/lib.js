

function clicked(problem, type_of_button){

	let sender = document.getElementById(problem + "_" + type_of_button)

	let hint1_button = document.getElementById(problem + "_hint1")
	let hint2_button = document.getElementById(problem + "_hint2")
	let hint3_button = document.getElementById(problem + "_hint3")
	let solution_button = document.getElementById(problem + "_solution")

	let buttons = [hint1_button, hint2_button, hint3_button, solution_button]


	for(button of buttons){
		if(button == sender && button.className.includes("problem_button_active")){
			deactivate(problem, type_of_button)
			button.className = button.className.replace("problem_button_active", "")
			return 0;
		}
		button.className = button.className.replace("problem_button_active", "")
	}

	sender.className += " problem_button_active"

	document.getElementById("below_problem_" + problem).innerHTML = '<img src="../pictures/' + chapter + '/' + type_of_button + '_' + problem +'.png" class = "page_image" ondblclick = "show_tex(\''+ chapter + "/" + type_of_button + '_' + problem +'.tex' + '\')" ><br><br>';
	document.getElementById("below_problem_" + problem).style.display = 'block';

}

function deactivate(problem, type_of_button){
	let sender = document.getElementById(problem + '_' + type_of_button)
	sender.className = sender.className.replace("problem_button_active", "");

	document.getElementById("below_problem_" + problem).innerHTML = '';
	document.getElementById("below_problem_" + problem).style.display = 'none';
}

function show_tex(file){
	report_bug_file = file;
	file = "../tex_files/" + file.slice(0, -4)
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	   if (this.readyState == 4 && this.status == 200) {
	    document.getElementById("modal_text").innerHTML = '<pre> <code class = "tex" >' + this.responseText + '</code></pre>'
	    hljs.highlightAll();
	   }
	};
	  xhttp.open("GET", file, true);
	  xhttp.send();
	open_modal()
}

function open_modal(){
	let modal = document.getElementById("myModal");
	modal.style.display = "block";
}
function close_modal(){
	let modal = document.getElementById("myModal");
	modal.style.display = "none";
}

function on_load(){
	// Get the modal
	let modal = document.getElementById("myModal");

	// Get the button that opens the modal
	let btn = document.getElementById("myBtn");

	// Get the <span> element that closes the modal
	let span = document.getElementsByClassName("close")[0];

	span.onclick = function() {
	  modal.style.display = "none";
	}

	// When the user clicks anywhere outside of the modal, close it
	window.onclick = function(event) {
	  if (event.target == modal) {
	    modal.style.display = "none";
	  }
	}
}

function report_bug(){
	let report_text = document.getElementById("bug").value;
	let user = document.getElementById("user").value;
	let mail = document.getElementById("mail").value;
	var xhttp = new XMLHttpRequest();
		xhttp.onreadystatechange = function() {
		   if (this.readyState == 4 && this.status == 200) {
		   	if(this.responseText == "Wysłano..."){
		    	alert("Dziękujemy!")
		    	document.getElementById("bug").value = "";
		   	}
		   	else{
				alert("Wystąpił niezidentyfikowany błąd. Spróbuj ponowanie później.")
		   	}
		   }
		};
	xhttp.open("GET", "../report_bug.php?user=" + user +"&mail=" + mail + "&bug=" + report_text + "&chapter=" + chapter + "&file=" + report_bug_file, true);
	xhttp.send();

}
