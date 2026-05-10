async function fetchLatestData() {

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/api/latest"
        );

        const data = await response.json();

        return data;

    } catch (error) {

        console.error(error);

        return null;
    }
}