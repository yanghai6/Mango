const requestAPI = async (rest_method, url_endpoint, payload, accessToken) => {
  let res_data;
  try {
    const GET_CONFIG = {
      method: "GET",
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    };
    const POST_CONFIG = {
      method: "POST",
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    };
    return fetch(
      url_endpoint,
      rest_method === "GET" ? GET_CONFIG : POST_CONFIG
    ).then((res) => res.json());
  } catch (e) {
    console.log(e.message);
  }
  return res_data;
};

const utils = {
  requestAPI,
};
export default utils;
