Attribute VB_Name = "ģ��1"
Sub ����ƥ��()
    For i = 2 To 17609     'BOM����
        For j = 2 To 5830      '����������
            If Cells(i, 4) = Sheets("sheet1").Cells(j, 1) And Sheets("sheet1").Cells(j, 3) = "" Then
                Cells(i, 32) = Sheets("sheet1").Cells(j, 2)
                Sheets("sheet1").Cells(j, 3) = "Y"
            End If
        Next
    Next
End Sub
