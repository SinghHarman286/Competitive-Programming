// naive solution -- O(n2)

function maxSubarr(arr, num) {

	// [1, 20 , 20, 5, 0, 50 ] --> 'i' will only be till arr.length - num (6 - 3 + 1)
	let tempSum = 0;
	let maxSum = -Infinity;

	for(i = 0; i <= arr.length - num; i++) {
		for(j = 0; j < num; j++) {
			tempSum += arr[i+j];
		}
		if(tempSum > minSum) {
			maxSum = tempSum;
		}
	}

	return maxSum;
}


// good solution O(n)

function maxSubarr(arr, num) {
	let tempSum = 0;
	let maxSum = 0;

	for(let i = 0; i < num; i++) {
		maxSum += arr[i];
	}

	tempSum = maxSum;

	let length = arr.length;

	for(let j = num; j < length; j++) {
		tempSum = tempSum - arr[j - num] + arr[j];
		maxSum = Math.max(tempSum, maxSum);
	}

	return maxSum;
}