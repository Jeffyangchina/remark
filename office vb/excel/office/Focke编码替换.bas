Attribute VB_Name = "ģ��11"
Sub Focke�����滻()
    For i = 2 To 17637  'ԭ��BOM�е�����
        For j = 2 To 99 '��ͼ�嵥�е�����
            If Cells(i, 4) = Sheets("1").Cells(j, 13) Then
            'ԭ��BOM�ġ�material number����Ԫ�������뷢ͼ�嵥����1�����ġ��������롱��Ԫ���������
            
                Cells(i, 4) = Sheets("1").Cells(j, 1)
                '��material number����Ԫ�����ݡ��滻Ϊ����������롱��Ԫ������
                
                Sheets("1").Cells(j, 14) = Cells(i, 1)
                'ԭ��BOM�ġ�sequence number������д�뷢ͼ�嵥����1��������ʾ��������롱���ǡ�material number��
            End If
        Next
    Next
End Sub
