import React, { useEffect, useState } from "react";
import { useAuth0 } from "@auth0/auth0-react";
import AuthButton from "./nav/AuthButton";
import logo from "../../../images/logo.png";
import {
  Badge,
  Box,
  Center,
  Container,
  Heading,
  Stack,
  Text,
  VStack,
} from "@chakra-ui/layout";
import { useColorModeValue } from "@chakra-ui/color-mode";
import { Image } from "@chakra-ui/image";

function ProfileHeader() {
  const boxColor = useColorModeValue("green.50", "green.600");
  const headingColor = useColorModeValue("yellow.500", "yellow.200");
  return (
    <Box
      height="100vh"
      as="header"
      pt={14}
      pb={12}
      bg={boxColor}
      boxShadow="sm"
      overflow="hidden"
      position="relative"
      zIndex="0">
      <Container
        as={Stack}
        spacing={8}
        direction={{ base: "column-reverse", lg: "column" }}>
        <Stack
          spacing="32px"
          align={{ base: "center", lg: "center" }}
          textAlign={{ base: "center", lg: "center" }}
          maxW={{ base: "full", lg: "md" }}>
          <Center flex="1" position="relative">
            <Box
              position="absolute"
              left="0"
              top="0"
              width="100%"
              height="100%"></Box>
            <Image src={logo} alt="logo" />
          </Center>
          <Stack spacing="16px" align={{ base: "center", lg: "center" }}>
            <Badge variant="solid" colorScheme="green">
              Now in Pre-Alpha
            </Badge>
            <Heading
              as="h1"
              fontSize="4xl"
              fontWeight="semibold"
              letterSpacing="tight"
              color={headingColor}>
              Mango
            </Heading>

            <Text color={headingColor}>
              <strong>Ripening the Deal</strong>
            </Text>
          </Stack>
        </Stack>
      </Container>
    </Box>
  );
}

const Profile = () => {
  const { user, getAccessTokenSilently } = useAuth0();
  const [serverCheck, setServerCheck] = useState(false);

  useEffect(() => {
    const getUserMetadata = async () => {
      try {
        const accessToken = await getAccessTokenSilently({
          audience: process.env.AUTH0_API_AUDIENCE,
          scope: "read:data",
        });

        fetch("/auth/test/private-scoped", {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        })
          .then((response) => response.json())
          .then((data) => setServerCheck(true));
      } catch (e) {
        console.log(e.message);
      }
    };

    getUserMetadata();
  }, [getAccessTokenSilently, user?.sub]);

  return (
    <>
      <ProfileHeader />
    </>
  );
};

export default Profile;
