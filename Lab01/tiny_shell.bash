#! /bin/bash

#---------------------------------------
# $Author: ee364c26 $
# $Date: 2017-08-26 16:40:54 -0400 (Sat, 26 Aug 2017) $
#---------------------------------------

# Do not modify above this line.

echo -n "Enter a command:" 

read param 

while [[ $param != "quit" ]]
do
	if [[ $param == "hello" ]]
	then
		echo -n "Hello "
		whoami
	elif [[ $param == "whereami" ]]
	then
		echo -n ""
		pwd
	elif [[ $param == "compile" ]]
	then
		for i in *.c
		do
			name=$(echo $i | cut -f 1 -d '.')		
			gcc -Wall -Werror $i -o $name.o
			if [[ $? == 0 ]]
			then
				echo "Compilation succeeded for: $i"
			else
				echo "Compilation failed for: $i"
			fi
		done
	else
		echo "Error: unrecognized input" 
	fi
	echo -n "Enter a command:" 
	read param

done

if [[ $param == "quit" ]]
then
	echo "Goodbye"
	exit 
fi






