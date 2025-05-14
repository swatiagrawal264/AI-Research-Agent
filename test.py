def funcChessBoard(inputNum):
	result = []
	for i in range(inputNum):
		row = []
		for j in range(inputNum):
			if (i + j) % 2 == 0:
				row.append("W")
			else:
				row.append("S")
		result.append(" ".join(row))
	return "\n".join(result)
	

def main():
	# input for inputNum
	inputNum = 5
	result = funcChessBoard(inputNum)
	print(result)

if __name__ == "__main__":
	main()