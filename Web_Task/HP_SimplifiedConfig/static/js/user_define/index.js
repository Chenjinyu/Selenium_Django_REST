/*
 author: Chen Jinyu
 email: jinyu2010.chen@gmail.com
 date: 2016-05-04
 */
var weburl = this.location.href.match(/http:\/\/([a-zA-Z0-9-_\.]+\/)+/gi);
var webpath = this.location.href.match(/http:\/\/([a-zA-Z0-9-_\.]+\/)/gi);
if (weburl == null) {
    weburl = 'http://127.0.0.1:8000/HP_SimplifiedConfig';
}

/**
 * Ajax to get different configuration categories information
 * @param cgr: configuration categories.
 */
function request_info(cgr){
	high_light_cgr(cgr);
	var post_url = weburl + '/request/' +  cgr + '/';
	$.ajax({
		type: "GET",
		url: post_url,
		dataType: "html",
		beforeSend:function(){
			$("#cgr_loaded").html("");
			$("#cgr_loaded").hide();
			$("#loading_div").fadeIn("fast");
		},
		success: function(response){
			$("#loading_div").hide();
			$("#cgr_loaded").fadeIn();
			$("#cgr_loaded").html(response);
		}
	});
}

/**
 * High light categories.
 */
function high_light_cgr(cgr){
	if(cgr == "processor"){
		$('#cgr_processer').css('background-color', '#425563');
		$('#cgr_memory').css('background-color', '');
		$('#cgr_storage').css('background-color', '');
	}
	else if(cgr == "memory"){
		$('#cgr_memory').css('background-color', '#425563');
		$('#cgr_processer').css('background-color', '');
		$('#cgr_storage').css('background-color', '');
	}
	else if(cgr == "storage"){
		$('#cgr_storage').css('background-color', '#425563');
		$('#cgr_processer').css('background-color', '');
		$('#cgr_memory').css('background-color', '');
	}
	
}

$(document).ready(function(){

	$(".hp_btn").each(function(e){
		$(this).hover(
			function(){
				$(this).css('border-width', '4px');
			  },
			function(){
				$(this).css('border-width', '2px');
			} 
		);
	});
	
	$('#arrow_left_a').each(function(e){
		$(this).hover(
			function(){
				$('#arrow_left').attr("src", "/static/images/prod_img/prod_categories/left_hover.png");
			},
			function(){
				$('#arrow_left').attr("src", "/static/images/prod_img/prod_categories/left_default.png");
		});	
		$(this).mousedown(
			function(){
				$('#arrow_left').attr("src", "/static/images/prod_img/prod_categories/left_click_down.png");
			}
		);	
		
		$(this).click(
			function(){
				alert('haha, you click me, but no any function...lol');
			}
		);
	});
	
	$('#arrow_right_a').each(function(e){
		$(this).hover(
			function(){
				$('#arrow_right').attr("src", "/static/images/prod_img/prod_categories/right_hover.png");
			},
			function(){
				$('#arrow_right').attr("src", "/static/images/prod_img/prod_categories/right_default.png");
		});	
		$(this).mousedown(
			function(){
				$('#arrow_right').attr("src", "/static/images/prod_img/prod_categories/right_click_down.png");
			}
		);	
		
		$(this).click(
			function(){
				alert('haha, you click me, but no any function...lol');
			}
		);
	});
	
	$('.cgr_group').each(function(e){
		$(this).hover(
			function(){
				$(this).css('background-color', '#425563');
			},
			function(){
				$(this).css('background-color', '');
			} 
		);
	});
	
});



