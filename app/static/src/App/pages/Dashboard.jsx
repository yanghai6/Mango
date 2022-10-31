import React, { useState, useEffect } from "react";
import { useAuth0, withAuthenticationRequired } from "@auth0/auth0-react";

import utils from "../utils";

import Loading from "../components/Loading";
import { useColorModeValue } from "@chakra-ui/color-mode";
import {
  Badge,
  Box,
  Container,
  Heading,
  HStack,
  Stack,
  Text,
  Wrap,
  WrapItem,
} from "@chakra-ui/layout";
import { Skeleton } from "@chakra-ui/skeleton";
import { Link as RouterLink } from "react-router-dom";
import { Button } from "@chakra-ui/button";
import { VictoryAxis, VictoryChart, VictoryLine } from "victory";

function DashboardHeader() {
  const { user } = useAuth0();
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
              {user.name}'s Dashboard
            </Heading>

            <Text color="white">At a Glance</Text>
          </Stack>
        </Stack>
      </Container>
    </Box>
  );
}

function GraphBox({ rank, category, delta, percent, data, ...rest }) {
  const amountData = data.map((item) => ({
    x: data.indexOf(item),
    y: item["amount"],
  }));
  const dateList = data.map((item) => item["date"]);
  return (
    <Box
      p={5}
      shadow="md"
      borderWidth="1px"
      maxW={{ base: "full", lg: "md" }}
      {...rest}>
      <Box>
        <Heading fontSize="xl">
          #{rank}: {category}
        </Heading>
        <HStack>
          <Box>
            <Text
              fontSize="2xl"
              color={parseFloat(delta) < 0 ? "red" : "green"}
              mt={4}>
              Delta: {parseFloat(delta) < 0 ? "-" : "+"}$
              {Math.abs(parseFloat(delta)).toFixed(2)}
            </Text>
            <Text
              fontSize="2xl"
              color={parseFloat(percent) < 0 ? "red" : "green"}
              mt={4}>
              Percentage: {parseFloat(percent) < 0 ? "-" : "+"}
              {Math.abs(parseFloat(percent)).toFixed(2)}%
            </Text>
          </Box>
          <VictoryChart domainPadding={2}>
            <VictoryAxis />
            <VictoryAxis dependentAxis tickFormat={(x) => `$${x}`} />
            <VictoryLine
              style={{
                data: { stroke: "#c43a31" },
                parent: { border: "1px solid #ccc" },
              }}
              data={amountData}
            />
          </VictoryChart>
        </HStack>
      </Box>
    </Box>
  );
}

function GraphContainer({ dataTop, dataBottom }) {
  return (
    <>
      <Heading
        as="h1"
        fontSize="4xl"
        fontWeight="semibold"
        letterSpacing="tight"
        key="graph-top-categories">
        Highest Growth Categories
      </Heading>
      <Badge variant="solid">Relative to previous month</Badge>
      <Wrap spacing={8} flexWrap={"wrap"} justify="center">
        {dataTop ? (
          dataTop.map((obj) => (
            <WrapItem key={`${obj["category"]}-WrapItem`}>
              <GraphBox
                key={`${obj["category"]}-GraphBox`}
                category={obj["category"]}
                delta={obj["delta"]}
                percent={obj["percent"]}
                data={obj["graphData"]}
                rank={dataTop.indexOf(obj) + 1}
              />
            </WrapItem>
          ))
        ) : (
          <Skeleton>
            <Box
              p={5}
              shadow="md"
              borderWidth="1px"
              maxW={{ base: "full", lg: "md" }}>
              <Heading fontSize="xl">Last Accessed: {}</Heading>
              <Text mt={4}>SOME BIG TEXT</Text>
            </Box>
          </Skeleton>
        )}
      </Wrap>
      <Heading
        as="h1"
        fontSize="4xl"
        fontWeight="semibold"
        letterSpacing="tight"
        key="graph-bottom-categories">
        Greatest Decline Categories
      </Heading>
      <Badge variant="solid">Relative to previous month</Badge>
      <Wrap spacing={8} flexWrap={"wrap"} justify="center">
        {dataBottom ? (
          dataBottom.map((obj) => (
            <WrapItem key={`${obj["category"]}-WrapItem`}>
              <GraphBox
                key={`${obj["category"]}-GraphBox`}
                category={obj["category"]}
                delta={obj["delta"]}
                percent={obj["percent"]}
                data={obj["graphData"]}
                rank={dataBottom.indexOf(obj) + 1}
              />
            </WrapItem>
          ))
        ) : (
          <Skeleton>
            <Box
              p={5}
              shadow="md"
              borderWidth="1px"
              maxW={{ base: "full", lg: "md" }}>
              <Heading fontSize="xl">Last Accessed: {}</Heading>
              <Text mt={4}>SOME BIG TEXT</Text>
            </Box>
          </Skeleton>
        )}
      </Wrap>
    </>
  );
}

function PersonaBox({ personaData, personaMap, ...rest }) {
  const personaState = {
    age: personaData["age"],
    education: personaData["education"],
    gender: personaData["gender"],
    income: personaData["income"],
    marital_status: personaData["marital_status"],
  };
  return (
    <Box
      p={5}
      shadow="md"
      borderWidth="1px"
      maxW={{ base: "full", lg: "md" }}
      {...rest}>
      <Heading fontSize="xl">
        Last Accessed: {personaData["last_accessed"]}
      </Heading>
      <Text mt={4}>
        A{" "}
        <strong>
          {personaMap["marital_status"][[personaData["marital_status"]]]}
        </strong>
        &nbsp;
        <strong>{personaMap["gender"][[personaData["gender"]]]}</strong> whose
        age is&nbsp;
        <strong>{personaMap["age"][[personaData["age"]]]}</strong>, with
        income&nbsp;
        <strong>{personaMap["income"][[personaData["income"]]]}</strong>, and
        education level&nbsp;
        <strong>{personaMap["education"][[personaData["education"]]]}</strong>.
      </Text>
      <Box pt={4}>
        <Button
          colorScheme="yellow"
          as={RouterLink}
          to="/persona/habit"
          state={{ selection: personaState }}>
          Access Prediction
        </Button>
      </Box>
    </Box>
  );
}

function PreviousPersonas({ predictedPersona, personaMapping }) {
  return (
    <>
      <Heading
        as="h1"
        fontSize="4xl"
        fontWeight="semibold"
        letterSpacing="tight"
        key="prediction-top-products">
        Previously Predicted Personas
      </Heading>

      <Wrap spacing={8} flexWrap={"wrap"}>
        {predictedPersona && personaMapping ? (
          predictedPersona.map((persona) => (
            <WrapItem key={`${persona["id"]}-personaBox`}>
              <PersonaBox
                key={`${persona["title"]}-featuring`}
                personaMap={personaMapping}
                personaData={persona}
              />
            </WrapItem>
          ))
        ) : (
          <Skeleton>
            <Box
              p={5}
              shadow="md"
              borderWidth="1px"
              maxW={{ base: "full", lg: "md" }}>
              <Heading fontSize="xl">Last Accessed: {}</Heading>
              <Text mt={4}>SOME BIG TEXT</Text>
            </Box>
          </Skeleton>
        )}
      </Wrap>
    </>
  );
}

function Dashboard() {
  // /api/data/persona/get_all
  const { user, getAccessTokenSilently } = useAuth0();
  const [predictedData, setPredictedData] = useState(null);
  const [personaMap, setPersonaMap] = useState(null);
  const [graphDataTop, setGraphDataTop] = useState(null);
  const [graphDataBottom, setGraphDataBottom] = useState(null);

  useEffect(() => {
    const sendData = async () => {
      try {
        const accessToken = await getAccessTokenSilently({
          audience: process.env.AUTH0_API_AUDIENCE,
          scope: "read:data",
        });
        await utils
          .requestAPI("GET", "/api/data/persona/get_all", null, accessToken)
          .then((res) => {
            setPredictedData(res["data"]);
          });
        await utils
          .requestAPI("GET", "/api/trends/get_all", null, accessToken)
          .then((res) => {
            const sortData = Object.entries(res["data"])
              .map(([key, value]) => ({
                category: key,
                delta: value["delta"]["amount"],
                percent: value["percent"]["amount"],
                graphData: value["graphData"],
              }))
              .sort((a, b) => (b["percent"] > a["percent"] ? 1 : -1));
            setGraphDataTop(sortData.slice(0, 3));
            setGraphDataBottom(sortData.slice(-3).reverse());
          });
        await utils
          .requestAPI("GET", "/api/persona/mapping", null, accessToken)
          .then((res) => {
            setPersonaMap(res["data"]);
          });
      } catch (e) {
        console.log(e.message);
      }
    };
    sendData();
  }, [getAccessTokenSilently, user?.sub]);

  return (
    <>
      <DashboardHeader />
      <Stack
        pt={10}
        pb={12}
        ml={48}
        mr={24}
        spacing="16px"
        align={{ base: "center", lg: "flex-start" }}>
        <GraphContainer dataTop={graphDataTop} dataBottom={graphDataBottom} />
        <PreviousPersonas
          predictedPersona={predictedData}
          personaMapping={personaMap}
        />
      </Stack>
    </>
  );
}

export default withAuthenticationRequired(Dashboard, {
  onRedirecting: () => <Loading />,
});
