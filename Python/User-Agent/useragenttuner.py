import random;

###############################################################################
#Creates a textfile with X number of useragents chosen at random from fileName
###############################################################################

fileName = "useragents.txt";

numberOfAgents = int(raw_input("Number of random User-Agents: "));

allAgents = [];

#Add all User-Agents from file to array
with open(fileName, 'r') as file:
    for line in file:
        allAgents.append(line);
    file.close();

print("All User-Agents read from file");

#Randomly choose X useragents and save them to a file named Xuseragents.txt
file = open(str(numberOfAgents) + fileName, "wb");
counter = 0;

while counter < numberOfAgents:
    file.write(random.choice(allAgents));
    counter += 1;

file.close();
print("Done");
