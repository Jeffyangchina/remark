Attribute VB_Name = "ģ��1"
Sub ��ȫ��ϢoldK()
    For i = 1 To 3
        For j = 1 To 30
            If Cells(i, j) = "�������" Then
                bz = j
            Else
                If Cells(i, j) = "����" Then
                    bm = j
                Else
                    If Cells(i, j) = "����" Then
                        bt = j
                    Else
                        If Cells(i, j) = "����" Then
                            bc = j
                        End If
                    End If
                End If
            End If
        Next
    Next
    For i = 1 To 3000
        If Sheets("sheet1").Cells(i, 8) = "" And Sheets("sheet1").Cells(i + 1, 8) = "" And Sheets("sheet1").Cells(i + 2, 8) = "" And Sheets("sheet1").Cells(i + 4, 8) = "" Then
            h = i - 1
            Exit For
        End If
    Next
    a = 1
    Do While Cells(a, bz) <> ""
        For i = 1 To h
            Cells(2, 10) = a
            Cells(2, 11) = i
            If Cells(a, bz) = Sheets("sheet1").Cells(i, 8) Then
                Cells(a, bm) = Sheets("sheet1").Cells(i, 10)
                Cells(a, bt) = Sheets("sheet1").Cells(i, 9)
                Cells(a, bc) = Sheets("sheet1").Cells(i, 11)
                Exit For
            End If
        Next
        a = a + 1
    Loop
End Sub
