// JS for templates/game/game_form.html
console.log('game/game_form.js');
console.log('cached? 14')

const submit_game_btn = document.querySelector('#submit-game-btn')

const add_player_btn = document.querySelector('#add-player-btn');

const game_form = document.querySelector('#game-form');
const player_form = document.querySelector('#add-player-form');
const player_form_rows = document.getElementsByClassName('add-player-row'); // Returns live list



let totalForms = document.querySelector("#id_form-TOTAL_FORMS");
// If view is updateGame, the totalForms id selector will differ.
// The following conditional handles that situation.
if (!totalForms) {
    console.log('!totalForms')
    totalForms = document.querySelector("#id_player_set-TOTAL_FORMS");
}

// Number of Player forms (including empty)
let formCount = player_form_rows.length - 1;

// Number of Players in the Game
//let playerCount = countPlayers();

// Add player-form-row
add_player_btn.addEventListener('click', function(event) {
    event.preventDefault();
     if (countPlayers() == 32 || formCount == 31) {
        alert("Maximum number of players is 32.");
        return;
    }

    // Clone form
    const newPlayerForm = player_form_rows[0].cloneNode(true);

    // Reset first name and last name fields to empty
    newPlayerForm.querySelectorAll('input')[0].setAttribute('value', '');
    newPlayerForm.querySelectorAll('input')[1].setAttribute('value', '');

    // Update management_form to handle new forms
    const formRegex = RegExp(`form-(\\d){1}-`, 'g');
    formCount++;

    newPlayerForm.innerHTML = newPlayerForm.innerHTML.replace(formRegex, `form-${formCount}-`);

    console.log(newPlayerForm)

    // Insert element into list
    player_form.appendChild(newPlayerForm);
    totalForms.setAttribute('value', `${formCount + 1}`);

    validateForm();
});

// Remove player-form-row
// Event bubbling. If any child element of game_form is clicked,
// then the event will be bubbled up to the parent node game_form.
// The expression event.target refers to the element the event fired on.
game_form.addEventListener('click', function(event) {
    if (event.target.classList.contains('rmv-player-btn')) {
        // (Grabs first_name field of the Player)
        // event.target.parentElement.querySelector('input').value

        if (countPlayers() == 4) {
                event.preventDefault();
                alert("Minimum number of players is 4.");
        } else {
            event.preventDefault();
            
            parentForm = event.target.parentElement
            
            // Commented out since we are not removing any form, only hiding it
            //event.target.parentElement.remove();
            //formCount--;
            //totalForms.setAttribute('value', `${formCount + 1}`);

            console.log(event.target.parentElement)
            console.log(event.target.parentElement.querySelector('input[type=checkbox]'))


            parentForm.querySelector('input[type=checkbox]').checked = true;

            /*
             * Forms do not need to be re-numbered because no form is deleted.
             * Deleted forms are 'hidden', not manually deleted from the page.
             */
            //updateForms();
            
            parentForm.style.display = 'none';
        }
    }
    validateForm();
});

/*
 * CURRENTLY UNUSED.
 *
 * Updates the id numbers of all Player form rows to reflect
 * the deletion / addition of a form.
 * Iterates and re-numbers the forms ids in order.
 */
function updateForms() {
    let count = 0;
    for (let form of player_form_rows) {
        delete_checkbox = form.querySelector('input[type=checkbox]');
        delete_true = delete_checkbox.checked;

        const formRegex = RegExp(`form-(\\d){1}-`, 'g');
        form.innerHTML = form.innerHTML.replace(formRegex, `form-${count++}-`);

        delete_checkbox.checked = delete_true;
    }
}

/*
 * Counts the number of Players in a Game,
 * excluding empty or hidden Player forms.
 */
function countPlayers() {
    let count = 0;

    for (let form of player_form_rows) {
        if (window.getComputedStyle(form).display === 'none') continue;

        // Grabs the first_name of each form and checks if it exists
        // Does not check last_name.
        if (form.querySelector('input').value) {
            count++;
        }
    }
    return count;
}

// Return true if playerCount is even.
function evenPlayerCount() { return (countPlayers() % 2) == 0; }

// Returns true if all emails are filled in
function checkEmails() {}

/*
 * Prevents User from submitting a Game. 
 * Used when certain Game criteria are not met, such as when there
 * is not an even number of Players.
 */
function validateForm() {
    // If a criteria is not met:
        // Disable the submit button;
        // Display message;
    // Else if criteria are met:
        // Enable the submit, (even if already enabled)

    if (!evenPlayerCount()) {
        submit_game_btn.disabled = true;
        console.log('Disabled submit. playerCount = ', countPlayers())
    } else {
        submit_game_btn.disabled = false;
        console.log('Enabling submit. playerCount = ', countPlayers())
    }
}










