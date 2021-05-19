console.log('game_detail_view.js');

player_list = document.querySelector('#player-list');

/*
 * Reveal recipient button. Activates via event bubbling.
 * Toggles visibility of a Player's recipient.
 */
player_list.addEventListener('click', function(event) {
    if (event.target.classList.contains('rvl-recipient-btn')) {
    	// If recipient is revealed
    	if (event.target.classList.contains('revealed')) {
    		// Hide recipient
    		event.target.textContent = 'Reveal Recipient';
    		event.target.parentElement.querySelector('.rvl-recipient-btn').classList.remove('revealed');
    		event.target.parentElement.querySelector('.recipient-info').classList.add('display-none');
    	} else {
    		// Show recipient
    		event.target.textContent = 'Hide Recipient';
    		event.target.parentElement.querySelector('.rvl-recipient-btn').classList.add('revealed');
    		event.target.parentElement.querySelector('.recipient-info').classList.remove('display-none');

    	}



    	//event.target.classList.remove('rvl-recipient-btn')
    }
});