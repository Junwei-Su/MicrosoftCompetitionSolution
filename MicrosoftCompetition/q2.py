
import glob
import os

input_directory = str("/Users/clarence/Desktop/MicrosoftCompetition/q2p.txt")
inputfile =open(input_directory, 'r');

first_line = inputfile.readline();
money = float(first_line);

#print(money);
#print("check");

stock=[];
hour = [];
earn_for_each_stock = [];
decision_for_each_stock = [];

second_line = inputfile.readline();
hours_line = second_line.strip().split(" ");

for s in hours_line:
    if s != "":
        hour.append(s);

#print(hour);

length = len(hour);

#extract information from the input file
for line in enumerate(inputfile):
    line = str(line[1]);
    content=line.strip().split(" ");
    print(content)
    price=[];
    decision=[];
    stock.append(content[0]);
    for i in range(len(content)-1):
        if content[i+1] != "":
            price.append(float(content[i+1]));

    print(price);
    current_money = money;
    for i in range(len(price)-1):
#        print(len(price))
#        print(i)
#        print(price[i]);
#        print(price[i+1]);
        if price[i+1] > price[i]:
            if i >=1 and (decision[i-1]== "B" or decision[i-1]== ".") :
                    decision.append(".");
            else:
                if current_money>=price[i]:
                    decision.append("B");
                    current_money= current_money-price[i];
                else:
                    decision.append(" ");


        if price[i+1] <= price[i]:
            if i >=1 and (decision[i-1]== " " or decision[i-1]== "S"):
                decision.append(" ");
            elif i>0:
                decision.append("S");
                current_money = current_money + price[i];
            else:
                decision.append(" ");
    

        print(decision);

    if decision[len(decision)-1] != "S":
        decision.append("S");
        current_money = current_money+price[len(price)-1];
#current_money=current_money+price[len(price)-1];

    earn_for_each_stock.append(current_money);
#    print(earn_for_each_stock);
    decision_string = "    ".join(decision);
    decision_for_each_stock.append(decision_string);
#    print(decision_for_each_stock);

stock_number = earn_for_each_stock.index(max(earn_for_each_stock))
sn = stock.index("BDCA");
print(earn_for_each_stock[sn]);
print(decision_for_each_stock[sn]);
print(stock[stock_number]);
hour_out = "    ".join(hour);
print(max(earn_for_each_stock));
print(hour_out);
print(decision_for_each_stock[stock_number]);


inputfile.close();







