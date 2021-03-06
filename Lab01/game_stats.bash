#! /bin/bash

#---------------------------------------
# $Author: ee364c26 $
# $Date: 2017-08-26 16:40:36 -0400 (Sat, 26 Aug 2017) $
#---------------------------------------

# Do not modify above this line.

if (( $# != 2 ))
then
	echo "Usage: ./game_stats.bash <file> <game>"
	exit 1
fi

fname=$1
gname=$2

if [[ ! -e $fname ]]
then
	echo "Error: $fname does not exist" 
	exit 2
fi

total=0
thours=0
min=10000
max=0

while IFS=, read name g_name hnum
do
	if [[ $gname == $g_name ]]
	then
		(( total=$total+1 ))
		(( thours=$thours+$hnum ))
		if (( $max < $hnum ))
		then
			max=$hnum
			nmax=$name
		fi
		if (( $min >= $hnum ))
		then
			min=$hnum
			nmin=$name
		fi
	fi
done < "$fname"

echo "Total students: $total"
echo "Total hours spent in a day: $thours"
echo "$nmax spent the highest amount of time in a day: $max"
echo "$nmin spent the least amount of time in a day: $min"

exit 0

