import axios from "axios"; // Убрали лишний {post}
import { useState } from "react";
import "../styles.css";

async function sendShortUrl(url) {
    try {
        const data = { "user_url": url };
        const response = await axios.post("http://localhost:8080/api/url/short_url", data);

        return response.data;
    } catch (error) {
        console.error("Ошибка при отправке URL:", error.message);
        return "Ошибка при сокращении";
    }
}

function AppDisplay() {
    const [userUrl, setUserUrl] = useState("");
    const [shortUrl, setShortUrl] = useState("");

    const handleInputChange = (e) => {
        setUserUrl(e.target.value);
    };

    const handleSumbit = async () => {
        if (!userUrl) return;
        const result = await sendShortUrl(userUrl);
        setShortUrl(typeof result === 'object' ? JSON.stringify(result) : result);
    };

    return (
        <div className="AppDisplay">
            <input
                type="text"
                value={userUrl}
                onChange={handleInputChange}
                placeholder="Введите ссылку..."
            />
            <button onClick={handleSumbit}>Сократить ссылку</button>

            {shortUrl && (
                <p>
                    <strong>Результат:</strong>
                    <span>{shortUrl}</span>
                </p>
            )}
        </div>
    );

}

export default AppDisplay;
//sdfsdg