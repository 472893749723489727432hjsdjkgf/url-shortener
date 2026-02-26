import ReactDom from "react-dom/client"
import App from "./App";
import React from "react";
import "../UrlDisplay.module.css"

ReactDom.createRoot(document.getElementById("root")).render(<React.StrictMode><App /></React.StrictMode>);