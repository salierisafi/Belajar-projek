local buah = {"Apel","Pisang"}
local sayur = {}
table.insert(buah, "Mangga")
table.insert(sayur, "Brokoli")
print(buah) -- print alamat
print(sayur) -- print alamat

for i,v in ipairs(buah) do -- print isi
	io.write(v..",")
end
print()
for i,v in ipairs(sayur) do -- print isi
	io.write(v..",")
end
print()
