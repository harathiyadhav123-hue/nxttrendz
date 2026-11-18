
const http = require("http");

const PORT = 3000;
const API_URL = process.env.API_URL || "http://backend:8000";

const server = http.createServer(async (req, res) => {
    if (req.url === "/") {
        res.writeHead(200, { "Content-Type": "text/plain" });
        res.end("NxtTrendz Frontend is running!");
    }

    else if (req.url === "/api/health") {
        try {
            const response = await fetch(`${API_URL}/health`);
            const data = await response.json();

            res.writeHead(200, {
                "Content-Type": "application/json"
            });

            res.end(JSON.stringify(data));
        } catch (error) {
            res.writeHead(502);
            res.end(JSON.stringify({
                error: "Backend unavailable"
            }));
        }
    }

    else {
        res.writeHead(404);
        res.end("Not Found");
    }
});

server.listen(PORT, "0.0.0.0", () => {
    console.log(`NxtTrendz frontend running on port ${PORT}`);
});
