import React, { useState, useEffect } from "react";
import { withAuthenticationRequired } from "@auth0/auth0-react";

import { Center } from "@chakra-ui/layout";
import {
  VictoryBar,
  VictoryChart,
  VictoryAxis,
  VictoryTheme,
  VictoryStack,
} from "victory";

import Loading from "../components/Loading";

function Charts() {
  const [graphData, setQuarterlyData] = useState(null);
  const [graphConfig, setGraphConfig] = useState(null);

  useEffect(() => {
    fetch("api/quarter-mock")
      .then((res) => res.json())
      .then((response) => {
        setGraphConfig(response.config);
        setQuarterlyData(response.data);
      });
  }, []);

  return (
    <Center>
      <div>
        <h1>Charts</h1>
        {graphData ? (
          <VictoryChart domainPadding={20} theme={VictoryTheme.material}>
            <VictoryAxis
              tickValues={graphConfig.xAxis.tickValue}
              tickFormat={graphConfig.xAxis.tickFormat}
            />
            <VictoryAxis dependentAxis tickFormat={(x) => `$${x / 1000}k`} />
            <VictoryStack colorScale={"cool"}>
              {Object.entries(graphData).map((year) => (
                <VictoryBar
                  key={year[0]}
                  data={year[1]}
                  x="quarter"
                  y="earnings"
                />
              ))}
            </VictoryStack>
          </VictoryChart>
        ) : (
          <Loading />
        )}
      </div>
    </Center>
  );
}

export default withAuthenticationRequired(Charts, {
  onRedirecting: () => <Loading />,
});
