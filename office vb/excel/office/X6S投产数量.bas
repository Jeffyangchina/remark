Attribute VB_Name = "ģ��1"
Sub Ͷ������()
    For i = 2 To 243
        For j = 2 To 15497
            If Cells(i, 21) = Sheets("����").Cells(j, 1) Then
                Cells(i, 34) = Sheets("����").Cells(j, 2) * 3
                Cells(i, 35) = Sheets("����").Cells(j, 2) * 1
                Cells(i, 36) = Sheets("����").Cells(j, 2) * 1
                Cells(i, 33) = Cells(i, 34) + Cells(i, 35) + Cells(i, 36)
            End If
        Next
    Next
End Sub
