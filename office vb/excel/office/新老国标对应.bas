Attribute VB_Name = "ģ��1"
Sub ���Ϲ����Ӧ()
    For i = 2 To 1874
        If Cells(i, 4) <> "" Then
            For j = 2 To 105
                If Cells(i, 15) = Sheets("gb").Cells(j, 2) Then
                    Cells(i, 5) = Sheets("gb").Cells(j, 1)
                End If
            Next
        End If
    Next
End Sub
