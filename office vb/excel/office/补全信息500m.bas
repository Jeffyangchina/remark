Attribute VB_Name = "ģ��1"
Sub ��ȫ��Ϣ500m()
    For i = 2 To 1228
        For j = 2 To 20305
            If Cells(i, 3) = Sheets("cd_item").Cells(j, 1) Then
                Cells(i, 8) = Sheets("cd_item").Cells(j, 2) '����
                Cells(i, 10) = Sheets("cd_item").Cells(j, 3) '�ͺ�
                Cells(i, 9) = Sheets("cd_item").Cells(j, 4) '���
                Cells(i, 17) = Sheets("cd_item").Cells(j, 6) '������
                'Cells(i, 5) = Sheets("cd_item").Cells(j, 7) '��λ
                Cells(i, 11) = Sheets("cd_item").Cells(j, 8) '��׼��
                Cells(i, 20) = Sheets("cd_item").Cells(j, 9) '��������1
                Cells(i, 21) = Sheets("cd_item").Cells(j, 10) '��������2
                Cells(i, 18) = Sheets("cd_item").Cells(j, 11) '������
                Cells(i, 22) = Sheets("cd_item").Cells(j, 12) '��Ӧ��
                Cells(i, 12) = Sheets("cd_item").Cells(j, 14) '����
                Cells(i, 16) = Sheets("cd_item").Cells(j, 16) '��Դ
                Cells(i, 15) = Sheets("cd_item").Cells(j, 21) '����
            End If
        Next
    Next
End Sub
