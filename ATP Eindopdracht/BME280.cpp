#include <iostream>
#include <random>
#include <time.h>

extern "C" {

    float readMockedTemperature() {
        srand(time(NULL));
        float random_temperature = ((float) rand()) / (float) RAND_MAX * 125.0 - 40.0;
        std::cout << "Simulated temperature reading: " << random_temperature << std::endl;
        return random_temperature;
    }

}
