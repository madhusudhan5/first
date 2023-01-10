.PHONY: say_hello generate clean
all: say_hello hello generate

CC := gcc
say_hello:
	@echo "Hello world"

hello:
	@echo "Compiling hello.c"
	${CC} hello.c -o hello

generate:
	@echo "Creating empty text files"
	touch file-{1..10}.txt

clean:
	@echo "Cleaning up"
	rm *.txt
	rm hello