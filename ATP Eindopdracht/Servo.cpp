#include <iostream>

extern "C" {

    void openVentilation() {
        std::cout << "Opening ventilation" << std::endl;
    }

    void closeVentilation() {
        std::cout << "Closing ventilation" << std::endl;
    }

}
