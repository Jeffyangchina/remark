Attribute VB_Name = "模块2"
Sub 显示各零部件工艺条数()
    For i = 2 To 22000
       If Cells(i, 1) <> "" Then
            If Cells(i, 3) = "" Then
                If Cells(i, 2) <> Cells(i - 1, 2) And Cells(i, 2) <> "" Then
                    Cells(i, 3) = 1
                Else
                    For j = 1 To 5000
                        If Cells(i + j - 1, 3) <> "" Then
                            Exit For
                        Else
                            For a = i To i + j - 1
                                Cells(a, 3) = j + 1
                                If Cells(i - 1, 2) = Cells(i, 2) And Cells(i - 1, 3) = j Then
                                    Cells(i - 1, 3) = Cells(i, 3)
                                Else
                                    If Cells(i, 2) = "" And Cells(i - 1, 3) = j Then
                                        Cells(i - 1, 3) = Cells(i, 3)
                                    End If
                                End If
                            Next
                        End If
                    Next
                End If
            End If
        Else
            Exit For
        End If
    Next
End Sub
