const players = ["Player 1", "Player 2", "Player 3", "Player 4"];
// Array  stores the names of players

//  make prompt = innerHTML** 


let currentWolfIndex = Math.floor(Math.random() * players.length);
// Randomly selects the initial "Wolf" player
let holeNum = 1;
// Current hole 
let roundNum = 1;

function playWolf() {
    const currentWolf = players[currentWolfIndex];
    // Retrieves the name of the current "Wolf" player from the players array

    console.log(`Hole ${holeNum}`);
    console.log(`It's ${currentWolf}'s turn as the Wolf.`);
    // Prints the current hole number and the name of the "Wolf" player

    let partner = "";
    const isAlone = confirm(`${currentWolf}, do you want to play alone? Click OK for Yes, Cancel for No.`);
    // Asks the "Wolf" player if they want to play alone
    if (!isAlone) {
        const remainingPlayers = players.filter((player) => player !== currentWolf);
        // Filters out the current "Wolf" player from the players array
        partner = prompt(`Choose a partner for the hole: ${remainingPlayers.join(", ")}`);
        // Asks the "Wolf" player to choose a partner from the remaining players
    }

    let winner = "";
    if (isAlone) {
        winner = prompt(`Who won the hole? Enter 1 for Wolf won alone, 2 for Wolf won with partner, 3 for Other two players won, 4 for All other players won.`);
        // Asks for the winner of the hole when the "Wolf" plays alone
    } else {
        winner = prompt(`Who won the hole? Enter 1 for Wolf won with partner, 2 for Other two players won, 3 for All other players won.`);
        // Asks for the winner of the hole when the "Wolf" has a partner
    }

    let outcome = "";
    if (winner === "1") {
        if (isAlone) {
            outcome = `${currentWolf} won the hole.`;
        } else {
            outcome = `The Wolf (${currentWolf}) and partner (${partner}) won the hole.`;
        }
    } else if (winner === "2") {
        outcome = `Other two players won the hole. Wolf (${currentWolf}) and partner (${partner}) lost.`;
    } else if (winner === "3") {
        outcome = `All other players won the hole. Wolf (${currentWolf}) lost.`;
    } else if (winner === "4") {
        outcome = `Wolf won the hole alone.`;
    } else {
        outcome = "No one won the hole.";
    }
    // Determines the outcome of the hole based on the winner

    console.log(outcome);
    // Prints the outcome of the hole

    currentWolfIndex = (currentWolfIndex + 1) % players.length;
    holeNum++;
    // Updates the current "Wolf" player index and increments the hole number

    if (holeNum > 18) {
        holeNum = 1;
        roundNum++;
    }
    // Resets the hole number and increments the round number if necessary

    if (roundNum === 19) {
        console.log("The game is over!");
        return;
    }
    // Checks if the game is over

    playWolf();
    // Calls the playWolf function recursively to play the next hole
}

// playWolf();
// Starts the game by calling the playWolf function initially
