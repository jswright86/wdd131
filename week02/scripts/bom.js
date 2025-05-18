

const input = document.querySelector('#favchap');

const button = document.querySelector('button');


    button.addEventListener("click", function() {
        if (input.value.trim() === '') {
            alert("Please enter a chapter name.");
            input.focus();
            return;
        }

        const li = document.createElement("li");
        li.textContent = input.value;

        const deleteButton = document.createElement('button');
        deleteButton.textContent = "❌";
        deleteButton.addEventListener("click", function() {
            li.remove();
            input.focus();
        });

        li.append(deleteButton);

        const list = document.querySelector('ul');
        list.append(li);

        input.value = '';
        input.focus();
    });
    console.dir(document);