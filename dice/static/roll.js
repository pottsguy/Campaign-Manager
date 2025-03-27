function roll(max, results, rollDisplayId, totalDisplayId) {
    results.push(Math.floor(Math.random() * max) + 1);
    document.getElementById(rollDisplayId).innerText = `${results}`;
    let total = 0;
    for (i=0 ; i<results.length ; i++) {
        total = total + results[i];
    }
    document.getElementById(totalDisplayId).innerText = `${total}`
    return;
}