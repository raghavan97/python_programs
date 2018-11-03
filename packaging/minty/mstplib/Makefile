all: clean_build

libmyextn.so: csrc.c
	gcc -fPIC -c csrc.c
	gcc -shared csrc.o -lpthread -o libmyextn.so


clean_build:
	rm -f libmyextn.so csrc.o
	make libmyextn.so
