import React, { useState, useEffect } from "react";
import { useAuth0, withAuthenticationRequired } from "@auth0/auth0-react";

import Loading from "../components/Loading";
import { useColorModeValue } from "@chakra-ui/color-mode";
import {
  Box,
  Center,
  Container,
  Heading,
  Stack,
  Text,
} from "@chakra-ui/layout";
import { FormControl } from "@chakra-ui/form-control";
import { Input } from "@chakra-ui/input";
import { useNavigate } from "react-router";

function TrainHeader() {
  const boxColor = useColorModeValue("teal.500", "teal.700");
  const headingColor = useColorModeValue("yellow.200", "yellow.300");
  return (
    <Box
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
        direction={{ base: "column-reverse", lg: "row" }}>
        <Stack
          spacing="32px"
          align={{ base: "center", lg: "flex-start" }}
          textAlign={{ base: "center", lg: "left" }}
          maxW={{ base: "full", lg: "md" }}>
          <Stack spacing="16px" align={{ base: "center", lg: "flex-start" }}>
            <Heading
              as="h1"
              fontSize="4xl"
              fontWeight="semibold"
              letterSpacing="tight"
              color={headingColor}>
              Upload training data
            </Heading>

            <Text color="white">Enhancing your model</Text>
          </Stack>
        </Stack>
      </Container>
    </Box>
  );
}

function Train() {
  const { getAccessTokenSilently } = useAuth0();
  const navigate = useNavigate();

  function uploadFile(e) {
    const formData = new FormData();

    formData.append("file", e.target.files[0]);

    const sendData = async () => {
      try {
        const accessToken = await getAccessTokenSilently({
          audience: process.env.AUTH0_API_AUDIENCE,
          scope: "read:data",
        });
        await fetch("/api/data/preferences/process", {
          method: "POST",
          body: formData,
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        }).then((res) => {
          if (res.ok) {
            window.location.reload();
          }
        });
      } catch (e) {
        console.log(e.message);
      }
    };
    sendData();
  }
  return (
    <>
      <TrainHeader />
      <Center pt={10} pb={12} ml={4} mr={4} spacing="16px">
        <Box
          bg="orange.300"
          width="50%"
          pl={2}
          pr={2}
          minH="300px"
          align="center">
          <FormControl position="relative" encType="multipart/form-data">
            <Input
              id="file"
              border="dashed 2px black"
              type="file"
              bg="orange.400"
              width="100%"
              m={2}
              marginBlockEnd="0px"
              marginInline="0px"
              minH="280px"
              onChange={uploadFile}
            />
          </FormControl>
        </Box>
      </Center>
    </>
  );
}

export default withAuthenticationRequired(Train, {
  onRedirecting: () => <Loading />,
});
