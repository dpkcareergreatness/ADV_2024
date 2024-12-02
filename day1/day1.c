#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

//#define DEBUG
#ifdef DEBUG
#define PRINT printf
#else
#define PRINT
#endif /* DEBUG */

uint32_t input1[1000];
uint32_t input2[1000];

void ParseInput(FILE *f, uint32_t * ip1, uint32_t * ip2)
{
	if (f != NULL)
	{
		char line[80];
		size_t read;
		size_t len = 80;
		uint32_t id = 0;
		char * strNum;
		while (fgets(line,sizeof(line),f)) {
			strNum = strtok(line,"   \n");
			int count = 0;
			do 
			{
			//	PRINT(" %s \n", strNum);
				if (count == 0)
				{
					input1[id] = atoi(strNum);
				}
				else if (count == 1)
				{
					input2[id] = atoi(strNum);
				}
				count = (count +1)%2;
				strNum = strtok(NULL,"   \n");
			}while(strNum !=NULL);
			id++;
		}
	}
}

/* Bubble sort, could do better */
void SortInput(uint32_t *ip, size_t size)
{
	for (uint32_t i = 0; i < size; i++)
	{
		for (uint32_t j = 0; j < size - 1 - i; j++)
		{
			if(ip[j] > ip[j+1])
			{
				uint32_t temp = ip[j];
				ip[j] = ip [j+1];
				ip[j+1] = temp;
			}
		}
	}
	for (uint32_t id = 0; id< size; id++)
	{
		PRINT (" %d \n", ip[id]);
	}
}

uint64_t GetDeviation(uint32_t *ip1, uint32_t *ip2, size_t size)
{
	uint64_t deviation = 0U;
	for (uint32_t id = 0; id < size; id++)
	{
		deviation += (ip1[id] > ip2[id]) ? (ip1[id] - ip2[id]) : (ip2[id] - ip1[id]);
	}

	return deviation;
}

int main()
{
	FILE *fp = fopen("./day1.txt", "r");
	ParseInput(fp, input1, input2);
	SortInput(input1, sizeof(input1)/sizeof(input1[0]));
	SortInput(input2, sizeof(input2)/sizeof(input2[0]));
	printf ("\n Deviation value is %lu", GetDeviation(input1, input2, sizeof(input1)/sizeof(input1[0])));
}