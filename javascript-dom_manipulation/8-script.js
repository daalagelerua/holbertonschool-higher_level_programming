fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    if (!response.ok) {
      throw new Error(`Erreur HTTP: ${response.status}`);
    }
    return response.json()
  })
  .then(data => {
    document.getElementById('hello').textContent = data.hello;
  })
  .catch(error => {
    console.error(`Error: ${error}`);
  });
  