Attribute VB_Name = "模块1"
Sub 成本报价()
    i = 2
    Do While Cells(i, 1) <> ""
        a = 2
        Do While Sheets("sheet1").Cells(a, 1) <> ""
            If Cells(i, 1) = Sheets("sheet1").Cells(a, 1) Then
                If Cells(i, 3) = Sheets("sheet1").Cells(a, 3) Or Sheets("sheet1").Cells(a, 3) = "" Then
                    Cells(i, 8) = Sheets("sheet1").Cells(a, 4)
                Else
                    If Sheets("sheet1").Cells(a, 3) = Cells(i, 3) + 1 Or Sheets("sheet1").Cells(a, 3) = Cells(i, 3) - 1 Then
                        Cells(i, 9) = Sheets("sheet1").Cells(a, 3)
                        Cells(i, 8) = Sheets("sheet1").Cells(a, 4)
                    End If
                End If
            End If
            a = a + 1
        Loop
        i = i + 1
    Loop
End Sub
