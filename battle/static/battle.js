const names = []

function addName() {
    const li = document.createElement("li"); // returns a https://developer.mozilla.org/en-US/docs/Web/API/HTMLLIElement
    const del = document.createTextNode("Delete");
    const btn = document.createElement('button'); // returns a https://developer.mozilla.org/en-US/docs/Web/API/HTMLButtonElement
    btn.addEventListener("click", removeCombatant);
    const notes = document.createElement('input'); // returns a https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement
    const newName = document.createTextNode(document.getElementById('nameInput').value); // returns a https://developer.mozilla.org/en-US/docs/Web/API/Text
    notes.value = document.getElementById('creationNotes').value;
    notes.style.width = '400px';
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

let selected = null

function dragOver(e) {
    if (isBefore(selected, e.target)) {
        e.target.parentNode.insertBefore(selected, e.target)
    } else {
        e.target.parentNode.insertBefore(selected, e.target.nextSibling)
    }
}

function dragEnd() {
    selected = null
}

function dragStart(e) {
    e.dataTransfer.effectAllowed = 'move'
    e.dataTransfer.setData('text/plain', null)
    selected = e.target
}

function isBefore(el1, el2) {
    let cur
    if (el2.parentNode === el1.parentNode) {
        for (cur = el1.previousSibling; cur; cur = cur.previousSibling) {
            if (cur === el2) return true
        }
    }
    return false;
}