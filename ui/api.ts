export default function fetcher(url: string): Promise<any> {
    return fetch(url)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP ERROR on ${url} [${response.status}]`)
            }
            return response.json();
        });
    }
