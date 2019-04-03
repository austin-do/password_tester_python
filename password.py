def main:

    upperCase = "ABCDEFGHIJKLOPQRSTUVWXYZ"
	lowerCase = "abcdefghijklopqrstuvwxyz"
	symbols = "!@#$&*"
	numbers = "1234567890"
	finalPass = ""
	hold

	for(int i=0; i<6; i++)
		char[] c = new char[6]

		if i == 0:
			Random rand = new Random();
			for(int j=0; j<6; j++)
				c[j] = upperCase.charAt(rand.nextInt(upperCase.length()))

		if i==1:
			Random rand = new Random();
			for(int j=0; j<6; j++)
				c[j] = lowerCase.charAt(rand.nextInt(lowerCase.length()));

		if i>1 && i<4:
			Random rand = new Random();
			for(int j=0; j<6; j++)
				c[j] = symbols.charAt(rand.nextInt(symbols.length()));

		if i>3:
			Random rand = new Random();
			for(int j=0; j<6; j++)
				c[j] = numbers.charAt(rand.nextInt(numbers.length()));

		hold = new String(runBracket(c));
		finalPass += hold;

	print("Password: " + finalPass);

def runBracket(c):
	Random game = new Random()
	round1 = []
	round2 = []
	result = []

	for(int i=0; i<4; i++)
		if(i==0)
			for(int j=0; j<c.length/2; j++)
				if(game.nextInt(1) == 1)
					round1[j] = c[j];
				else
					round1[j] = c[c.length-1];

		else if(i==1)
			for(int j=0; j<round1.length/2; j++)
				if(game.nextInt(1) == 1)
					round2[j] = round1[j];
				else
					round2[j] = round1[round1.length-j-1];

		else
			for(int j=0; j<round2.length/2; j++)
				if(game.nextInt(1) == 1)
					result[j] = round2[j];
				else
					result[j] = round2[round2.length-j-1];
	return result;
