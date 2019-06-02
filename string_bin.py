

def zero_string_binaria(palavra):
	max_value = 0
	cont  = 0
	for p in palavra:
		if(p == "0"):
			cont = cont + 1
			if cont > max_value:
				max_value = cont
		else:
			cont = 0

	print(max_value)
	return max_value


palavra = "11010010101001000010101000000101010"
zero_string_binaria(palavra)