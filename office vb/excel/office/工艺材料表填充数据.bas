Attribute VB_Name = "Ä£¿é2"
Sub Ìî³äÊý¾Ý()
For x = 0 To 2
    y = 1 + 26 * x
    Sheets("sheet1").Cells(y, 26) = Cells(y + 1, 12)
    Sheets("sheet1").Cells(y + 1, 26) = Cells(y + 1, 13)
    Sheets("sheet1").Cells(y + 1, 32) = Cells(y + 1, 14)
    Sheets("sheet1").Cells(y + 1, 35) = Cells(y + 1, 15)
    For i = 1 To 18
        Sheets("sheet1").Cells(i + 3, 2) = Cells(i, 1)
        Sheets("sheet1").Cells(i + 3, 3) = Cells(i, 2)
        Sheets("sheet1").Cells(i + 3, 5) = Cells(i, 3)
        Sheets("sheet1").Cells(i + 3, 7) = Cells(i, 4)
        Sheets("sheet1").Cells(i + 3, 8) = Cells(i, 5)
        Sheets("sheet1").Cells(i + 3, 10) = Cells(i, 6)
        Sheets("sheet1").Cells(i + 3, 12) = Cells(i, 7)
        Sheets("sheet1").Cells(i + 3, 13) = Cells(i, 8)
        Sheets("sheet1").Cells(i + 3, 24) = Cells(i, 9)
        Sheets("sheet1").Cells(i + 3, 28) = Cells(i, 10)
        Sheets("sheet1").Cells(i + 3, 32) = Cells(i, 11)
    Next
End Sub
