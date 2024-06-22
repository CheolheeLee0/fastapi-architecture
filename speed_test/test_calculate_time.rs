use std::time::Instant;

fn main() {
    // Number of arithmetic operations to perform
    let num_operations = 100_000_000;

    // Addition
    let start_time = Instant::now();
    let mut result = 0;
    for _ in 0..num_operations {
        result += 1;
    }
    let end_time = Instant::now();
    println!("Time taken for 100 million additions: {:.4} seconds", (end_time - start_time).as_secs_f64());

    // Subtraction
    let start_time = Instant::now();
    result = num_operations;
    for _ in 0..num_operations {
        result -= 1;
    }
    let end_time = Instant::now();
    println!("Time taken for 100 million subtractions: {:.4} seconds", (end_time - start_time).as_secs_f64());

    // Multiplication
    let start_time = Instant::now();
    result = 1;
    for _ in 0..num_operations {
        result *= 1;
    }
    let end_time = Instant::now();
    println!("Time taken for 100 million multiplications: {:.4} seconds", (end_time - start_time).as_secs_f64());

    // Division
    let start_time = Instant::now();
    result = num_operations;
    for _ in 0..num_operations {
        result /= 1;
    }
    let end_time = Instant::now();
    println!("Time taken for 100 million divisions: {:.4} seconds", (end_time - start_time).as_secs_f64());
}
