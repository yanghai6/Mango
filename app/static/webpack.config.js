const webpack = require("webpack");
const Dotenv = require("dotenv-webpack");

module.exports = {
  entry: __dirname + "/src/index.jsx",
  output: {
    path: __dirname + "/dist",
    filename: "bundle.js",
  },
  mode: "development",
  resolve: {
    extensions: [".js", ".jsx", ".css"],
  },
  plugins: [
    new Dotenv({
      path: "../../.env",
      systemvars: true,
    }),
  ],
  module: {
    rules: [
      {
        test: /\.jsx?/,
        exclude: /node_modules/,
        use: [
          {
            loader: "babel-loader",
          },
        ],
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.(png|woff|woff2|eot|ttf|svg)$/,
        use: ["url-loader?limit-100000"],
      },
    ],
  },
};
