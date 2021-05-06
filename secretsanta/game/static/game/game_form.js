// JS for templates/game/game_form.html
console.log('game/game_form.js')

add_player_btn = document.getElementById('add-player-btn')
rem_player_btn = document.getElementById('add-player-btn')

// Add player form row
// Bug: adding a row simply duplicates the last row
add_player_btn.addEventListener('click', function() {
    player_rows = document.getElementsByClassName('add-player-row')
    last_row = player_rows[player_rows.length - 1]
    clone = last_row.cloneNode(true)
    last_row.parentNode.appendChild(clone)
})

// Remove a player form row

