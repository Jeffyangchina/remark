Attribute VB_Name = "ģ��1"
Sub Focke���ݱȶԺ�����()
Attribute Focke���ݱȶԺ�����.VB_Description = "���� zch4537 ¼�ƣ�ʱ��: 2010-7-16"
Attribute Focke���ݱȶԺ�����.VB_ProcData.VB_Invoke_Func = " \n14"

    a = 1474        '������
    
    Columns("AI:AI").Select
    Selection.Cut
    Columns("AH:AH").Select
    Selection.Insert Shift:=xlToRight
    Columns("AL:AL").Select
    Selection.Cut
    Columns("AI:AI").Select
    Selection.Insert Shift:=xlToRight
    For i = 2 To a
        If Cells(i, 36) <> "" Then
            Cells(i, 39) = Cells(i, 36)
            Cells(i, 36) = ""
        End If
        If Cells(i, 37) <> "" Then
            Cells(i, 39) = Cells(i, 37)
            Cells(i, 37) = ""
        End If
        If Cells(i, 38) <> "" And Cells(i, 39) <> "�汾����" Then
            Cells(i, 39) = Cells(i, 38)
            Cells(i, 38) = ""
        End If
    Next
End Sub
