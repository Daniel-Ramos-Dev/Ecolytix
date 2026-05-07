function applyData(aqi, status) {

    document.getElementById('aqi-value').innerText = aqi;
    document.getElementById('aqi-status').innerText = status;

    const statusElement = document.getElementById('aqi-status');

    if (status === 'GOOD') {
        statusElement.style.color = '#00E676';
    }
    else if (status === 'MODERATE') {
        statusElement.style.color = '#FFD600';
    }
    else {
        statusElement.style.color = '#FF5252';
    }
}

function addLog(message) {

    const logs = document.getElementById('logs');

    const item = document.createElement('div');
    item.classList.add('log-item');

    item.innerText = message;

    logs.prepend(item);
}

function setConnectionStatus(status) {

    const el = document.getElementById('connection-status');

    el.innerText = status;

    if (status === 'ONLINE') {
        el.style.color = '#00E676';
    }
    else {
        el.style.color = '#FF5252';
    }
}