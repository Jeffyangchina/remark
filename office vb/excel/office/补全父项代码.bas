Attribute VB_Name = "ģ��1"
Sub ��ȫ�������()
    For i = 2 To 20000
        If Cells(i, 4) = "" And Cells(i + 1, 4) = "" Then
            Exit For
        Else
            If Cells(i, 21) = "" Then
                If Cells(i, 2) = 0 Then
                    Cells(i, 21) = Cells(i, 4)
                Else
                    For j = 2 To i
                        If Cells(j, 2) = 0 Then
                            Cells(i, 21) = Cells(j, 4)
                        End If
                    Next
                End If
            End If
        End If
    Next
End Sub
