// JS for templates/game/game_form.html
console.log("game/game_form.js")




player_forms = document.getElementsByClassName('player_form')


/*
 * Add extra field
 */
function addForm() {
    let clone = player_forms[player_forms.length-1].cloneNode(true)

    console.log(clone)

    togglePlayerFormeButton(clone)
    player_forms[player_forms.length-1].parentNode.appendChild(clone)
}

function deleteForm() {


}

function togglePlayerFormeButton(elem) {
    elem.addEventListener('click', function() {

        if (this.classList.contains('add-form-row')) {
            this.innerHTML = '-'
            addForm()

        } else {
            //this.innerHTML = '+'
            //deleteForm()
            this.parentNode.remove()
        }

        this.classList.toggle('add-form-row')
        this.classList.toggle('remove-form-row')
    })
}

player_btns = document.getElementsByClassName('player-btn')

for (i = 0; i < player_btns.length; i++) {
    togglePlayerFormeButton(player_btns[i])
}

/*
for (i = 0; i < player_btns.length; i++) {
    player_btns[i].addEventListener('click', function() {

        if (this.classList.contains('add-form-row')) {
            this.innerHTML = '-'
            addForm()

        } else {
            this.innerHTML = '+'
            deleteForm()

        }

        this.classList.toggle('add-form-row')
        this.classList.toggle('remove-form-row')
    })
}
*/

