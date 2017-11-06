#! /bin/bash

#---------------------------------------
# $Author: ee364c26 $
# $Date: 2017-09-03 17:06:54 -0400 (Sun, 03 Sep 2017) $
#---------------------------------------

# Do not modify above this line.

if (( $# != 1 ))
then
	echo "Usage: process_logs.bash <input file>"
	exit 1
fi

if [[ ! -r $1 ]]
then
	echo "Error: <$1> is not a readable file"
	exit 2
fi

touch $1.out
exec 4> $1.out
sed 1d $1 | while read time temp
do
	arrtemp=($temp)	
	len=${#arrtemp[*]}
	total=0
	for i in ${arrtemp[*]}
	do
		(( total=$total + $i ))	
	done 
	average=$(bc <<< "scale=2 ; $total/$len")
	echo "Average temperature for time $time was $average C.">&4
	sorted=$(for item in ${arrtemp[*]}; do echo $item; done | sort -n)
	arrsort=($sorted)
	if (( $len%2 != 0 ))
	then
		(( mednum=($len/2) ))
		printf "Median temperature for time %s was %0.2f C.\n" ${colarr[0]} ${sorted[$mednum]} >&4
		echo >&4
	fi
	if (( $len%2 == 0 ))
	then		
		(( mednum=($len/2)-1 ))
		(( m2=$mednum+1 ))
		(( avg1=${arrsort[$m2]} + ${arrsort[$mednum]} ))
		avg2=$(bc <<< "scale=2 ; $avg1/2") 
		echo "Median temperature for time $time was $avg2 C." >&4
		echo >&4
	fi
done 

mname=$(head -n 1 $1)
marr=($mname)
len=${#marr[*]}
dum=2
while (( $dum <= $len ))
do	
	col=$(cut -f$dum $1)
	colarr=($col)
	colf=${colarr[@]:1}
	sort2=$(for item in ${colf[*]}; do echo $item; done | sort -n)
	colsort=($sort2)
	lfin=${#colsort[*]}
	tot=0
	for i in ${colsort[*]}
	do
		(( tot=$tot + $i ))	
	done 
	aver=$(bc <<< "scale=2 ; $tot/$lfin")
	echo "Average temperature for time $colarr was $aver C." >&4
	if (( $lfin%2 != 0 ))
	then
		(( mednum=($lfin/2) ))
		printf "Median temperature for time %s was %0.2f C.\n" ${colarr[0]} ${colsort[$mednum]} >&4
		echo >&4 
	fi
	if (( $lfin%2 == 0 ))
	then		
		(( mednum=($lfin/2)-1 ))
		(( m2=$mednum+1 ))
		(( avg1=${colsort[$m2]} + ${colsort[$mednum]} ))
		avg2=$(bc <<< "scale=2 ; $avg1/2") 
		echo "Median temperature for time $colarr was $avg2 C." >&4
		echo >&4 
	fi
	(( dum=$dum+1 ))
done

exit 0

