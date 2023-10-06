#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int infinite_while(void);

/**
 * main - creates 5 zombie processes.
 * Return: 0 if success.
*/

int main(void)
{
	int i, j;

	for (i = 0; i < 5; i++)
	{
		if (fork() == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	for (j = 0; j < 5; j++)
	infinite_while();

	return (0);
}

/**
 * infinite_while - sleeps infinitely.
 * Return: 0 if success.
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
