#! /bin/bash

#---------------------------------------
# $Author: ee364c26 $
# $Date: 2017-08-29 17:27:36 -0400 (Tue, 29 Aug 2017) $
#---------------------------------------

# Do not modify above this line.

if (( $# != 1 ))
then
	echo "Usage: ./kaprekar.bash <non-negative integer>"
	exit 1
fi

num=1

while (( $num <= $1 ))
do
	(( sq= $num*$num ))
	(( len=($(echo $sq | wc -c)-1)))
	if (( $num == 1 ))
	then 
		echo "1, square=1, 1+0=1"
	fi
	if (( $num == 3 ))
	then
		echo "3, square=9, 8+1=9"
	fi
	if (( $num != 2 && $num != 3 && $num != 1 ))
	then
		(( cc1= $len/2 ))		
		num1=$(echo $sq | cut -c 1-$cc1)
		(( cc2=$cc1+1 ))
		num2=$(echo $sq | cut -c $cc2-$len)
		let s=$num1+$num2 
			if (( $s == $num ))
			then
				echo "$num, square=$sq, $num1+$num2=$num"
			fi
	fi
	
	(( num=$num+1 ))
done

exit 0
