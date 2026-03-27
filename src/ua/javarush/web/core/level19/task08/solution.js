function updateTime() {
//TODO:
    const now = new Date();
    let hours = String(now.getHours()).padStart(2, '0');
    let minutes = String(now.getMinutes()).padStart(2, '0');
    const timeString = hours + ":" + minutes;
    document.getElementById("clock").textContent = timeString;
}

function startClock() {
//TODO:
    updateTime();
    setInterval(updateTime, 1000);
}
