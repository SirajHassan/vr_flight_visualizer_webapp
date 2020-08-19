#include <iostream>
#include <vector>
#include <queue> 
#include <thread>

// This file is being used to test and work with code




void testThreads(int id){

	std::cout << "\n thread" << id << "working \n" ;

}

int main(){


//----------initiate queue-------------------//
	int r1[5] = {1,45,5,47,10};
	int r2[5] = {2,46,5,47,10};
	int r3[5] = {3,47,5,47,10};
	int r4[5] = {4,48,5,47,10};
	int r5[5] = {5,49,5,47,10};


	std::queue<int *> myqueue;
	myqueue.push(r1);
	myqueue.push(r2);
	myqueue.push(r3);
	myqueue.push(r4);
	myqueue.push(r5);

	//int* request = myqueue.back();
	//std::cout << "\n" << (request[1]) << "\n" ;

//--- start thread pool -----------------------//

	//each thread will pop element off queue, and start requesting the api until signaled to stop..
	//when connection lost clear databse table.


//--- 





	return 1;
}





