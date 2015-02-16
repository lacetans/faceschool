window.onload = inicia_activadors;

function inicia_activadors() {
	if (window.innerWidth > 950) {

		$("#menu_img").hide();
		document.getElementById("a1").addEventListener("mouseover", resalta_icona_menu1_pc, false);
		document.getElementById("a1").addEventListener("mouseout", desresalta_icona_menu1_pc, false);
		document.getElementById("a2").addEventListener("mouseover", resalta_icona_menu2_pc, false);
		document.getElementById("a2").addEventListener("mouseout", desresalta_icona_menu2_pc, false);
		document.getElementById("a3").addEventListener("mouseover", resalta_icona_menu3_pc, false);
		document.getElementById("a3").addEventListener("mouseout", desresalta_icona_menu3_pc, false);
		document.getElementById("a4").addEventListener("mouseover", resalta_icona_menu4_pc, false);
		document.getElementById("a4").addEventListener("mouseout", desresalta_icona_menu4_pc, false);
	
	} else {

		$("#menu_img").show();
		modifica_menu_settings();

	}
	
}


// Resolució mode ordinador

function resalta_icona_menu1_pc() {

	$("#a1").css("background-color","black");
	$("#a1").css("border-bottom","1px solid orange");
	$("#a1").css("border-top","1px solid orange");
	$("#a1 a").css("color","orange");

}

function desresalta_icona_menu1_pc() {

	$("#a1").css("background-color","white");
	$("#a1").css("border","none");
	$("#a1 a").css("color","black");

}

function resalta_icona_menu2_pc() {

	$("#a2").css("background-color","black");
	$("#a2").css("border-bottom","1px solid orange");
	$("#a2").css("border-top","1px solid orange");
	$("#a2 a").css("color","orange");

}

function desresalta_icona_menu2_pc() {

	$("#a2").css("background-color","white");
	$("#a2").css("border","none");
	$("#a2 a").css("color","black");

}

function resalta_icona_menu3_pc() {

	$("#a3").css("background-color","black");
	$("#a3").css("border-bottom","1px solid orange");
	$("#a3").css("border-top","1px solid orange");
	$("#a3 a").css("color","orange");

}

function desresalta_icona_menu3_pc() {

	$("#a3").css("background-color","white");
	$("#a3").css("border","none");
	$("#a3 a").css("color","black");

}

function resalta_icona_menu4_pc() {

	$("#a4").css("background-color","black");
	$("#a4").css("border-bottom","1px solid orange");
	$("#a4").css("border-top","1px solid orange");
	$("#a4 a").css("color","orange");

}

function desresalta_icona_menu4_pc() {

	$("#a4").css("background-color","white");
	$("#a4").css("border","none");
	$("#a4 a").css("color","black");

}

// Resolució mode tables i móbil

function modifica_menu_settings() {

	$(".menu_settings").css("flex-direction","column");
	$(".menu_settings").css("-webkit-flex-direction","column");

}
