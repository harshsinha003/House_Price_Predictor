// This file acts a cron job which give the requests to the render where backend is stored and hence make the site active
const express = require("express");
const axios = require("axios");
const app = express();

const url = `https://house-price-predictor-fouz.onrender.com`;
const interval = 30000;    // 30 milliseconds is 30 seconds

function reloadWebsite() {
  axios
    .get(url)
    .then((response) => {
      console.log("website reloded");
    })
    .catch((error) => {
      console.error(`Error : ${error.message}`);
    });
}

setInterval(reloadWebsite, interval);

app.get("/", (req, res) => {
  res.send("hello world");
});

const port = 4000;

app.listen(port, () => {
  console.log(`server is running on port ${port}`);
});