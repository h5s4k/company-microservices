const express = require('express');
const app = express();
const port = 3000;

app.get('/users', (req, res) => {
	res.json([
		{ id: 1, nome: 'Alice' },
		{ id: 2, nome: 'Bruno' },
		{ id: 3, nome: 'Carla' }
	]);
});

app.listen(port, () => {
	console.log('users-service rodando na porta ${port}');
})
