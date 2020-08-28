// This file will request JSON data from the OpenSky API
// https://opensky-network.org/apidoc/

//Source of some of this code 
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
#include <typeinfo>

 
using namespace utility;
using namespace web;
using namespace web::http;
using namespace web::http::client;
using namespace concurrency::streams;

// using namespace std;
// input client id
// input lat 
// input lng
// input rad 



json::value get_request(std::string lamin, std::string lomin, std::string lamax, std::string lomax);

json::value get_request(std::string lamin, std::string lomin, std::string lamax, std::string lomax){

	json::value jsonObjectResult;
	// create api path
	std::ostringstream os;
	os << "states/all?lamin=" << lamin << "&lomin="<< lomin <<"&lamax="<< lamax <<"&lomax="<< lomax << ""; 
	std::string requestPath = os.str();

	// Make a GET request.
	auto requestJson = http_client(U("https://opensky-network.org"))
		.request(methods::GET,
			uri_builder(U("api")).append_path(U(requestPath)).to_string())
 
	// Get the response.
	.then([=](http_response response) {
		// Check the status code.
		if (response.status_code() != 200) {
			throw std::runtime_error("Returned " + std::to_string(response.status_code()));
		}
 
		// Convert the response body to JSON object.
		return response.extract_json();
	})
 
	// Get the data field.
	.then([=](json::value jsonObject) mutable {
		jsonObjectResult = jsonObject;
		return jsonObject[U("states")];
	})
 
	// Parse the user details.
	.then([=](json::value jsonObject) {
		std::cout << jsonObject[0] << std::endl;
		std::cout << jsonObject[0][0] << std::endl;

	});
 
	// Wait for the concurrent tasks to finish.
	try {
		requestJson.wait();
	} catch (const std::exception &e) {
		printf("Error exception:%s\n", e.what());
		
	}
	return jsonObjectResult;
}








int main() {

	// fake args
	int r1[5] = {1,45,5,47,10};

	
	//build api request.. 
	std::ostringstream os;
	std::string lamin = std::to_string(r1[1]);
	std::string lomin = std::to_string(r1[2]);
	std::string lamax = std::to_string(r1[3]);
	std::string lomax = std::to_string(r1[4]);
	
	json::value jsonObjectResult = get_request(lamin,lomin,lamax,lomax);
	std::cout << jsonObjectResult[U("states")][0] << std::endl;
	std::cout << jsonObjectResult[U("states")][0][0] << std::endl;

	return 0;
}