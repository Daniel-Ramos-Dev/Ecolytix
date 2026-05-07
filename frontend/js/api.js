const API_URL = 'http://127.0.0.1:8000';

async function fetchLatestData() {

    try {

        const response = await fetch(`${API_URL}/api/latest`);

        if (!response.ok) {
            throw new Error('API ERROR');
        }

        return await response.json();

    } catch (err) {

        console.error(err);

        setConnectionStatus('OFFLINE');

        return null;
    }
}

async function startPolling() {

    setInterval(async () => {

        const data = await fetchLatestData();

        if (!data) return;

        setConnectionStatus('ONLINE');

        applyData(data.air_quality, data.status);

        updateCharts(data.air_quality, data.status);

        addLog(
            `[${new Date().toLocaleTimeString()}] AQI: ${data.air_quality} | ${data.status}`
        );

    }, 2000);
}