import React, { useState, useEffect } from "react";
import { useAuth0, withAuthenticationRequired } from "@auth0/auth0-react";

import utils from "../utils";

import {
  Box,
  Container,
  Stack,
  Wrap,
  WrapItem,
  Heading,
  Text,
  Skeleton,
  HStack,
  Image,
  Button,
  useColorModeValue,
} from "@chakra-ui/react";
import { Link as RouterLink, useLocation, useNavigate } from "react-router-dom";
import { SettingsIcon } from "@chakra-ui/icons";

import Loading from "../components/Loading";

function PersonaHabitHeader({ describedPersona, predictedValue }) {
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
              Persona Prediction
            </Heading>
            {/* // A [marital status] [gender] whose age is [age], with education level [education] */}

            {describedPersona ? (
              <Text color="white">
                A{" "}
                <strong>
                  {describedPersona["marital_status"]["description"]}
                </strong>
                &nbsp;
                <strong>
                  {describedPersona["gender"]["description"]}
                </strong>{" "}
                whose age is&nbsp;
                <strong>{describedPersona["age"]["description"]}</strong>, with
                income&nbsp;
                <strong>{describedPersona["income"]["description"]}</strong>,
                and education level&nbsp;
                <strong>{describedPersona["education"]["description"]}</strong>.
              </Text>
            ) : (
              <Skeleton>
                <Text color="white">
                  A <strong>marital_status</strong>&nbsp;
                  <strong>gender</strong> whose age is
                  <strong>age</strong>, with education level&nbsp;
                  <strong>education</strong>.
                </Text>
              </Skeleton>
            )}

            {predictedValue ? (
              <Text
                as="h1"
                fontSize="xl"
                fontWeight="semibold"
                letterSpacing="tight"
                color={headingColor}>
                Minimum Offer Value: ${parseFloat(predictedValue).toFixed(2)}
              </Text>
            ) : (
              <Skeleton>
                <Text
                  as="h1"
                  fontSize="xl"
                  fontWeight="semibold"
                  letterSpacing="tight"
                  color={headingColor}>
                  Minimum Offer Value: $100000
                </Text>
              </Skeleton>
            )}
            <Button
              as={RouterLink}
              to="/persona"
              leftIcon={<SettingsIcon />}
              state={{ selection: describedPersona }}>
              Reconfigure Persona
            </Button>
          </Stack>
        </Stack>
      </Container>
    </Box>
  );
}

function PredictionCategory({ title, amount, frequency, ...rest }) {
  return (
    <Box
      p={5}
      shadow="md"
      borderWidth="1px"
      maxW={{ base: "full", lg: "md" }}
      {...rest}>
      <Heading fontSize="xl">{title}</Heading>
      <Text mt={4}>Average: ${parseFloat(amount).toFixed(2)}</Text>
      <Text mt={4}>Frequency: {parseFloat(frequency).toFixed(2)}/month</Text>
    </Box>
  );
}

function FeatureProduct({
  title,
  category,
  total,
  multiples,
  imageHref,
  rank,
  ...rest
}) {
  return (
    <Box
      p={5}
      shadow="md"
      borderWidth="1px"
      maxW={{ base: "full", lg: "md" }}
      {...rest}>
      <Box>
        <HStack>
          <Box>
            <Heading fontSize="xl">
              #{rank}: {title}
            </Heading>
            <Text mt={4}>Total: ${parseFloat(total).toFixed(2)}</Text>
            <Text mt={4}>Multiples: {parseInt(multiples)}</Text>
          </Box>
          {imageHref && imageHref !== "#" && (
            <Image
              boxSize="100px"
              objectFit="contain"
              src={imageHref}
              alt="{title}"
              key="{title}-image"
            />
          )}
        </HStack>
        <Text mt={4}>Category: {category}</Text>
      </Box>
    </Box>
  );
}

function PredictionResult({ predictedHabit, predictedInterest }) {
  return (
    <Stack
      pt={10}
      pb={12}
      ml={48}
      mr={24}
      spacing="16px"
      align={{ base: "center", lg: "flex-start" }}>
      <Heading
        as="h1"
        fontSize="4xl"
        fontWeight="semibold"
        letterSpacing="tight"
        key="prediction-top-products">
        Prediction Top 5 products
      </Heading>

      <Wrap spacing={8} flexWrap={"wrap"} justify="center">
        {predictedInterest ? (
          predictedInterest.map((pred) => (
            <WrapItem key={`${pred["category"]}-wrapItem-feature`}>
              <FeatureProduct
                key={`${pred["title"]}-featuring`}
                title={pred["title"]}
                category={pred["category"]}
                total={pred["total"]}
                multiples={pred["multiples"]}
                imageHref={pred["image"]}
                rank={predictedInterest.indexOf(pred) + 1}
              />
            </WrapItem>
          ))
        ) : (
          <Skeleton>
            <FeatureProduct
              key={"feature-skeleton"}
              title={"skeleton"}
              amount={"0"}
              frequency={"0"}
            />
          </Skeleton>
        )}
      </Wrap>

      <Heading
        as="h1"
        fontSize="4xl"
        fontWeight="semibold"
        letterSpacing="tight"
        key="prediction-general-habits">
        Prediction General Habits
      </Heading>

      <Wrap spacing={8} flexWrap={"wrap"} justify="flex-start">
        {predictedHabit ? (
          predictedHabit.map((pred) => (
            <WrapItem key={`${pred["category"]}-wrapItem-categories`}>
              <PredictionCategory
                key={pred["category"]}
                title={pred["category"]}
                amount={pred["amount"]}
                frequency={pred["frequency"]}
              />
            </WrapItem>
          ))
        ) : (
          <Skeleton>
            <PredictionCategory
              key={"categories-skeleton"}
              title={"skeleton"}
              amount={"0"}
              frequency={"0"}
            />
          </Skeleton>
        )}
      </Wrap>
    </Stack>
  );
}

function PersonaHabit() {
  const location = useLocation();
  const navigate = useNavigate();
  const { user, getAccessTokenSilently } = useAuth0();
  const [predictedData, setPredictedData] = useState(null);
  const [predictedProducts, setPredictedProducts] = useState(null);
  const [predictedValue, setPredictedValue] = useState(null);
  const [personaDesciption, setPersonaDesciption] = useState(null);

  useEffect(() => {
    if (location.state == null) {
      navigate("/persona");
      window.location.reload(); //hack to reload page
    }

    var selectedPersona = location.state.selection;

    const sendData = async () => {
      try {
        const accessToken = await getAccessTokenSilently({
          audience: process.env.AUTH0_API_AUDIENCE,
          scope: "read:data",
        });
        await utils
          .requestAPI(
            "POST",
            "/api/persona/predict_spending_habit",
            selectedPersona,
            accessToken
          )
          .then((res) => {
            setPredictedData(res["data"]);
            setPredictedProducts(res["interest"]);
            setPersonaDesciption(res["description"]);
            setPredictedValue(res["minimum_value"]);
          });
      } catch (e) {
        console.log(e.message);
      }
    };
    sendData();
  }, [getAccessTokenSilently, user?.sub, location.state, navigate]);

  return (
    <>
      <PersonaHabitHeader
        describedPersona={personaDesciption}
        predictedValue={predictedValue}
      />
      <PredictionResult
        predictedHabit={predictedData}
        predictedInterest={predictedProducts}
      />
    </>
  );
}

export default withAuthenticationRequired(PersonaHabit, {
  onRedirecting: () => <Loading />,
});
