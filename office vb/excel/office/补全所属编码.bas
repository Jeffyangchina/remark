Attribute VB_Name = "Ä£¿é1"
Sub ²¹È«ËùÊô±àÂë()
    For i = 2 To 50000
        If Cells(i, 4) = "" And Cells(i + 1, 4) = "" And Cells(i + 2, 4) = "" Then
            Exit For
        Else
            If Cells(i, 2) = 0 Then
                    Cells(i, 29) = ""
                    a = i
            Else
                For j = a To i
                    If Cells(j, 2) = Cells(i, 2) - 1 Then
                            Cells(i, 29) = Cells(j, 4)
                    End If
                Next
            End If
        End If
    Next
End Sub
