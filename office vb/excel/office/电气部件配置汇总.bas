Attribute VB_Name = "ģ��1"
Sub �����������û���()
    For i = 2 To 1666   'BOM����
        For j = 2 To 41  '��������
            If Cells(i, 21) = Sheets("PZ").Cells(j, 1) Then
                For a = 23 To 28   '���ܱ����û���
                    For b = 9 To 16 '���ñ����û���
                        If Cells(1, a) = Sheets("PZ").Cells(1, b) Then
                            Cells(i, a) = Sheets("PZ").Cells(j, b)
                            Sheets("PZ").Cells(j, 4) = ""
                        End If
                    Next
                Next
            End If
        Next
    Next
End Sub
