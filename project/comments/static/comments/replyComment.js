var commentForm = $("#commentform").get(0);
    var replyForm = $(commentForm).clone().closest("form").addClass("w-100 mt-3");
    replyForm = replyForm.removeAttr("id");
    $(function () {
        $("button.btn-comment-reply").click(function () {
            var cross = $(this).children(".small");
            var commentDiv = $(this).parent().parent();
            if (
                cross.hasClass("icon-cancel")
            ) {
                commentDiv.children("form").remove()
            } else {
                commentDiv.append(
                    $(replyForm).clone().get(0)
                );
                commentDiv.find("input[name='parent']").val(
                    commentDiv.attr("data-comment-id")
                )
            }
            cross.toggleClass("icon-cancel");
        })
    });