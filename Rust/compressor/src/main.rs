use flate2::write::GzEncoder;
use flate2::Compression;
use std::env::args;
use std::fs::File;
use std::io::copy;
use std::io::BufReader;
use std::time::Instant; //use for timing

fn main() {
    
    // checks the cargo command to see if a source and target file name is given along with cargo command i.e. run
    if args().len() != 3 {
        eprintln!("Usage: `source` `target`");
        return;
    }

    // i have no idea how this works
    let mut input = BufReader::new(File::open(args().nth(1).unwrap()).unwrap());
    let output = File::create(args().nth(2).unwrap()).unwrap();
    let mut encoder = GzEncoder::new(output, Compression::default());
    let start = Instant::now();
    copy(&mut input, &mut encoder).unwrap();
    let output = encoder.finish().unwrap();

    // outputting file sizes and time taken
    println!("Source len: {:?}", input.get_ref().metadata().unwrap().len());
    println!("Target len: {:?}", output.metadata().unwrap().len());
    println!("Elapsed time: {:?}", start.elapsed());
}
