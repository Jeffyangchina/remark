Attribute VB_Name = "ģ��1"
Sub �ԱȺ�����ϼ�Ϊ��()
    i = 4173
    Do While i <> 1
        If Cells(i, 18) = "�ϼ�" Then
            If Cells(i, 19) = 0 Then
                Cells(i, 22) = "Y"
            End If
        Else
            If Cells(i, 3) = Cells(i + 1, 3) Then
                Cells(i, 22) = Cells(i + 1, 22)
            End If
        End If
        i = i - 1
    Loop
End Sub
