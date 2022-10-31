import React from "react";
import { useNavigate } from "react-router-dom";
import { Auth0Provider } from "@auth0/auth0-react";

const Auth0ProviderWithHistory = ({ children }) => {
  const navigate = useNavigate();

  const onRedirectCallback = (appState) => {
    navigate(appState?.returnTo || window.location.pathname);
  };

  return (
    <Auth0Provider
      domain={process.env.AUTH0_BASE_URL}
      clientId={process.env.AUTH0_SPA_CLIENT_ID}
      redirectUri={window.location.origin}
      scope="read:data"
      useRefreshTokens
      cacheLocation="localstorage"
      onRedirectCallback={onRedirectCallback}>
      {children}
    </Auth0Provider>
  );
};

export default Auth0ProviderWithHistory;
