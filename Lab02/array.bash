#! /bin/bash

# $Author: ee364c26 $
# $Date: 2017-09-05 16:42:06 -0400 (Tue, 05 Sep 2017) $

function array 
{
    # Fill out.
	ARR=(a.txt b.txt c.txt d.txt e.txt)
	num=($RANDOM%5)
	head -n 9 ${ARR[$num]}| tail -n 3
    	return

}


#
# To test your function, you can call it below like this:
#
array 
#
