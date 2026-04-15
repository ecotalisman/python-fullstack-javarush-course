const express = require('express');
const app = express();
const PORT = 5000;

app.get('/', (req, res) => {
  res.send('Додаток працює!');
});

app.listen(PORT, () => {
  console.log(`Сервер запущений на порту ${PORT}`);
});