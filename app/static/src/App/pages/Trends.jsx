import React, { useState, useEffect } from "react";
import { useAuth0, withAuthenticationRequired } from "@auth0/auth0-react";

import utils from "../utils";

import Loading from "../components/Loading";
import { useColorModeValue } from "@chakra-ui/color-mode";
import {
  Box,
  Container,
  Heading,
  Stack,
  Text,
  Wrap,
  WrapItem,
} from "@chakra-ui/layout";
import { Tabs, TabList, TabPanels, Tab, TabPanel } from "@chakra-ui/react";
import { Skeleton } from "@chakra-ui/skeleton";
import { VictoryAxis, VictoryChart, VictoryLine, VictoryTheme } from "victory";

function TrendsHeader() {
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
              Trends
            </Heading>

            <Text color="white">Change in consumption</Text>
          </Stack>
        </Stack>
      </Container>
    </Box>
  );
}

function GraphBox({ category, data, ...rest }) {
  const amountData = data["graphData"].map((item) => ({
    x: data["graphData"].indexOf(item),
    y: item["amount"],
  }));
  const frequencyData = data["graphData"].map((item) => ({
    x: data["graphData"].indexOf(item),
    y: item["frequency"],
  }));
  const dateList = data["graphData"].map((item) => item["date"]);
  return (
    <Box p={5} shadow="md" borderWidth="1px" maxW="2xl" {...rest}>
      <Tabs>
        <TabList>
          <Tab>Amount</Tab>
          <Tab>Frequency</Tab>
        </TabList>

        <TabPanels>
          <TabPanel>
            <VictoryChart width="1000" height="400" domainPadding={2}>
              <VictoryAxis
                style={{
                  tickLabels: {
                    fontSize: 22,
                  },
                }}
                tickValues={[...Array(amountData.length).keys()]}
                tickFormat={dateList}
              />
              <VictoryAxis dependentAxis tickFormat={(x) => `$${x}`} />
              <VictoryLine
                style={{
                  data: { stroke: "#c43a31" },
                  parent: { border: "1px solid #ccc" },
                }}
                data={amountData}
              />
            </VictoryChart>
          </TabPanel>
          <TabPanel>
            <VictoryChart width="1000" height="400">
              <VictoryAxis
                style={{
                  tickLabels: {
                    fontSize: 22,
                  },
                }}
                tickValues={[...Array(frequencyData.length).keys()]}
                tickFormat={dateList}
              />
              <VictoryAxis dependentAxis tickFormat={(x) => `${x}`} />
              <VictoryLine
                style={{
                  data: { stroke: "#c43a31" },
                  parent: { border: "1px solid #ccc" },
                }}
                data={frequencyData}
              />
            </VictoryChart>
          </TabPanel>
        </TabPanels>
      </Tabs>
      <Text mt={4}>{category}</Text>
    </Box>
  );
}

function TrendsGraphs({ fetchedData }) {
  return (
    <Stack
      pt={10}
      pb={12}
      ml={40}
      mr={24}
      spacing="16px"
      align={{ base: "center", lg: "flex-start" }}>
      <Wrap spacing={16} flexWrap={"wrap"}>
        {fetchedData ? (
          Object.entries(fetchedData).map(([key, value]) => (
            <WrapItem key={`${key}-personaBox`}>
              <GraphBox key={`${key}-featuring`} category={key} data={value} />
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
    </Stack>
  );
}

function Trends() {
  // /api/data/persona/get_all
  const { user, getAccessTokenSilently } = useAuth0();
  const [graphData, setGraphData] = useState(null);

  useEffect(() => {
    const sendData = async () => {
      try {
        const accessToken = await getAccessTokenSilently({
          audience: process.env.AUTH0_API_AUDIENCE,
          scope: "read:data",
        });
        await utils
          .requestAPI("GET", "/api/trends/get_all", null, accessToken)
          .then((res) => {
            setGraphData(res["data"]);
          });
      } catch (e) {
        console.log(e.message);
      }
    };
    sendData();
  }, [getAccessTokenSilently, user?.sub]);

  return (
    <>
      <TrendsHeader />
      <TrendsGraphs fetchedData={graphData} />
    </>
  );
}

export default withAuthenticationRequired(Trends, {
  onRedirecting: () => <Loading />,
});
