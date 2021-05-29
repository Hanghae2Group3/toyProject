// 게시판
// 글 삭제
$(document).ready(function(){
	$(".delArticle").on('click', function() { 
			if(confirm("정말로 삭제하시겠습니까?")) {
				location.href = $(this).data('uri'); 
			}
	});
});