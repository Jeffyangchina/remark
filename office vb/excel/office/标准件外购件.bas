Attribute VB_Name = "Ä£¿é1"
Sub H()
    For i = 2 To 17150
        If Cells(i, 5) = "" Then
            For a = 2 To 18168
                If Cells(i, 3) = Sheets("sheet2").Cells(a, 1) Then
                    For j = 5 To 13
                        For b = 2 To 8
                            If Cells(1, j) = Sheets("sheet2").Cells(1, b) Then
                                Cells(i, j) = Sheets("sheet2").Cells(a, b)
                                Exit For
                            End If
                        Next
                    Next
                    Exit For
                End If
            Next
        End If
    Next
End Sub
