

const input = document.querySelector('#favchap');
const button = document.querySelector('button');
const list = document.querySelector('#list');

let chaptersArray = getChapterList();
if (!Array.isArray(chaptersArray)) {
    chaptersArray = [];
}

button.addEventListener("click", function() {
    if (input.value !== '') {
        displayList(input.value);
        chaptersArray.push(input.value);
        setChapterList();
        input.value = '';
        input.focus();
    }
});
console.log('I dont know what to do with this code, but I will try to run it anyway.');

chaptersArray.forEach(chapter => {
    displayList(chapter);
});

function displayList(item) {
    let li = document.createElement("li");
    li.textContent = item;
    let deleteButton = document.createElement('button');
    deleteButton.textContent = "❌";
    deleteButton.classList.add("delete");
    deleteButton.addEventListener("click", function() {
        list.removeChild(li);
        deleteChapter(li.textContent);
        input.focus();
    });
    li.append(deleteButton);
    list.append(li);
}

function setChapterList() {
    localStorage.setItem('#list', JSON.stringify(chaptersArray));
}

function getChapterList() {}
    // Retrieve the chapters from localStorage
function deleteChapter(chapter) {
    const index = chaptersArray.indexOf(chapter);
    if (index > -1) {
        chaptersArray.splice(index, 1);
        setChapterList();
    }
}
    chaptersArray = chaptersArray.filter(item => item !== chapter);
    setChapterList();

    

    
   