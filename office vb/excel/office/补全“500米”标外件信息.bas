Attribute VB_Name = "ģ��1"
Sub ��ȫ"500��"�������Ϣ()
    For i = 2 To 753
        For j = 2 To 20000
            If Sheets("sheet1").Cells(i, 4) = Sheets("cd_item").Cells(j, 1) Then
                Sheets("sheet1").Cells(i, 8) = Sheets("cd_item").Cells(j, 2)            '����
                Sheets("sheet1").Cells(i, 10) = Sheets("cd_item").Cells(j, 3)           '�ͺ�
                Sheets("sheet1").Cells(i, 9) = Sheets("cd_item").Cells(j, 4)            '���
                Sheets("sheet1").Cells(i, 17) = Sheets("cd_item").Cells(j, 6)           '������
                'Sheets("sheet1").Cells(i, 5) = Sheets("cd_item").Cells(j, 7)           '��λ
                Sheets("sheet1").Cells(i, 11) = Sheets("cd_item").Cells(j, 8)           '��׼��
                Sheets("sheet1").Cells(i, 20) = Sheets("cd_item").Cells(j, 9)           '��������1
                Sheets("sheet1").Cells(i, 21) = Sheets("cd_item").Cells(j, 10)          '��������1
                Sheets("sheet1").Cells(i, 18) = Sheets("cd_item").Cells(j, 11)          '������
                Sheets("sheet1").Cells(i, 22) = Sheets("cd_item").Cells(j, 12)          '��Ӧ��
                Sheets("sheet1").Cells(i, 12) = Sheets("cd_item").Cells(j, 14)          '����
                Sheets("sheet1").Cells(i, 16) = Sheets("cd_item").Cells(j, 16)          '��Դ
                Sheets("sheet1").Cells(i, 15) = Sheets("cd_item").Cells(j, 21)          '����
            End If
        Next
    Next
End Sub
