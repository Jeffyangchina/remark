Attribute VB_Name = "ģ��111"
Sub Focke��������()
    For i = 2 To 99  'ԭ��BOM�е�����
        For j = 2 To 99 '��ͼ�嵥�е�����
            If Cells(i, 4) = Sheets("1").Cells(j, 1) Then
            'ԭ��BOM�ġ�material number����Ԫ�������뷢ͼ�嵥����1�����ġ�������롱��Ԫ���������

                Sheets("1").Cells(j, 14) = Cells(i, 5)
                '��������
                
                Cells(i, 6) = "Y"
                '�����������
                
            End If
        Next
    Next
End Sub
