#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

//#define DEBUG
#ifdef DEBUG
#define PRINT printf
#else
#define PRINT
#endif /* DEBUG */

uint32_t input1[80];
uint32_t safetCount = 0U;


static inline bool IsItSafeLevel(uint32_t * ip, uint32_t count)
{
	bool isSafe = true;
	bool bIsIncreasing = true;
	if (count > 1U)
	{
		if (ip[0] > ip[1])
		{
			bIsIncreasing = false;
		}

		if (bIsIncreasing)
		{
			for (uint32_t id = 0; id < (count - 1U); id++)
			{
				if ( (ip[id] >= ip [id + 1]) || (abs(ip[id] - ip[id + 1]) > 3))
				{
					isSafe = false;
					break;
				}
			}
		}
		else
		{
			for (uint32_t id = 0; id < (count - 1U); id++)
			{
				if ( (ip[id] <= ip [id + 1]) || (abs(ip[id] - ip[id + 1]) > 3))
				{
					isSafe = false;
					break;
				}
			}
		}
	}

	return isSafe;
	
}

void ParseInput(FILE *f, uint32_t * ip1)
{
	if (f != NULL)
	{
		char line[80];
		size_t read;
		size_t len = 80;
		uint32_t id = 0;
		char * strNum;
		uint32_t levelCount = 0U;
		while (fgets(line,sizeof(line),f))
		{
			id = 0;
			levelCount = 0U;
			strNum = strtok(line," \n");
			do 
			{
				PRINT(" %s \n", strNum);
				input1[id++] = atoi(strNum);
				strNum = strtok(NULL,"   \n");
				levelCount++;
			}while(strNum !=NULL);
			if (IsItSafeLevel(input1, levelCount))
			{
				safetCount++;
			}
		}
	}
}

int main()
{
	FILE *fp = fopen("./day2.txt", "r");
	ParseInput(fp, input1);
	printf ("\n Safe levels are %d \n", safetCount);
}