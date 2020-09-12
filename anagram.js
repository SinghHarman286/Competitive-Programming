 function validAnagram(str1, str2) {
 	if(str1.length !== str2.length) {
 		return false;
 	}

 	let object1 = {};
 	let object2 = {};

 	for(let i of str1) {
 		// defining keys

 		if(!object1[i]) {
 		    object1[i] = 1;
 		}
 		else {
 		    object1[i] += 1;
 		}
 	}

 	for(let j of str2) {
 		// defining keys
 		
 		if(!object2[j]) {
 		    object2[j] = 1;
 		}
 		else {
 		    object2[j] += 1;
 		}
 	}
 	
 	for(let key in object1) {
 		if(!(key in object2)) {
 			return false;
 		}
 		if(object1[key] !== object2[key]) {
 			return false;
 		}
 	}

 	return true;
 }

 validAnagram('rat', 'tar');


 // Colt's solution
 function validAnagram(first, second) {
  if (first.length !== second.length) {
    return false;
  }

  const lookup = {};

  for (let i = 0; i < first.length; i++) {
    let letter = first[i];
    // if letter exists, increment, otherwise set to 1
    lookup[letter] ? lookup[letter] += 1 : lookup[letter] = 1;
  }
  console.log(lookup)

  for (let i = 0; i < second.length; i++) {
    let letter = second[i];
    // can't find letter or letter is zero then it's not an anagram
    if (!lookup[letter]) {
      return false;
    } else {
      lookup[letter] -= 1;
    }
  }

  return true;
}

// {a: 0, n: 0, g: 0, r: 0, m: 0,s:1}
validAnagram('anagrams', 'nagaramm')