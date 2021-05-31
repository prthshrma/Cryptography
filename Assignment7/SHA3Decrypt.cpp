#include<bits/stdc++.h>
using namespace std;
int main()
{
    char hashValue[]="64616261000000008002840A6968616EE46BEFEB6968616E800A8D8A6968616E0008098000000000800A8D8A6968616E64696BE1000000006461626100000000";
    //char hashValue[]="0008098000000000800A8D8A6968616E64696BE100000000646162610000000064616261000000008002840A6968616EE46BEFEB6968616E800A8D8A6968616E";
    map<char,int>convert;    //This maps -->> char to int
    convert['0']=0;
    convert['1']=1;
    convert['2']=2;
    convert['3']=3;
    convert['4']=4;
    convert['5']=5;
    convert['6']=6;
    convert['7']=7;
    convert['8']=8;
    convert['9']=9;
    convert['A']=10;
    convert['B']=11;
    convert['C']=12;
    convert['D']=13;
    convert['E']=14;
    convert['F']=15;

    map<int,int>chiInvert;    //Inverse Mapping of Chi
    chiInvert[0]=0;chiInvert[5]=1;chiInvert[10]=2;chiInvert[11]=3;chiInvert[20]=4;chiInvert[17]=5;chiInvert[22]=6;chiInvert[23]=7;
    chiInvert[9]=8;chiInvert[12]=9;chiInvert[3]=10;chiInvert[2]=11;chiInvert[13]=12;chiInvert[8]=13;chiInvert[15]=14;chiInvert[14]=15;
    chiInvert[18]=16;chiInvert[21]=17;chiInvert[24]=18;chiInvert[27]=19;chiInvert[6]=20;chiInvert[1]=21;chiInvert[4]=22;chiInvert[7]=23;
    chiInvert[26]=24;chiInvert[29]=25;chiInvert[16]=26;chiInvert[19]=27;chiInvert[30]=28;chiInvert[25]=29;chiInvert[28]=30;chiInvert[31]=31;

    uint64_t state[5][5][64], tempstate[5][5][64];
    for(int i = 0; i < 5; ++i)
        for(int j = 0; j < 5; ++j)
            for(int k = 0; k < 64; ++k)
                state[i][j][k]=0;

    int k=0;
    int l=512;

    //Converts Hash to binary bits
    while(k<l)
    {
        for(int j=3;j>=0;j--)
            state[k/(64*5)][(k/64)%5][k%64 + j]=(convert[hashValue[k/4]]>>j)&1;
        k+=4;
    }


    int current_round = 0 ;
    int Total_rounds=24;

	while(current_round < Total_rounds)
    {
        int newColumnParity[5][64];
	    int newState[5][5][64];

        //Chi Inverse

        for(int i=0;i<5;i++)
        {
            for(int k=0;k<64;k++)
            {
                int t=0,shift=4;
                for(int j=0;j<5;j++)
                {
                    t+=(state[i][j][k]*pow(2,shift));
                    shift--;
                }
                int integerValue=chiInvert[t];
                shift=4;
                for(int j=0;j<5;j++)
                {
                    newState[i][j][k]=(integerValue>>shift)&1;
                    shift--;
                }
            }
        }


        for(int i=0; i<5; i++){
		    for(int j=0; j<5; j++){
			    for(int k=0; k<64; k++){
				    state[i][j][k] = newState[i][j][k];
			    }
		    }
	    }


        //Pi Inverse

        for(int i=0; i<5; i++)
        {
		    for(int j=0; j<5; j++)
		    {
			    for(int k=0; k<64; k++)
			    {
				    newState[i][j][k] = state[j][(2*i+3*j)%5][k];
			    }
		    }
	    }

        //Theta Inverse

        for(int i = 0; i < 5; i++)
        {
			for(int k = 0; k < 64; k++)
			{
				newColumnParity[i][k] = 0;
				for(int j = 0; j < 5; j++)
					newColumnParity[i][k] ^= newState[i][j][k];
			}
		}

		for(int i = 0; i < 5; i++)
        {
			for(int j = 0; j < 5; j++)
            {
				for(int k = 0; k < 64; k++)
				{
					state[i][j][k] = newState[i][j][k]^newColumnParity[(i+2)%5][k]^newColumnParity[(i+3)%5][k];
				}
			}
		}
	    ++current_round ;
	}

	 //end of while

    k=0 ;
    //converting bits in ascii
	while(k<512)
    {
	    int t = 0 ,shift=7;
	    for(int j=0;j<8;j++)
        {
	        t +=state[k/(64*5)][(k/64)%5][k%64+j]<<shift ;
	        shift--;
	    }
		printf("%c", t);
        k+=8 ;
	}

return 0;
}
