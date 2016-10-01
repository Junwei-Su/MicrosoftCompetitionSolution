
import glob
import os

input_directory = str("/Users/clarence/Desktop/MicrosoftCompetition/q2p1.txt")
inputfile =open(input_directory, 'r');

first_line = inputfile.readline();
parameter = int(first_line);

Upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];
Lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
Number = ["0","1","2","3","4","5","6","7","8","9"];


#print(parameter);
#print("check");

output_array=[];

#extract information from the input file
for line in enumerate(inputfile):
    if parameter == 0:
        break;
    else:
        line = str(line[1]);
#        print(line);
        ##run the test here
        allString = line.split(" ");
#        print(allString);
        common_e = len(allString);
        Buket = [];
        for i in range(62):
            Buket.append(0);
        
        for s in allString:
            index = 0;
            for Nu in Number:
                if Nu in s:
                    Buket[index]=Buket[index]+1;
                    index=index+1;
                else:
                    index=index+1;

            for Up in Upper:
                if Up in s:
                    Buket[index]=Buket[index]+1;
                    index=index+1;
                else:
                    index=index+1;
                
            for Lo in Lower:
                if Lo in s:
                    Buket[index]=Buket[index]+1;
                    index=index+1;
                else:
                    index=index+1;

                        
            output = [];

            for i in range(62):
                if i <=9:
                    if Buket[i]==common_e:
                        output.append(Number[i]);
                            
                if i<= 35 and i>9:
                    if Buket[i]==common_e:
                        output.append(Upper[i-10]);
                                
                if i>35:
                    if Buket[i]==common_e:
                        output.append(Lower[i-36]);
                        
            outputString = "".join(output);
                
        output_array.append(outputString);

    parameter = parameter-1;


#finish indicator and close the file
for s in output_array:
    print(s);

inputfile.close();







