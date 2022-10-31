import React from "react";
import { useAuth0 } from "@auth0/auth0-react";
import { Button } from "@chakra-ui/react";

const AuthButton = () => {
  const { loginWithRedirect, logout, isAuthenticated } = useAuth0();

  return (
    <Button
      display={{ base: "none", md: "inline-flex" }}
      fontSize={"sm"}
      fontWeight={600}
      color={"white"}
      bg={"yellow.400"}
      href={"#"}
      _hover={{
        bg: "yellow.300",
      }}
      onClick={() =>
        isAuthenticated
          ? logout({ returnTo: window.location.origin })
          : loginWithRedirect()
      }>
      {isAuthenticated ? "Sign Out" : "Sign In"}
    </Button>
  );
};

export default AuthButton;
