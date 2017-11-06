#! /bin/bash

#---------------------------------------
# $Author: ee364c26 $
# $Date: 2017-09-05 16:41:42 -0400 (Tue, 05 Sep 2017) $
#---------------------------------------

# Do not modify above this line.

if (( $# != 1 ))
then
	echo "Usage: ./sorting_data.bash <input file>"
	exit 1
fi

if [[ ! -r $1 ]]
then
	echo "Error: <$1> is not a readable file"
	exit 2
fi

fname=$1
echo "Your choices are:"
echo "1) First 10 people"
echo "2) Last 5 names by highest zipcode"
echo "3) Address of 6th-10th by reverse e-mail"
echo "4) First First 12 companies"
echo "5) Pick a number of people"
echo "6) Exit"

while ((1))
do
echo -n "Your choice:"
read num
if (( num == 1 ))
then
	tail -n +2 $1 | sort -k7,7 -k5,5 -k2,2 -k1,1 -t, | head -n 10
	continue	
fi 

if (( num == 2 ))
then
	
	tail -n +2 $1 | sort -k8,8n -t, | tail -n 5 | cut -f1,2 -d, 	
	continue
fi
if (( num == 3 ))
then
	
	tail -n +2 $1 | sort -k11,11r -t, | head -n 10 | tail -n 5 | cut -f4 -d,	
	continue
fi
if (( num == 4 ))
then
	
	tail -n +2 $1 | sort -k3,3 -t, | head -n 12 | cut -f3 -d,	
	continue
fi
if (( num == 5 ))
then
	
	echo -n "Enter a number:"
	read ent
	tail -n +2 $1 | sort -k2,2 -k1,1 -t, | head -n $ent
	continue
fi
if (( num == 6 ))
then
	echo "Have a nice day!"
	exit 0	
fi
if (( num != 1 || num != 2 || num != 3 || num != 4 || num != 5 || num != 6))
then
	echo "Error! Invalid selection!"
	continue
fi
done 



