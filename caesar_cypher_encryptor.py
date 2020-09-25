def caesarCipherEncryptor(string, key):
    # Write your code here.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
	newString = []
	
	for i in range(len(string)):
		curr_index = alphabet.find(string[i])
		new_index = (curr_index + key ) % len(alphabet)
		newString.append(alphabet[new_index])
		
	return "".join(newString)
