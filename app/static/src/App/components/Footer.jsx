// Footer inspired from https://chakra-templates.dev/page-sections/footer

import React from "react";

import {
  Box,
  Button,
  Container,
  Stack,
  Text,
  useColorModeValue,
  VisuallyHidden,
} from "@chakra-ui/react";
import { FaGithub, FaYoutube } from "react-icons/fa";

const SocialButton = ({ children, label, href }) => {
  return (
    <Button
      bg={useColorModeValue("blackAlpha.100", "whiteAlpha.100")}
      rounded={"full"}
      cursor={"pointer"}
      as={"a"}
      href={href}
      display={"inline-flex"}
      alignItems={"center"}
      justifyContent={"center"}
      transition={"background 0.3s ease"}
      _hover={{
        bg: useColorModeValue("yellow.200", "whiteAlpha.200"),
      }}>
      <VisuallyHidden>{label}</VisuallyHidden>
      {children}
    </Button>
  );
};

export default function SmallWithSocial() {
  return (
    <Box
      className={"footer--pin"}
      position={"relative"}
      left={0}
      bottom={0}
      bg={useColorModeValue("gray.50", "gray.900")}
      color={useColorModeValue("gray.700", "gray.200")}>
      <Container
        as={Stack}
        maxW={"6xl"}
        py={4}
        direction={{ base: "column", md: "row" }}
        spacing={4}
        justify={{ base: "center", md: "space-between" }}
        align={{ base: "center", md: "center" }}>
        <Text>© 2021 Mango Technologies. All rights reserved</Text>
        <Stack direction={"row"} spacing={6}>
          <SocialButton
            label={"GitHub"}
            href={"https://github.com/dcsil/mango"}>
            <FaGithub />
          </SocialButton>
          <SocialButton
            label={"YouTube"}
            href={"https://www.youtube.com/watch?v=dQw4w9WgXcQ"}>
            <FaYoutube />
          </SocialButton>
        </Stack>
      </Container>
    </Box>
  );
}
