Attribute VB_Name = "ģ��1"
Sub ��ȫ��ϢBOM()
    istart = 686
    
    iend = 1870
    a = 2
    For i = istart To iend
        For j = a To 32281
            If Cells(i, 4) = Sheets("cd_item").Cells(j, 1) Then
                a = j
                Cells(i, 9) = "Y"
                If Cells(i, 7) = "" Then
                    Cells(i, 7) = Sheets("cd_item").Cells(j, 7) '��λ
                End If
                Cells(i, 12) = Sheets("cd_item").Cells(j, 2) '����
                Cells(i, 13) = Sheets("cd_item").Cells(j, 4) '���
                Cells(i, 14) = Sheets("cd_item").Cells(j, 3) '�ͺ�
                Cells(i, 15) = Sheets("cd_item").Cells(j, 8) '��׼��
                Cells(i, 16) = Sheets("cd_item").Cells(j, 14) '����
                Cells(i, 19) = Sheets("cd_item").Cells(j, 21) '����
                If Cells(i, 20) = "" Then
                    Cells(i, 20) = Sheets("cd_item").Cells(j, 16) '��Դ
                End If
                If Cells(i, 21) = "" Then
                    Cells(i, 21) = Sheets("cd_item").Cells(j, 9) '��������1
                End If
                'Cells(i, 21) = Sheets("cd_item").Cells(j, 10) '��������2
                Cells(i, 22) = Sheets("cd_item").Cells(j, 6) '������
                Cells(i, 23) = Sheets("cd_item").Cells(j, 11) '������
                Cells(i, 25) = Sheets("cd_item").Cells(j, 12) '��Ӧ��
                Exit For
            End If
        Next
    Next
End Sub
