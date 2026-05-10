async function updateDashboard() {

    const data = await fetchLatestData();

    if (!data) return;

    document.getElementById("air").innerText =
        data.air_quality;

    document.getElementById("status").innerText =
        data.status;

    document.getElementById("insight").innerText =
        data.insight;

    document.getElementById("hash").innerText =
        data.tx_hash;

    document.getElementById("tx-link").href =
        `https://explorer.solana.com/tx/${data.tx_hash}?cluster=devnet`;
}

updateDashboard();

setInterval(updateDashboard, 2000);