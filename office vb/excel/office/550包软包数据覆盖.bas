Attribute VB_Name = "模块1"
Sub 软包数据覆盖()
    For i = 2 To 1425
        For j = 2 To 58305
            If Cells(i, 4) = Sheets("all").Cells(j, 4) Then
                Cells(i, 24) = "YJ"
                Cells(i, 11) = Sheets("all").Cells(j, 11)
                Cells(i, 12) = Sheets("all").Cells(j, 12)
                Cells(i, 14) = Sheets("all").Cells(j, 14)
                Cells(i, 15) = Sheets("all").Cells(j, 15)
                Cells(i, 16) = Sheets("all").Cells(j, 16)
                Cells(i, 17) = Sheets("all").Cells(j, 17)
                Cells(i, 18) = Sheets("all").Cells(j, 18)
                Cells(i, 19) = Sheets("all").Cells(j, 19)
                Cells(i, 20) = Sheets("all").Cells(j, 20)
                Exit For
            End If
        Next
    Next
End Sub
