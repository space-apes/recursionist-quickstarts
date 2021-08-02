#!/bin/sh
until nc -z -v -w30 db 3306
do 
	echo "waiting for db..."
	sleep 5
done

    	
