Attribute VB_Name = "ģ��1"
Sub �������ñ�ת��ΪPZ()
    az = 89     '�������ñ�����
    ba = 9      '�������ñ��û���ʼ����
    bz = 11     '�������ñ��û���ֹ����
    i = 1
    For a = 2 To az
        For b = ba To bz
            i = (a - 2) * (bz - ba + 1) + (b - ba + 1)  '����iΪ��a-2��*�û�����+��b-�û���ʼ����+1��
            Cells(i, 2) = Sheets("BOM1").Cells(a, 1)
            Cells(i, 4) = Sheets("BOM1").Cells(a, 2)
            Cells(i, 5) = Sheets("BOM1").Cells(a, b)
            Cells(i, 10) = Sheets("BOM1").Cells(1, b)
            Cells(i, 9) = Sheets("BOM1").Cells(a, 8) & Sheets("BOM1").Cells(1, b)
            Cells(i, 1) = 2
            Sheets("BOM1").Cells(a, b) = ""
        Next
    Next
End Sub


