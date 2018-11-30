// this is where the chatbot will send and receive data to and from the server

function print(d) { // too lazy to write entire console.log
    console.log(d);
}

document.addEventListener('DOMContentLoaded', function () {
    let botui = new BotUI('bot');

    function sendMessageToUser(text) {
        // this will send a message to the user
        botui.message.add({
            content: text
        });
    }

    function sendMessageWithActionToUser(text, messageAction, action, data) { // subject to change
        // this will send a message to the user and ask for something in return (an action). actions can be found on botui docs
        // for now keep it simple as there isn't a backend to work with

        // for now let's just do two of the actions that are possible, the textual input and the buttons
        let actions = {
            'input': (text) => botui.action.text({action: {placeholder: text}}),
            'button': (buttons) => botui.action.button({action: buttons}) // buttons will be an array of objects where key is text and value is value. these are generated elsewhere
        };

        botui.message.add({
            content: text
        }).then(function () {
            actions[action](messageAction).then(function (res) {
                // do something with whatever the user writes
                print(res.value);
            })
        });

    }

    function sendToServer(message) {
        // just hanging out here for now. will probably be changed once we begin work with DialogFlow
    }

    function receiveFromServer(message) {
        // just hanging out here for now. will probably be changed once we begin work with DialogFlow
    }

    let button = document.getElementById('show');
    button.addEventListener('click', function () {

        let botSection = document.getElementById('bot');

        // if the section is hidden, then show it
        if (botSection.style.display === 'none' || botSection.style.display === '') { // contains no initial display style to begin with
            botSection.style.display = 'block';
        } else { // else we should hide it
            botSection.style.display = 'none';
        }


        // sendMessageToUser("Hello there");
        // sendMessageWithActionToUser("Hello there", 'General Kenobi', 'input');
        // sendMessageWithActionToUser("Hello there", [{text:'Do', value:'It'}], "button", '');

    });
});