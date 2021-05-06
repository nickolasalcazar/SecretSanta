// JS for templates/game/game_form.html
console.log('game/game_form.js');

const add_player_btn = document.querySelector('#add-player-btn');
//rem_player_btn = document.getElementById('add-player-btn');

const game_form = document.querySelector('#game-form');
const player_form = document.querySelector('#add-player-form');
const player_form_rows = document.getElementsByClassName('add-player-row'); // Returns live list

const totalForms = document.querySelector("#id_form-TOTAL_FORMS");
let formCount = player_form_rows.length - 1;

// Add player-form-row
add_player_btn.addEventListener('click', function(event) {
    event.preventDefault();

     if (formCount == 31) {
        alert("Maximum number of players is 32.");
        return;
    }
    // Clone form
    const newPlayerForm = player_form_rows[0].cloneNode(true);

    // Reset first name and last name fields to empty
    newPlayerForm.querySelectorAll('input')[0].value = '';
    newPlayerForm.querySelectorAll('input')[1].value = '';

    // Update management_form to handle new forms
    const formRegex = RegExp(`form-(\\d){1}-`, 'g');
    formCount++;
    newPlayerForm.innerHTML = newPlayerForm.innerHTML.replace(formRegex, `form-${formCount}-`);
    
    // Insert element into list
    //game_form.insertBefore(newPlayerForm, add_player_btn);
    player_form.appendChild(newPlayerForm);
    totalForms.setAttribute('value', `${formCount + 1}`);

    console.log(formCount)
});

// Event bubbling. If any child element of game_form is clicked,
// then the event will be bubbled up to the parent node game_form.
// The expression event.target refers to the element the event fired on.
game_form.addEventListener('click', function(event) {
    if (event.target.classList.contains('rmv-player-btn')) {

        console.log(formCount)

        if (formCount == 3) {
            alert("Minimum number of players is 4.");
        } else {
            console.log('Node is deleted.')

            event.preventDefault();
            event.target.parentElement.remove();
            formCount--;
            totalForms.setAttribute('value', `${formCount + 1}`);
            updateForms();
        }
    }
});

function updateForms() {
    let count = 0;
    for (let form of player_form_rows) {
        const formRegex = RegExp(`form-(\\d){1}-`, 'g');
        form.innerHTML = form.innerHTML.replace(formRegex, `form-${count++}-`);
    }
}
