#include <iostream>
#include <chrono>

int main() {
    const long num_operations = 100000000;
    long result;
    auto start_time = std::chrono::high_resolution_clock::now();
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed;

    // Addition
    result = 0;
    start_time = std::chrono::high_resolution_clock::now();
    for (long i = 0; i < num_operations; ++i) {
        result += 1;
    }
    end_time = std::chrono::high_resolution_clock::now();
    elapsed = end_time - start_time;
    std::cout << "Time taken for 100 million additions: " << elapsed.count() << " seconds" << std::endl;

    // Subtraction
    result = num_operations;
    start_time = std::chrono::high_resolution_clock::now();
    for (long i = 0; i < num_operations; ++i) {
        result -= 1;
    }
    end_time = std::chrono::high_resolution_clock::now();
    elapsed = end_time - start_time;
    std::cout << "Time taken for 100 million subtractions: " << elapsed.count() << " seconds" << std::endl;

    // Multiplication
    result = 1;
    start_time = std::chrono::high_resolution_clock::now();
    for (long i = 0; i < num_operations; ++i) {
        result *= 1;
    }
    end_time = std::chrono::high_resolution_clock::now();
    elapsed = end_time - start_time;
    std::cout << "Time taken for 100 million multiplications: " << elapsed.count() << " seconds" << std::endl;

    // Division
    result = num_operations;
    start_time = std::chrono::high_resolution_clock::now();
    for (long i = 0; i < num_operations; ++i) {
        result /= 1;
    }
    end_time = std::chrono::high_resolution_clock::now();
    elapsed = end_time - start_time;
    std::cout << "Time taken for 100 million divisions: " << elapsed.count() << " seconds" << std::endl;

    return 0;
}

// Time taken for 100 million additions: 0.117577 seconds
// Time taken for 100 million subtractions: 0.0874213 seconds
// Time taken for 100 million multiplications: 0.0875261 seconds
// Time taken for 100 million divisions: 0.202164 seconds