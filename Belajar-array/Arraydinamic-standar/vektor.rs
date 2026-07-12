fn main() {
    let mut buah = vec![String::from("Apel"),"Pisang".to_string()];
    let mut sayur: Vec<String> = Vec::new(); //kosongan
    sayur.push(String::from("Brokoli"));//harus konversi&str ke strinh
    buah.push("Mangga".to_string()); //sama, beda cara
    let ambil: String = buah.pop().unwrap(); //ambil, pake unwrap
    //cara print vektor
    println!("Ambil {}, \nBuah {:?}\nSauyur {:?}",ambil,buah,sayur);

}
