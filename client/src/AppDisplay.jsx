import axios from "axios";
import React, { useState } from "react";

function UrlDisplay() {
    const [userUrl, setUserUrl] = useState("");
    const [responseData, setResponseData] = useState("");
    const [loading, setLoading] = useState(false);

    async function handleSubmit() {
        if (!userUrl.trim()) {
            setResponseData("Пожалуйста, введите URL");
            return;
        }

        setLoading(true);
        setResponseData("");

        try {
            console.log("Отправляем URL:", userUrl.trim()); // Отладка

            const res = await axios.post("http://localhost:8080/api/short_url", {
                "user_url": userUrl.trim()
            });

            console.log("Ответ от сервера:", res);
            console.log("Данные ответа:", res.data);


            if (res.data) {

                if (typeof res.data === 'string') {
                    setResponseData(res.data);
                }

                else if (typeof res.data === 'object') {
                    // Показываем весь объект в читаемом виде
                    setResponseData(JSON.stringify(res.data, null, 2));
                }
            } else {
                setResponseData("Сервер вернул пустой ответ");
            }

        } catch (error) {
            console.error("Детали ошибки:", error);

            if (error.response) {

                console.log("Статус ошибки:", error.response.status);
                console.log("Данные ошибки:", error.response.data);
                setResponseData(`Ошибка сервера: ${error.response.status} - ${JSON.stringify(error.response.data)}`);
            } else if (error.request) {

                console.log("Нет ответа от сервера:", error.request);
                setResponseData("Сервер не отвечает. Проверьте подключение");
            } else {

                console.log("Ошибка запроса:", error.message);
                setResponseData(`Ошибка: ${error.message}`);
            }
        } finally {
            setLoading(false);
        }
    }

    const styles = {
        container: {
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            minHeight: "100vh",
            backgroundColor: "#f5f5f5",
            fontFamily: "Arial, sans-serif"
        },
        content: {
            backgroundColor: "white",
            padding: "40px",
            borderRadius: "10px",
            boxShadow: "0 4px 6px rgba(0, 0, 0, 0.1)",
            width: "100%",
            maxWidth: "500px"
        },
        title: {
            textAlign: "center",
            color: "#333",
            marginBottom: "30px",
            fontSize: "24px"
        },
        inputContainer: {
            display: "flex",
            gap: "10px",
            marginBottom: "20px"
        },
        input: {
            flex: 1,
            padding: "12px",
            border: "2px solid #e0e0e0",
            borderRadius: "5px",
            fontSize: "16px",
            outline: "none",
            transition: "border-color 0.3s ease"
        },
        button: {
            padding: "12px 24px",
            backgroundColor: "#007bff",
            color: "white",
            border: "none",
            borderRadius: "5px",
            fontSize: "16px",
            cursor: "pointer",
            transition: "background-color 0.3s ease"
        },
        buttonDisabled: {
            backgroundColor: "#cccccc",
            cursor: "not-allowed"
        },
        responseContainer: {
            marginTop: "20px",
            padding: "15px",
            backgroundColor: "#f8f9fa",
            borderRadius: "5px",
            borderLeft: "4px solid #007bff",
            maxHeight: "300px",
            overflow: "auto" // Добавляем прокрутку для длинных ответов
        },
        responseText: {
            margin: 0,
            color: "#333",
            fontSize: "14px",
            wordBreak: "break-all",
            whiteSpace: "pre-wrap" // Сохраняем форматирование JSON
        },
        errorResponse: {
            borderLeftColor: "#dc3545",
            backgroundColor: "#fff5f5"
        }
    };

    return (
        <div style={styles.container}>
            <div style={styles.content}>
                <h2 style={styles.title}>URL Отправитель</h2>
                <div style={styles.inputContainer}>
                    <input
                        type="text"
                        style={styles.input}
                        value={userUrl}
                        onChange={(e) => setUserUrl(e.target.value)}
                        placeholder="Введите URL"
                    />
                    <button
                        onClick={handleSubmit}
                        disabled={loading}
                        style={{
                            ...styles.button,
                            ...(loading ? styles.buttonDisabled : {})
                        }}
                    >
                        {loading ? "Отправка..." : "Отправить"}
                    </button>
                </div>

                {}
                {responseData && (
                    <div style={{
                        ...styles.responseContainer,
                        ...(responseData.includes("Ошибка") ? styles.errorResponse : {})
                    }}>
                        <pre style={styles.responseText}>{responseData}</pre>
                    </div>
                )}

                {}
                {process.env.NODE_ENV === 'development' && (
                    <div style={{marginTop: '10px', fontSize: '12px', color: '#999'}}>
                        Статус: {loading ? 'Загрузка...' : 'Готов'}
                    </div>
                )}
            </div>
        </div>
    );
}

export default UrlDisplay;