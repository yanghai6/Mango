import { Center } from "@chakra-ui/layout";
import React from "react";

const loadingImg =
  "https://cdn.auth0.com/blog/auth0-react-sample/assets/loading.svg";

const Loading = () => (
  <Center h="md" color="white">
    <div className="spinner">
      <img src={loadingImg} alt="Loading..." />
      <h1>Loading...</h1>
    </div>
  </Center>
);

export default Loading;
