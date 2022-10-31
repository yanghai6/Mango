import React from "react";

import "../stylesheets/App.css";

import Profile from "../components/Profile";
import { Box, Heading, Text } from "@chakra-ui/layout";
import { Button } from "@chakra-ui/button";

function StartTrial() {
  return (
    <Box as="section">
      <Box
        maxW="2xl"
        mx="auto"
        px={{ base: "6", lg: "8" }}
        py={{ base: "16", sm: "20" }}
        textAlign="center">
        <Heading size="3xl" fontWeight="extrabold" letterSpacing="tight">
          Ready to sweeten the pot ?
        </Heading>
        <Text mt="4" fontSize="lg">
          Start recapturing your customer interests today.
        </Text>
        <Button
          mt="8"
          as="a"
          href="#"
          size="lg"
          colorScheme="yellow"
          fontWeight="bold">
          Book a demo.
        </Button>
      </Box>
    </Box>
  );
}

function Home() {
  return (
    <>
      <Profile />
      <StartTrial />
    </>
  );
}

export default Home;
