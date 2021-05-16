// JS for templates/game/game_form.html
console.log('game/game_form.js');
console.log('cached? 13')

const add_player_btn = document.querySelector('#add-player-btn');
//rem_player_btn = document.getElementById('add-player-btn');

const game_form = document.querySelector('#game-form');
const player_form = document.querySelector('#add-player-form');
const player_form_rows = document.getElementsByClassName('add-player-row'); // Returns live list


let totalForms = document.querySelector("#id_form-TOTAL_FORMS");
if (!totalForms) {
    console.log('!totalForms')
    totalForms = document.querySelector("#id_player_set-TOTAL_FORMS");
}

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

    
    
    console.log('formCount', formCount)
});

// Remove player-form-row
// Event bubbling. If any child element of game_form is clicked,
// then the event will be bubbled up to the parent node game_form.
// The expression event.target refers to the element the event fired on.
game_form.addEventListener('click', function(event) {
    if (event.target.classList.contains('rmv-player-btn')) {
        if (formCount == 3) {
            alert("Minimum number of players is 4.");
        } else {
            parentForm = event.target.parentElement

            event.preventDefault();
            
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
});

/*
 * Updates the id numbers of all Player form rows to reflect
 * the deletion / addition of a form.
 * Iterates and re-numbers the forms ids in order.
 * Currently unused.
 */
function updateForms() {
    let count = 0;
    for (let form of player_form_rows) {
        delete_checkbox = form.querySelector('input[type=checkbox]')
        delete_true = delete_checkbox.checked;

        const formRegex = RegExp(`form-(\\d){1}-`, 'g');
        form.innerHTML = form.innerHTML.replace(formRegex, `form-${count++}-`);

        delete_checkbox.checked = delete_true;
    }
}










