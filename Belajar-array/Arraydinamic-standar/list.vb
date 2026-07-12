Imports System
Imports System.Collections.Generic

Module Program
Sub Main()
	Dim buah As New List (Of String) From {"Apel","Pisang"}
	Dim sayur As New List (Of String)()
	sayur.Add("Brokoli")
	buah.Add("Mangga")
	Dim length As Integer = buah.Count
	Dim ambil As String = buah(length-1)
	buah.RemoveAt(length-1)
	Console.WriteLine("ambil " & ambil)
	Console.WriteLine("buah 1:" & buah(0))
	Console.WriteLine("buah 2:" & buah(1))
	Console.WriteLine("sayur 1:" & sayur(0))
End Sub
End Module

