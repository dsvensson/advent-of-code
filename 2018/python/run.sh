#!/bin/bash
for x in {1..24}; do 
	if [ -e day$x.py ]; then
		echo "Running day $x..."
		time python3 day$x.py > /dev/null
		echo
	fi
done
