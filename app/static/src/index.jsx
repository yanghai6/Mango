import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import { ChakraProvider, ColorModeScript } from "@chakra-ui/react";

import "./index.css";
import App from "./App/App";
import theme from "./App/theme";
import reportWebVitals from "./reportWebVitals";
import Auth0ProviderWithHistory from "./App/components/auth/Auth0History";

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <ChakraProvider>
        <Auth0ProviderWithHistory>
          <ColorModeScript initialColorMode={theme.config.initialColorMode} />
          <App />
        </Auth0ProviderWithHistory>
      </ChakraProvider>
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
