#include <stdio.h>
#include <vector>
#include <string>
#include <cstring>
#include <stdlib.h>
#include <iostream>
using namespace std;

int main(int argc, char* argv[])
{
	string mytree = argv[1];
	int size = mytree.size();
	string added_chars = "";
	for(int i = 0; i < size;i++)
	{
		string left = mytree.substr(i, size - i);
		size_t found = added_chars.find(left[0]);
		if (found == string::npos)
		{
			string main = "";
			string diff = "";
			for(int j = 0; j < left.size(); j++)
			{
				if(left[j] == main[0])
				{
					if(diff != "" && diff != main)
	
					else if(diff == main)
							
					else
						diff += left[j];		
				}
				else
					
			}
			added_chars += left[0];
			cout << left << "\n";
		}
	}
}
