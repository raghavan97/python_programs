#include <stdio.h>
#include <pthread.h>

int my_api(char *str)
{
    printf("%s \n",str);
}
static void *thread_routine()
{
	printf("thread executed\n");
	return(NULL);
}

int my_api2(char *str)
{
	pthread_t thread_id;
    int s;

	s=pthread_create(&thread_id, NULL, thread_routine, NULL);
}
