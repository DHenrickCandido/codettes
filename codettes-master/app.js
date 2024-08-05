const express = require('express');
const bodyParser = require('body-parser');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const app = express();
const port = 3000;


app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// const db = new sqlite3.Database('database/database.db');

// db.serialize(() => {
//     db.run("CREATE TABLE IF NOT EXISTS subscribers (id INTEGER PRIMARY KEY, email TEXT NOT NULL)");
// });

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// app.post('/subscribe', (req, res) => {
//     const email = req.body.email;

//     db.run("INSERT INTO subscribers (email) VALUES (?)", [email], (err) => {
//         if (err) {
//             return console.error(err.message);
//         }
//         console.log(`New subscriber: ${email}`);
//     });
// });

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
