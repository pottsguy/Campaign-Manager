const names = []

function updateNameDisplay() {
    const li = document.createElement("li");
    const newName = document.createTextNode(document.getElementById('nameInput').value);
    li.appendChild(newName);
    document.getElementById("nameList").appendChild(li);
}