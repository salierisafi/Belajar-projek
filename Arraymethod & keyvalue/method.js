const arr = [
        "1-ahmad-python,2008",
        "3-alfin-javascript,2007",
        "4-bayu-python,2008",
        "1-ahmad-python,2008",
        "2-bagas-c,2006",
        "3-alfin-javascript,2007",
        "3-alfin-javascript,2007",
        "5-dimas-csharp,2007"
        ];

let arrunik = [...new Set(arr)];
console.log(arrunik);
arrunik = [];

for (let i=0;i<arr.length;i++){
	// untuk bikin tidak ada elemen yg sama
	// ngecek apakah sebuah elemen ada dalam array :
	if (!arrunik.includes(arr[i])){
		arrunik.push(arr[i]);
	}
}

console.log(arrunik);

let splitarr = [];
for (let i = 0;i<arrunik.length;i++) {
    x = arrunik[i].split("-")
    splitarr.push(x);
}

console.log(splitarr);

let temp = [1];
let i = 0;
while (true) {
	let indikator = parseInt(splitarr[i][0])
	let temp2 = splitarr[i];
	splitarr[i] = temp;
	temp = temp2;
	if (indikator.toString() === splitarr[indikator-1][0]){
		i++;
	}
	else{
		i = parseInt(temp2[0])-1;
	}
	if (i>=splitarr.length) break;
}
console.log(splitarr);

let arrdict = [];
for (let j=0;j<splitarr.length;j++){
    let tempdict = {};
    tempdict.no = splitarr[j][0];
    tempdict.name = splitarr[j][1];
    tempdict.lang = splitarr[j][2].split(",")[0];
	//slicing, slice(awal,akhir) index "," +1 jadi awal, akhir = panjang array
    tempdict.year = splitarr[j][2].slice(splitarr[j][2].indexOf(",")+1,splitarr[j][2].length)
    arrdict.push(tempdict);
}
console.log(arrdict);


