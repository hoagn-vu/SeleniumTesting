const user = JSON.parse(sessionStorage.getItem('user'));
const logoutButton = document.getElementById('logout-btn');

if (!user) {
    window.location.href = '/frontend/html/login.html';
} else {
    document.getElementById('user-name').innerText = user.name;
}

logoutButton.addEventListener('click', () => {
    sessionStorage.removeItem('user');
    window.location.href = '/frontend/html/login.html';
});

const moviesData = [
    { id: 1, title: 'Movie 1', releaseDate: '2021-01-01', director: 'Director 1', rate: 4.5 },
    { id: 2, title: 'Movie 2', releaseDate: '2021-02-06', director: 'Director 2', rate: 4.8 },
    { id: 3, title: 'Movie 3', releaseDate: '2021-03-08', director: 'Director 3', rate: 3.5 },
    { id: 4, title: 'Movie 4', releaseDate: '2021-01-10', director: 'Director 4', rate: 5.0 },
    { id: 5, title: 'Movie 5', releaseDate: '2021-02-21', director: 'Director 2', rate: 2.5 },
    { id: 6, title: 'Movie 6', releaseDate: '2021-06-09', director: 'Director 3', rate: 4.7 },
    { id: 7, title: 'Movie 7', releaseDate: '2021-07-08', director: 'Director 1', rate: 3.6 },
    { id: 8, title: 'Movie 8', releaseDate: '2021-04-01', director: 'Director 2', rate: 2.9 },
    { id: 9, title: 'Movie 9', releaseDate: '2021-07-18', director: 'Director 1', rate: 3.6 },
    { id: 10, title: 'Movie 10', releaseDate: '2021-04-30', director: 'Director 2', rate: 2.9 },
];
const tableBody = document.getElementById('movies-table-body');
moviesData.forEach((movie, index) => {
  const row = `
    <tr>
        <th scope="row" class="text-center">${index + 1}</th>
        <td>${movie.title}</td>
        <td>${movie.releaseDate}</td>
        <td>${movie.rate}</td>
        <td>${movie.director}</td>
    </tr>
  `;
  tableBody.innerHTML += row;
});

const searchTerm = document.getElementById('searchTerm');
    searchTerm.addEventListener('input', (event) => {
        const value = event.target.value.toLowerCase();
        const filteredMovies = moviesData.filter(movie => movie.title.toLowerCase().includes(value));
        tableBody.innerHTML = '';
        filteredMovies.forEach((movie, index) => {
        const row = `
            <tr>
            <th scope="row" class="text-center">${index + 1}</th>
            <td>${movie.title}</td>
            <td>${movie.releaseDate}</td>
            <td>${movie.rate}</td>
            <td>${movie.director}</td>
            </tr>
        `;
        tableBody.innerHTML += row;
    });
});