
const form = document.getElementById('news-form');
// Example CORS configuration in Express
const express = require('express');
const cors = require('cors');
const { text } = require('body-parser');
const app = express();

app.use(cors());


form.addEventListener('submit', async (event) => {

  event.preventDefault();


  const input = document.getElementById('news-text').value;

  try {
 
    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({text: input}),
    });
    console.log(text);


    if (response.ok) {
 
      const prediction = (await response.json()).prediction;
      const resultDiv = document.getElementById('prediction-result');
      resultDiv.innerText = prediction === 0 ? 'The review is Real' : 'The review is Fake';
    } else {
      console.error('Request failed:', response.status);
    }
  } catch (error) {
    console.error('Request failed:', error);
  }
});
