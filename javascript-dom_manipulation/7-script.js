fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error(`Erreur HTTP: ${response.status}`);
    }
    return response.json()
  })
  .then(data => {
    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      document.getElementById('list_movies').appendChild(li);
    })
  })
  .catch(error => {
    console.error(`Error: ${error}`);
  });
  