#include <iostream>
#include <vector>
#include <string>

int main() {
	std::vector<std::string> buah = {"Apel","Pisang"};
	buah.push_back("Mangga");
	std::vector<std::string> sayur;
	sayur.push_back("Brokoli");
	int len = buah.size();
	std::string ambil = buah[len-1];
	buah.pop_back();
	std::cout<<"Ambil:"<<ambil<<"\n";
	std::cout<<"Buah 1:"<<buah[0]<<"\n";
	std::cout<<"Buah 2:"<<buah[1]<<"\n";
	std::cout<<"Sayur 1:"<<sayur[0]<<"\n";
	return 0;
}
