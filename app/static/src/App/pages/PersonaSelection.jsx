import React, { useState, useEffect } from "react";
import { useAuth0, withAuthenticationRequired } from "@auth0/auth0-react";

import utils from "../utils";

import { Field, Form, Formik } from "formik";
import {
  FormControl,
  FormErrorMessage,
  FormLabel,
  Center,
  Select,
  Button,
  useColorModeValue,
  Box,
  Container,
  Stack,
  Heading,
  Text,
} from "@chakra-ui/react";
import { Link, useLocation } from "react-router-dom";

import Loading from "../components/Loading";

function PersonaSelectionHeader() {
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

            <Text color="white">
              Select the <strong>desired persona</strong> to predict their{" "}
              <strong>spending habits</strong>.
            </Text>
          </Stack>
        </Stack>
      </Container>
    </Box>
  );
}

function PersonaSelectionForm({ personaMapping, initialFormValues }) {
  function validateField(value) {
    let error;

    if (value === "") {
      error = "Required";
    }

    return error;
  }
  return (
    <Center pt={10} pb={12}>
      {personaMapping ? (
        <Formik initialValues={initialFormValues}>
          {(props) => (
            <Form>
              {Object.entries(personaMapping).map(([category, values]) => (
                <Field key={category} name={category} validate={validateField}>
                  {({ field, form }) => {
                    const reformattedCategory = category
                      .replace("_", " ")
                      .replace(/^\w/, (c) => c.toUpperCase());
                    return (
                      <FormControl
                        isInvalid={
                          form.errors[category] && form.touched[category]
                        }>
                        <FormLabel htmlFor={category}>
                          {reformattedCategory}
                        </FormLabel>
                        <Select {...field} id={category}>
                          {Object.entries(values).map(([id, description]) => (
                            <option value={id} key={`${category}-${id}`}>
                              {description}
                            </option>
                          ))}
                        </Select>
                        <FormErrorMessage>
                          {form.errors[category]}
                        </FormErrorMessage>
                      </FormControl>
                    );
                  }}
                </Field>
              ))}
              <Button
                as={Link}
                mt={4}
                colorScheme="teal"
                isLoading={props.isSubmitting}
                to="habit"
                state={{ selection: props.values }}>
                Submit
              </Button>
            </Form>
          )}
        </Formik>
      ) : (
        <Loading />
      )}
    </Center>
  );
}

function PersonaSelection() {
  const location = useLocation();
  const { user, getAccessTokenSilently } = useAuth0();
  const [personaMap, setPersonaMap] = useState(null);
  const [formValues, setFormValues] = useState({
    age: 0,
    gender: 0,
    marital_status: 0,
    education: 0,
    income: 0,
  });

  useEffect(() => {
    if (location.state !== null) {
      const selectedPersona = location.state.selection;
      setFormValues({
        age: selectedPersona["age"]["value"],
        gender: selectedPersona["gender"]["value"],
        marital_status: selectedPersona["marital_status"]["value"],
        education: selectedPersona["education"]["value"],
        income: selectedPersona["income"]["value"],
      });
    }
    const getPersonaMap = async () => {
      try {
        const accessToken = await getAccessTokenSilently({
          audience: process.env.AUTH0_API_AUDIENCE,
          scope: "read:data",
        });
        await utils
          .requestAPI("GET", "/api/persona/mapping", null, accessToken)
          .then((res) => {
            setPersonaMap(res.data);
          });
      } catch (e) {
        console.log(e.message);
      }
    };
    getPersonaMap();
  }, [getAccessTokenSilently, location.state, user.sub]);

  return (
    <>
      <PersonaSelectionHeader />
      <PersonaSelectionForm
        personaMapping={personaMap}
        initialFormValues={formValues}
      />
    </>
  );
}

export default withAuthenticationRequired(PersonaSelection, {
  onRedirecting: () => <Loading />,
});
