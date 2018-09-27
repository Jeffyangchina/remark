Attribute VB_Name = "Ä£¿é1"
Sub h()
    Const sh1 As Integer = 140, sh2 As Integer = 120
    Dim i As Integer
    Dim j As Integer
    For j = 1 To sh2
        If Sheet2.Cells(j, 1) = Sheet2.Cells(j + 1, 1) Then
            Sheet2.Cells(1, 6) = "ÓÐÖØ¸´"
            Sheet2.Cells(j, 6) = 1
        End If
    Next
    For i = 1 To sh1
        For j = 1 To sh2
            If Sheet1.Cells(i, 2) = Sheet2.Cells(j, 1) Then
                Sheet1.Cells(i, 8) = j
                Sheet2.Cells(j, 5) = 1
                Sheet1.Cells(i, 3) = Sheet2.Cells(j, 2)
                Sheet1.Cells(i, 4) = Sheet2.Cells(j, 3)
            Else
                If Sheet1.Cells(i, 3) = "please to input" Then
                    Sheet1.Cells(i, 3) = ""
                    Sheet1.Cells(i, 4) = ""
                End If
            End If
        Next
    Next
End Sub
