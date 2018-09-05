#include<omp.h>
#include<stdio.h>
#include<stdlib.h>

//Source: https://www.coursera.org/lecture/parallelism-ia/3-4-parallel-loops-Q3Qo3
int main(int argc, char *argv[])
{
	#pragma omp parallel for 
	for (int i = 0; i <10000; i++){
		printf("Iteration %d is processed by thread %d \n", i, omp_get_thread_num()); 
	}
}
