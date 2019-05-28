#!/usr/bin/python
##################
# jangan comot oke #
# bikin tools itu tidak mudah brader #
# Copyright @Pemuda biasa ~MWH~ #
###################
mess = """===============================================
            Scrip Deface Sederhana            
            -----------+=+---------					                	
                Thanks to : 						
           Member MALWARE WAS HERE						
==============================================="""

print mess " Created by Pemuda Biasa "
title = raw_input("judul title: ")
heading = raw_input("hacked by: ")
imagelink = raw_input("gambar yang di posisi tengah: ")
bgimagelink = raw_input("gambar background: ")
message  = raw_input("pesan . gunakan <br> untuk pindah kehalaman selanjutnya: ")
textcolor = raw_input("warna buat font nya (contoh:green): ")
youtubeid = raw_input("kode youtube nya : ")


#Open the index 
fo = open ("scpepes.html","w")

messagescript1 = """ <html> <head> <title> """

messagescript2 = title

messagescript3 = """ </title> </head> 
<body>
<br>
<style type="text/css">
			body {
				overflow:hidden;
				background-image:ur('');
				background-color: #000000;
				background-repeat:no-repeat;
				background-size: 100% ;
				background-position:top center;
				margin: 0px;
				cursor: ;
				font-family: Iceland, sans-serif;
			}
			a{
				text-decoration: none;
			}
			h1{
			font-family: Iceland, sans-serif;
			font-size:90px;
			color:#fff;
			margin:0px 0px 0px;
			
			}
			h2{
			font-family: Iceland, sans-serif;
			font-size:40px;
			color:#000;
			margin: 0px;
			text-shadow: 0 0 3px #fff;
			
			}
			p{
			color:#fff;
			font-size:25px;
			margin: 0px;
			text-shadow: 0 0 3px #ff0099;

			}
			.fot{
			font-family: Iceland, sans-serif;
			font-size:14px;
			color:#fff;
			margin: 0px;
			text-shadow: 0 0 3px #000, 0px 0px 5px #000;
			}
			 h1{
			color:#000;
			text-shadow: 0 0 5px #fff;
		}
		.greets{
	font-family: Arial, sans-serif;
	line-height: 24px;
	font-size: 18px;
	width: 50%;
	background: #000;
	opacity: 0.9;
	text-transform: uppercase;
	z-index: 9999;
	border-radius:10px;
	-moz-box-shadow: 1px 0px 2px #000;
	-webkit-box-shadow: 1px 0px 2px #000;
	box-shadow: 1px 0px 2px #000;
}
		</style>

	<body bgcolor="#000000" background = """

messagescript4 = bgimage

messagescript5 = """><div class='CenterDiv'>
<center>
<div align="center"><table border="0" width="100%"><tr><td>

<font size="7">
<b><font face="times"><b><center><SCRIPT>



farbbibliothek = new Array();



farbbibliothek[0] = new Array("#FF0000","#FF1100","#FF2200","#FF3300","#FF4400","#FF5500","#FF6600","#FF7700","#FF8800","#FF9900","#FFaa00","#FFbb00","#FFcc00","#FFdd00","#FFee00","#FFff00","#FFee00","#FFdd00","#FFcc00","#FFbb00","#FFaa00","#FF9900","#FF8800","#FF7700","#FF6600","#FF5500","#FF4400","#FF3300","#FF2200","#FF1100");



farbbibliothek[1] = new Array("#FF0000","#FFFFFF","#FFFFFF","#FF0000");



farbbibliothek[2] = new Array("#FFFFFF","#FF0000","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF");



farbbibliothek[3] = new Array("#FF0000","#FF4000","#FF8000","#FFC000","#FFFF00","#C0FF00","#80FF00","#40FF00","#00FF00","#00FF40","#00FF80","#00FFC0","#00FFFF","#00C0FF","#0080FF","#0040FF","#0000FF","#4000FF","#8000FF","#C000FF","#FF00FF","#FF00C0","#FF0080","#FF0040");



farbbibliothek[4] = new Array("#FF0000","#EE0000","#DD0000","#CC0000","#BB0000","#AA0000","#990000","#880000","#770000","#660000","#550000","#440000","#330000","#220000","#110000","#000000","#110000","#220000","#330000","#440000","#550000","#660000","#770000","#880000","#990000","#AA0000","#BB0000","#CC0000","#DD0000","#EE0000");


farbbibliothek[5] = new Array("#FF0000","#FF0000","#FF0000","#FFFFFF","#FFFFFF","#FFFFFF");


farbbibliothek[6] = new Array("#FF0000","#FDF5E6");



farben = farbbibliothek[4];



function farbschrift()



{



for(var i=0 ; i<Buchstabe.length; i++)



{



document.all["a"+i].style.color=farben[i];



}



farbverlauf();



}



function string2array(text)



{



Buchstabe = new Array();



while(farben.length<text.length)



{



farben = farben.concat(farben);



}



k=0;



while(k<=text.length)



{



Buchstabe[k] = text.charAt(k);



k++;



}



}



function divserzeugen()



{



for(var i=0 ; i<Buchstabe.length; i++)



{



document.write("<span id='a"+i+"' class='a"+i+"'>"+Buchstabe[i] + "</span>");



}



farbschrift();



}



var a=1;



function farbverlauf()



{



for(var i=0 ; i<farben.length; i++)



{



farben[i-1]=farben[i];



}



farben[farben.length-1]=farben[-1];







setTimeout("farbschrift()",30);



}



//



var farbsatz=1;



function farbtauscher()



{



farben = farbbibliothek[farbsatz];



while(farben.length<text.length)



{



farben = farben.concat(farben);



}



farbsatz=Math.floor(Math.random()*(farbbibliothek.length-0.0001));



}



setInterval("farbtauscher()",5000);



text =" """

messagescript6  = heading

messagescript7 = """;//h 
string2array(text);


divserzeugen();



//document.write(text);"""


messagescript8 = """<script type="text/javascript" src="http://htmlfreecodes.com/codes/rain.js"></script> 
	 <body bgcolor="black">
	 <style type="text/css">body { font-family: 'times'; color: white; padding: 0; margin: 0; background-image: url(''); background-repeat:no-repeat; background-position:center; background-size: 100% 100%; } { 0% { opacity: 1.0; } 50% { opacity: 0.0; } 100% { opacity: 1.0; } } img { opacity: 0.8; } img { animation-name: rotate ; animation-duration: 5s; animation-play-state: running; animation-timing-function: linear; animation-iteration-count: infinite; opacity: 1.0; filter: alpha(opacity=50); } img:hover { opacity: 1.0;filter: alpha(opacity=100); } @keyframes rotate{ 10% {transform:rotateY(36deg)} 20% {transform:rotateY(72deg)} 30% {transform:rotateY(108deg)} 40% {transform:rotateY(144deg)} 50% {transform:rotateY(180deg)} 60% {transform:rotateY(216deg)} 70% {transform:rotateY(252deg)} 80% {transform:rotateY(288deg)} 90% {transform:rotateY(324deg)} 100% {transform:rotateY(360deg)} } </style>  <center> <img src=" """

messegescript9 = imagelink

messagescript10 = """" width="450" height="450"> </center>
<script language=\"JavaScript\">
var i=0
var j=0
var texteNE, affiche
var texte=\"<br><br><br><br><br><font face=Orbitron color="""

messagescript11 = textcolor

messagescript12 = """ size=7> """

messagescript13 = message

messegescript14 = """<br><br></font><br></b></div>\"
var ie = (document.all);
var ne = (document.layers); 
function init(){
texteNE='';
machine_a_ecrire();
}
function machine_a_ecrire(){
texteNE=texteNE+texte.charAt(i)
affiche='<font face=Orbitron size=1 color=#ffffff><strong>Messenge : '+texteNE+'</strong></font>'
if (texte.charAt(i)=="<") {
j=1
}
if (texte.charAt(i)==">") {
j=0
}
if (j==0) {
if (document.getElementById) { // avec internet explorer
document.getElementById("bulle").innerHTML = affiche;
}
}
if (i<texte.length-1){
i++
setTimeout("machine_a_ecrire()",70)
}
else
return
}
</script>
<font face="Orbitron" size="1"><blink><span style="color: rgb(255, 255, 255);"><b><font color=lime size=4></font></b></u></blink><br></font></b>
<a href="/index.php"><img style="position:fixed;bottom:0px;z-index:1000;right:-10px;"  src="http://static1.squarespace.com/static/5706c12007eaa0b82399660d/5706c68bf0bc33987cae6c71/577d5c5d37c581fd0e25c10b/1469717705608/insult-145142_1280.png" type="image/gif" width="150"></a></body>
<!-- CSS --><style>
.CenterDiv{width:650px;border:1px #ff0000 solid;padding:5px;margin:0px auto; background: url('http://i.imgur.com/sDbaMsW.gif');}
</style>
<br>
<br>
<br>
<iframe width="0" height="0" src="http://www.youtube.com/v/"""

messagescript15 = youtubeid

messagescript16 = """&autoplay=1" frameborder="0"></iframe>"""

fo.write(messagescript1)
fo.write(messagescript2)
fo.write(messagescript3)
fo.write(messagescript4)
fo.write(messagescript5)
fo.write(messagescript6)
fo.write(messagescript7)
fo.write(messagescript8)
fo.write(messagescript9)
fo.write(messagescript10)
fo.write(messagescript11)
fo.write(messagescript12)
fo.write(messagescript13)
fo.write(messagescript14)
fo.write(messagescript15)
fo.write(messagescript16)

print "sudah selesaai yang bikin scrip"
print "tinggal di upload aja ke web terget aja"
