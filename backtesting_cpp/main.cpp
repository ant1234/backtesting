#include <iostream>
#include <hdf5.h>

int main(int, char**){
    std::cout << "Hello, from backtesting_cpp!\n";
    hid_t fapl = H5Pcreate(H5P_FILE_ACCESS);
}
