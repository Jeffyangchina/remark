Attribute VB_Name = "ģ��1"
Sub �������û���()
    For i = 2 To 24846    'BOM����
        For j = 2 To 1610  '��������
            If Cells(i, 31) = Sheets("PZ").Cells(j, 2) Then
                For a = 32 To 39   '���ܱ����û���
                    If Cells(1, a) = Sheets("PZ").Cells(j, 10) Then
                        Cells(i, a) = Sheets("PZ").Cells(j, 5)
                        Sheets("PZ").Cells(j, 6) = "GP"
                    End If
                Next
            End If
        Next
    Next
End Sub
