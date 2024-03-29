#include <iostream>
#include <random>
#include <time.h>

extern "C" {

    float readMockedLightIntensity() {
        srand(time(NULL));
        float random_light_intensity = ((float) rand()) / (float) RAND_MAX * 500.0 + 500.0;
        std::cout << "Simulated light intensity reading: " << random_light_intensity << std::endl;
        return random_light_intensity;
    }

}
