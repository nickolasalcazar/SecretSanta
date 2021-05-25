// JS for templates/game/game_form.html
console.log('game/update_game_form.js');
console.log('cached15')

const add_player_btn = document.querySelector('#add-player-btn');

const game_form = document.querySelector('#game-form');
const player_form = document.querySelector('#add-player-form');
const player_form_rows = document.getElementsByClassName('add-player-row'); // Returns live list

// Criteria list variables
const criteria_list = document.querySelector('#criteria-list');
const odd_player_msg = document.querySelector('#odd-player-msg');
const min_player_msg = document.querySelector('#min-player-msg');

// Select Django form manager TOTAL_FORMS variable
let totalForms = document.querySelector("#id_player_set-TOTAL_FORMS");

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
    let formRegex = RegExp(`set-(\\d){1}-`);
    newPlayerForm.innerHTML = newPlayerForm.innerHTML.replace(formRegex, `set-${formCount}-`);

    // Insert new form into formset
    player_form.appendChild(newPlayerForm);
    totalForms.setAttribute('value', `${formCount + 1}`);

    // Attach listeners
    attachOnInputListeners();
});

// Remove player-form-row. Event bubbling.
game_form.addEventListener('click', function(event) {
    if (event.target.classList.contains('rmv-player-btn')) {
        event.preventDefault();

        if (!canDeleteRow(event.target)) return;
        
        parentForm = event.target.parentElement;

        // Mark form for deletion
        parentForm.querySelector('input[type=checkbox]').checked = true;
        
        parentForm.style.display = 'none';
    }
    validateForm();
});

const submit_game_btn = document.querySelector('#submit-game-btn')
validateForm(); // Make validation check after eventListeners are added
attachOnInputListeners() // Attach oninput event listeners

/*
 * Counts the number of Players in a Game,
 * excluding empty or hidden Player forms.
 */
function countPlayers() {
    let count = 0;
    for (let form of player_form_rows) {
        // Ignore hidden forms
        if (window.getComputedStyle(form).display === 'none') continue;
        // Grabs the 'name' field of each form and checks if filled in
        if (form.querySelector('input').value) count++;
    }
    return count;
}

/*
 * Counts the total number of Player forms, excluding empty or hidden Player forms.
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
    submit_game_btn.disabled = !((totalPlayers % 2 == 0) && totalPlayers >= 4);
    addMessages(totalPlayers);
}

/*
 * Returns a Boolean of whether formRow can be deleted.
 * If there are at least five form rows, then any form row can be deleted.
 */
function canDeleteRow(formRow) { return countForms() >= 5; }

/*
 * Displays elements that specify critieria to creating a Game.
 * Takes current total number of Players as an argument.
 */
function addMessages(totalPlayers) {
    if (totalPlayers % 2 == 0) odd_player_msg.style.display = 'none';
    else odd_player_msg.style.display = '';
    if (totalPlayers >= 4) min_player_msg.style.display = 'none';
    else min_player_msg.style.display = '';
}

/*
 * Attaches oninput event listeners to form inputs. Calls validateForm() upon firing.
 */
function attachOnInputListeners() {
    for (let form of player_form_rows) form.querySelector('input').oninput = validateForm;
}



