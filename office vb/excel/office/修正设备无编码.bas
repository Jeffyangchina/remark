Attribute VB_Name = "ģ��1"
Sub �����豸�ޱ���()
Attribute �����豸�ޱ���.VB_Description = "zch4537 ��¼�ĺ� 2006-4-11"
Attribute �����豸�ޱ���.VB_ProcData.VB_Invoke_Func = " \n14"
    For j = 1 To 60
        If Cells(1, j) = "�豸" Then
            a = j
        End If
    Next
    For i = 2 To 60000
        If Cells(i, a) <> "" Then
            Select Case Cells(i, a)
                Case "�ӽ�"
                    Cells(i, a) = "�ӽ�(EE30)"
                Case "�͹�"
                    Cells(i, a) = "����(EB00)"
                Case "����"
                    Cells(i, a) = "����(EF00)"
                Case "��ǯ"
                    Cells(i, a) = "��ǯ(EX22)"
                Case "ƽ��"
                    Cells(i, a) = "ƽ��(EX10)"
                Case "ǯ��"
                    Cells(i, a) = "ǯ��(EX21)"
                Case "�ȹ�"
                    Cells(i, a) = "�ȹ�(ED00)"
                Case "ί��"
                    Cells(i, a) = "ί��(E000)"
                Case "��ϳ"
                    Cells(i, a) = "��ϳ(E261)"
                Case "��ϳ"
                    Cells(i, a) = "��ϳ(E211)"
                Case "����ĥ"
                    Cells(i, a) = "M1020A(E481)"
            End Select
        End If
    Next
End Sub
