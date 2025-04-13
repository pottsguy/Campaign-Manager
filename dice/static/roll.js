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

function clearRolls(d4Results, d6Results, d8Results, d10Results, d12Results, d20Results, d100Results) {
    while (d4Results.length > 0) {
        d4Results.pop();
    }
    while (d6Results.length > 0) {
        d6Results.pop();
    }
    while (d8Results.length > 0) {
        d8Results.pop();
    }
    while (d10Results.length > 0) {
        d10Results.pop();
    }
    while (d12Results.length > 0) {
        d12Results.pop();
    }
    while (d20Results.length > 0) {
        d20Results.pop();
    }
    while (d100Results.length > 0) {
        d100Results.pop();
    }
    
    document.getElementById('d4RollsDisplay').innerText = "Rolls";
    document.getElementById('d6RollsDisplay').innerText = "Rolls";
    document.getElementById('d8RollsDisplay').innerText = "Rolls";
    document.getElementById('d10RollsDisplay').innerText = "Rolls";
    document.getElementById('d12RollsDisplay').innerText = "Rolls";
    document.getElementById('d20RollsDisplay').innerText = "Rolls";
    document.getElementById('d100RollsDisplay').innerText = "Rolls";
    document.getElementById('d4TotalDisplay').innerText = "Total";
    document.getElementById('d6TotalDisplay').innerText = "Total";
    document.getElementById('d8TotalDisplay').innerText = "Total";
    document.getElementById('d10TotalDisplay').innerText = "Total";
    document.getElementById('d12TotalDisplay').innerText = "Total";
    document.getElementById('d20TotalDisplay').innerText = "Total";
    document.getElementById('d100TotalDisplay').innerText = "Total";
    return;
}