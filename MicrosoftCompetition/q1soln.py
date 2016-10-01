
import glob
import os

input_directory = str("/Users/clarence/Desktop/MicrosoftCompetition/PracticeInput.txt")
inputfile =open(input_directory, 'r');

first_line = inputfile.readline();
parameter = int(first_line);

Upper = set("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z");
Lower = set("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z");
Number = set("0","1","2","3","4","5","6","7","8","9");

Buket = []
for i in range(61):
    Buket.append(1);
print(parameter);
print("check");

output=[];

#extract information from the input file
for line in enumerate(inputfile):
	if parameter == 0:
		break;
	else:
		line = str(line[1]);
		print(line);
		##run the test here
		allString = line.split(" ");
		print(allString);

		for s in allString:
           
    			
           index = 0;
			for Up in Upper
				if Up not in s:
					Buket[index]--;
					index++;
				else:
					index++;
				
			for Lo in Lower
				if Lo not in s:
					Buket[index]--;
					index++;
				else:
					index++;
					
			for Nu in Lower
				if Nu not in s:
					Buket[index]--;
					index++;
				else:
					index++;
			output = "";
			common_e = min(Buket);
			for i in range(61):
				if i <=25:
					if Buket[i]==common_e:
						output.append(Upper[i]);
				
				if i<= 51 and i>25:
					if Buket[i]==common_e:
						output.append(Lower[i]);
						
				if i>51:
					if Buket[i]==common_e:
						output.append(Number[i]);
			
			print(output);
			
			break;		
							
		parameter = parameter-1;


#finish indicator and close the file
inputfile.close();







