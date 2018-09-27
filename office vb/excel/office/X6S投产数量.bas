Attribute VB_Name = "模块1"
Sub 投产数量()
    For i = 2 To 243
        For j = 2 To 15497
            If Cells(i, 21) = Sheets("反排").Cells(j, 1) Then
                Cells(i, 34) = Sheets("反排").Cells(j, 2) * 3
                Cells(i, 35) = Sheets("反排").Cells(j, 2) * 1
                Cells(i, 36) = Sheets("反排").Cells(j, 2) * 1
                Cells(i, 33) = Cells(i, 34) + Cells(i, 35) + Cells(i, 36)
            End If
        Next
    Next
End Sub
