def read(input):
	with open(input, 'r') as file:
		data = file.read()
	return data


def normalize(element: any) -> str | float:
	try:
		return float(element)
	except ValueError:
		return str(element)


