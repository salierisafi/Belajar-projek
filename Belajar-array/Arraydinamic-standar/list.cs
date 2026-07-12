using System;
using System.Collections.Generic;
class Program {
	static void Main() {
		List<string> buah = new List<string>{"Apel","Pisang"};
		List<string> sayur = new List<string>();
		sayur.Add("Brokoli");
		buah.Add("Mangga");
		int len = buah.Count;
		var ambil = buah[len-1];
		buah.RemoveAt(len-1);
		Console.WriteLine("ambil {0}",ambil);
		Console.WriteLine("buah 1:{0}",buah[0]);
		Console.WriteLine("buah 2:{0}",buah[1]);
		Console.WriteLine("sayur 1:{0}",sayur[0]);
	}
}
