(function () {
    var buttons = document.getElementsByClassName("fold-button");

    for (var i = 0; i < buttons.length; i++) {
        buttons[i].addEventListener("click", function (event) {
            var card = event.target.parentElement;
            if (!card || !card.classList.contains("one-post")) {
                card = event.target.closest
                    ? event.target.closest(".one-post")
                    : null;
            }
            if (!card) {
                return;
            }

            var folded = card.classList.contains("folded");
            if (folded) {
                card.classList.remove("folded");
                event.target.textContent = "свернуть";
            } else {
                card.classList.add("folded");
                event.target.textContent = "развернуть";
            }
        });
    }
})();
