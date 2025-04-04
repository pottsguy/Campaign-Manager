const names = []

function addName() {
    const li = document.createElement("li"); // returns a https://developer.mozilla.org/en-US/docs/Web/API/HTMLLIElement
    const del = document.createTextNode("Delete");
    const btn = document.createElement('button'); // returns a https://developer.mozilla.org/en-US/docs/Web/API/HTMLButtonElement
    btn.addEventListener("click", removeCombatant);
    const notes = document.createElement('input'); // returns a https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement
    const newName = document.createTextNode(document.getElementById('nameInput').value); // returns a https://developer.mozilla.org/en-US/docs/Web/API/Text
    notes.value = document.getElementById('creationNotes').value;
    notes.style.width = '450px';
    // const creationNotes = document.createTextNode(document.getElementById('creationNotes').value);
    li.appendChild(newName);
    document.getElementById("nameList").appendChild(li);
    li.append(notes);
    li.appendChild(btn);
    btn.appendChild(del);

    function removeCombatant() {
        li.remove()
    }
}