var smallBox;
var minesNum = 32;
var minesOver = 20;
var minesOverFlags = 40;
var mineMap = [];
var inlei;
function start(){
		$(this).hide(500).next().show(500);
		$(".box").show(500)
		$(".prompt").show(500);
		$(".prompt1").show(500)
		minesOver = 20;
		if($(".box")[0].innerHTML == ""){
			for (var i = 0; i < 10; i++) {
				for (var j = 0; j < 18;j++) {
				var con = document.createElement("div")
				con.classList.add("block");
				$(con).attr({"id":i + "_" + j})
				$(".box").append(con)
				mineMap.push({mine:0});
			}
		}
		}
		for(var i= 0;i < 31;i++){
			var idx = Math.floor(Math.random()*160);
			if(mineMap[idx].mine == 0){
				mineMap.mine = 1;
				$(".block")[idx].classList.add("inlei");
			}
		}}
function leftclick(dom){
if(dom && dom.classList.contains('Flags')){
	return false;
}
 inlei= $(".inlei")
if(dom && dom.classList.contains("inlei")){
	for(var i = 0;i<inlei.length;i++){
		inlei[i].classList.add("show")
	}
	setTimeout(over,1000)}else{
	var n = 0;
	var posArr = dom && dom.getAttribute("id").split("_");//2,2
	// alert(posArr)
	posX = posArr && +posArr[0];//2
	posY = posArr && +posArr[1];//2
	dom && dom.classList.add("num");//变换背景
	for (var i = posX - 1;i<= posX + 1;i++){
		for(var j = posY-1;j <= posY+1;j++){
			var aroundBox = document.getElementById(i + "_" + j)
			// console.log(typeof(aroundBox))
			if(aroundBox && aroundBox.classList.contains("inlei")){
				n++;
			}
			
		}

	}
	dom && (dom.innerHTML = n)
	if(n == 0){
		for (var i = posX - 1;i<= posX + 1;i++){
			for(var j = posY -1;j <= posY + 1;j++){
				var nearBox = document.getElementById(i + "_" + j);
					// console.log(nearBox)
				if(nearBox && nearBox.length != 0){
					if(!nearBox.classList.contains("check")){
						nearBox.classList.add("check");
						if(!nearBox.classList.contains('inlei')){
							leftclick(nearBox);	
						}
					}
					
				}
			}
		}
	}
 }}
 onkeydown = function(e){
 	// console.log(e)
 	switch (e.which) {
 		case 123:
 			alert("禁止使用F12后台");
 			return false;
 			break;
 	}
 }
function rightclick(dom){
	if(dom && dom.classList.contains('num')){
		return false;
	}else{
		minesOverFlags--;
		if(dom && !dom.classList.contains('Flags')){
			// $(dom).toggleClass('Flags');
			dom.classList.add('Flags')
		}else{
			(minesOverFlags += 1);
			minesOverFlags ++
			dom.classList.remove('Flags');
		}
		if(dom && dom.classList.contains("inlei")){
			if(!dom.classList.contains("checkt")){
				dom.classList.add("checkt")
				minesOver--;
			}
		}
	}
	if(minesOverFlags == 0){
		alert('Flags is null,then Game Over')
		over()
	}
	if(minesOver == 0){
		GameWin()
	}}
function GameWin(){
	$(".start").hide(800)
	$(".over").hide(800)
	$(".box").fadeOut(800)
	$(".prompt").fadeOut(800)
	$(".prompt1").fadeOut(800)
	$(".box").html('')
	setTimeout(function(){
		$(".GameWin").slideDown(800)
	},800)
}
function over(){
	$(".over").hide(800)
	$(".start").hide(800)
	$(".box").fadeOut(800)
	$(".prompt").fadeOut(800)
	$(".prompt1").fadeOut(800)
	$(".box").html('')
	minesNum = 30;
	minesOverFlags = 30;
	setTimeout(function(){
		$(".overBox").slideDown(800);
	},1000)}
function restart(){
	$(".over").hide(800);
	$(".GameWin").hide(500);
	$(".start").show(300);
	$(this).parent().slideUp(300);
		Refresh()
}
function WindowSize(dom){
	$(dom).height($(window).height())
	$(dom).width($(window).width())}
function Refresh(){
	setTimeout(function(){
		location.reload()
	},600)}
function prompt(){
	// console.log($(window).width())
	if($(window).width() < 1920){
		$(".Prompt").show()
	}else{
		$(".Prompt").hide()
	}}
$(function(){
		WindowSize($(".wrapper"));
		$(".start").click(start);
		prompt()
		$(".over").click(over);
		$(".Restart").click(restart);
		$(".prompt").children('span').html(minesOver);
		$(".prompt1").children('span').html(minesOverFlags);
		oncontextmenu = function(){
			return false;
		}
		$(".box")[0].onmousedown = function(e){
			var event = e.target;
			if(e.which == 1) {
				leftclick(event)
			}else if(e.which == 3) {
				rightclick(event)
				$(".prompt1").children('span').html(minesOverFlags)
				$(".prompt").children('span').html(minesOver)
			}
		}})