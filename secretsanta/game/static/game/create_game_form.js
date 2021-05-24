// JS for templates/game/game_form.html
console.log('game/create_game_form.js');
console.log('cached 10')

const submit_game_btn = document.querySelector('#submit-game-btn')

const add_player_btn = document.querySelector('#add-player-btn');

const game_form = document.querySelector('#game-form');
const player_form = document.querySelector('#add-player-form');
const player_form_rows = document.getElementsByClassName('add-player-row'); // Returns live list

// Select Django form manager TOTAL_FORMS variable
let totalForms = document.querySelector("#id_form-TOTAL_FORMS");

// Number of Player forms (including empty)
let formCount = player_form_rows.length - 1;

// Add player-form-row
add_player_btn.addEventListener('click', function(event) {
    event.preventDefault();
     if (countPlayers() == 32 || formCount == 31) {
        alert("Maximum number of players is 32.");
        return;
    }

    // Clone form
    const newPlayerForm = player_form_rows[0].cloneNode(true);

    // Reset 'name' and 'email' fields to empty before appending
    newPlayerForm.querySelectorAll('input')[0].setAttribute('value', '');
    newPlayerForm.querySelectorAll('input')[1].setAttribute('value', '');

    // Update Django management form variables
    formCount++;
    let formRegex = RegExp(`form-(\\d){1}-`, 'g');
    newPlayerForm.innerHTML = newPlayerForm.innerHTML.replace(formRegex, `form-${formCount}-`);

    // Insert new form into formset
    player_form.appendChild(newPlayerForm);
    totalForms.setAttribute('value', `${formCount + 1}`);

    validateForm();
});

// Remove player-form-row. Event bubbling.
game_form.addEventListener('click', function(event) {
    if (event.target.classList.contains('rmv-player-btn')) {
        if (!canDeleteRow(event.target)) return;

        event.preventDefault();
        
        parentForm = event.target.parentElement;

        console.log(event.target.parentElement)
        console.log(event.target.parentElement.querySelector('input[type=checkbox]'))

        // Reset 'name' and 'email' fields
        event.target.parentElement.querySelectorAll('input')[0].setAttribute('value', '');
        event.target.parentElement.querySelectorAll('input')[1].setAttribute('value', '');
        
        parentForm.style.display = 'none';
    
    }
    validateForm();
});

validateForm(); // Make validation check after eventListeners are added

/*
 * Counts the total number of Players in a Game, excluding empty or hidden Player forms.
 */
function countPlayers() {
    let count = 0;
    for (let form of player_form_rows) {
        // Ignore hidden forms
        if (window.getComputedStyle(form).display === 'none') continue;
        // Grabs the 'name' field of each form and checks if it field i
        if (form.querySelector('input').value) count++;
    }
    return count;
}

/*
 * Counts the total number of Player forms, excluding hidden Player forms.
 */
function countForms() {
    let count = 0;
    for (let form of player_form_rows) {
        if (window.getComputedStyle(form).display === 'none') continue; // Ignore hidden forms
        count++;
    }
    return count;
}

/*
 * Disables submit button if certain Game criteria are not met, such as when there
 * is not an even number of Players.
 */
function validateForm() { 
    const totalPlayers = countPlayers();
    return (!(totalPlayers % 2) == 0 || totalPlayers < 4); }

/*
 * Returns a Boolean of whether formRow can be deleted.
 * If there are at least five form rows, then any form row can be deleted.
 */
function canDeleteRow(formRow) { return countForms() >= 5; }






