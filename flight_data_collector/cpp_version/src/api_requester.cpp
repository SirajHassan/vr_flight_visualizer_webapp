// This file will request JSON data from the OpenSky API
// https://opensky-network.org/apidoc/

//Source of most of this code 
// http://www.atakansarioglu.com/easy-quick-start-cplusplus-rest-client-example-cpprest-tutorial/

// compile with this 
// g++ -std=c++11 api_requester.cpp -stdlib=libc++ -lcpprest -lssl -lcrypto -lboost_system -lboost_thread-mt -lboost_chrono-mt -L/usr/local/opt/openssl/lib -I/usr/local/opt/openssl/include


#include <iostream>
#include <sstream>
#include <string>
#include <cpprest/http_client.h>
#include <cpprest/filestream.h>
#include <cpprest/uri.h>
#include <cpprest/json.h>
 
using namespace utility;
using namespace web;
using namespace web::http;
using namespace web::http::client;
using namespace concurrency::streams;

//using namespace std;
//input client id
//input lat 
//input lng
//input rad 



//int send_request(std::string lamin, std::string lomin, std::string lamax, std::string lomax);

int main() {

	// fake args
	int r1[5] = {1,45,5,47,10};
	
	//build api request.. 
	std::ostringstream os;
	std::string lamin = std::to_string(r1[1]);
	std::string lomin = std::to_string(r1[2]);
	std::string lamax = std::to_string(r1[3]);
	std::string lomax = std::to_string(r1[4]);
	os << "states/all?lamin=" << lamin << "&lomin="<< lomin <<"&lamax="<< lamax <<"&lomax="<< lomax << ""; //"states/all?lamin=45.8389&lomin=5.9962&lamax=47.8229&lomax=10.5226"
	std::string requestPath = os.str();


	// Create a file stream to write the received file into it.
	auto fileStream = std::make_shared<ostream>();
	
	// Open stream to output file.
	pplx::task<void> requestTask = fstream::open_ostream(U("users.json"))
	
	// Make a GET request.
	.then([=](ostream outFile) {
		*fileStream = outFile;
 
		// Create http_client to send the request.
		http_client client(U("https://opensky-network.org"));
 
		// Build request URI and start the request.
		return client.request(methods::GET, uri_builder(U("api")).append_path(U(requestPath)).to_string());
	})
 
	// Get the response.
	.then([=](http_response response) {
		// Check the status code.
		if (response.status_code() != 200) {
			throw std::runtime_error("Returned " + std::to_string(response.status_code()));
		}
 
		// Write the response body to file stream.
		response.body().read_to_end(fileStream->streambuf()).wait();
		// std::cout << response.body() << "\n";
 
		// Close the file.
		return fileStream->close();
	});
 
	// Wait for the concurrent tasks to finish.
	try {
		while (!requestTask.is_done()) { std::cout << ""; }
	} catch (const std::exception &e) {
		printf("Error exception:%s\n", e.what());
	}
 
	return 0;
}