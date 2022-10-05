console.log('Im in');

const getData = async (url) => {
	// const config = { headers: { Accept: 'application/json' } };
	const result = await axios.get(url);
	return result;
};

let call = (id) => {
	let req = getData(`http://127.0.0.1:5000/dashboard/${id}`);
	req.then((res) => {
		console.log(res);
	});
	req.catch((err) => {
		console.log(err);
	});
};
