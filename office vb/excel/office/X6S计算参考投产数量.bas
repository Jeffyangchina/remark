Attribute VB_Name = "ģ��11"
Sub ����ο�Ͷ������()
    a = 1105          'aΪ������
    For i = 2 To a
        For j = 2 To i
            If Cells(i, 29) = Cells(j, 4) Then
                If Cells(i, 2) = 3 Then
                    Cells(i, 37) = Cells(i, 6) * Cells(j, 33)
                    Cells(i, 38) = Cells(i, 6) * Cells(j, 34)
                    Cells(i, 39) = Cells(i, 6) * Cells(j, 35)
                    Cells(i, 40) = Cells(i, 6) * Cells(j, 36)
                Else
                    If Cells(i, 2) > 3 Then
                        Cells(i, 37) = Cells(i, 6) * Cells(j, 37)
                        Cells(i, 38) = Cells(i, 6) * Cells(j, 38)
                        Cells(i, 39) = Cells(i, 6) * Cells(j, 39)
                        Cells(i, 40) = Cells(i, 6) * Cells(j, 40)
                    End If
                End If
            End If
        Next
    Next
End Sub
