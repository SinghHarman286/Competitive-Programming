// laolmotlov , lol

function search(long, short) {
	let count = 0;
	for(let i = 0; i < long.length; i++) {
		for(let j = 0; j < short.length; j++) {
			// checking now
			if(long[i+j] !== short[j]) {
				break;
			}
			if(j === short.length - 1) {
				count++;
			}
		}
	}
	return count;
}

// much better

function search(long, short) {
	let count = 0;
	let short_str = long.slice(0, short.length + 1);
	console.log(short_str);

	if(short_str === short) {
		count++;
	}

	for(let i = short.length; i < long.length; i++) {
		short_str = short_str - long[i - short.length]+ long[i];
		if(short_str === short) {
			count++;
		}
	}

	return count;
}