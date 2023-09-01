fn main() {
    for i in 1..101 {
        let mut output: String = String::new();
        let phrases: [&str; 6] = ["Fizz", "Buzz", "Whizz", "Bang", "Snap", "Naqibo"];
        let numbers: [i32; 6] = [3, 5, 7, 8, 12, 4];
        for j in 0..phrases.len() {
            if i % numbers[j] == 0 {
                output.push_str(phrases[j]);
            }
        }
        if output.len() == 0 {
            output.push_str(&i.to_string());
        }
        println!("{output}");
    }
}
