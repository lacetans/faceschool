window.onload = inicia_activadors;

function inicia_activadors() {
	$(".menu_settings").hide();
	document.getElementById("menu_img").addEventListener("click", cambia_estat_menu1, false);
	document.getElementById("menu_img").addEventListener("dblclick", cambia_estat_menu2, false);
	document.getElementById("menu_img").addEventListener("mouseover", resalta_icona_menu, false);
	document.getElementById("menu_img").addEventListener("mouseout", desresalta_icona_menu, false);
}

function cambia_estat_menu1() {
	$("#menu_img").css("background-color","grey");
	$(".menu_settings").show("medium");

}

function cambia_estat_menu2() {
	$("#menu_img").css("background-color","black");
	$(".menu_settings").hide();

}

function resalta_icona_menu() {
	$("#menu_img").css("background-color","grey");	

}

function desresalta_icona_menu() {
	$("#menu_img").css("background-color","black");

}
