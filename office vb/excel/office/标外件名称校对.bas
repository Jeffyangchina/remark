Attribute VB_Name = "模块1"
Sub 标外件名称校对()
    For i = 2 To 461
        For j = 2 To 20556
            If Cells(i, 4) = Sheets("cd_item").Cells(j, 1) Then
                Cells(i, 11) = Sheets("cd_item").Cells(j, 2)
                Exit For
            End If
        Next
    Next
End Sub
