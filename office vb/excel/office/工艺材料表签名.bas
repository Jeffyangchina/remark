Attribute VB_Name = "ģ��11"
Sub ǩ��()
    y = 129         '��ҳ��
    b = 26          '��ҳ���������
    qs = 24         '��һҳǩ������
    bz = 19         '��������
    sh = 23         '�������
    For i = 2 To y
        Cells(b * (i - 1) + qs, 19) = Cells(qs, 19)
        Cells(b * (i - 1) + qs, 23) = Cells(qs, 23)
    Next
End Sub
