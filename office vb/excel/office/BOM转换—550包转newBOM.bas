Attribute VB_Name = "ģ��1"
Sub BOMת����550��תnewBOM()
Attribute BOMת����550��תnewBOM.VB_Description = "���� zch4537 ¼�ƣ�ʱ��: 2010-7-14"
Attribute BOMת����550��תnewBOM.VB_ProcData.VB_Invoke_Func = " \n14"
    Columns("E:E").Select
    Selection.Insert Shift:=xlToRight
    Columns("M:O").Select
    Selection.Insert Shift:=xlToRight
    Columns("R:R").Select
    Selection.Insert Shift:=xlToRight
    Columns("W:W").Select
    Selection.Cut
    Columns("U:U").Select
    Selection.Insert Shift:=xlToRight
    Columns("W:W").Select
    Selection.Insert Shift:=xlToRight
    Columns("AA:AD").Select
    Selection.Insert Shift:=xlToRight
    Cells(1, 5) = "ͼ��"
    Cells(1, 13) = "��    ��"
    Cells(1, 14) = "��    ��"
    Cells(1, 15) = "��׼��"
    Cells(1, 18) = "������λ"
    Cells(1, 23) = "������"
    Cells(1, 27) = "��Ŀ����"
    Cells(1, 28) = "����"
    Cells(1, 29) = "��������"
    Cells(1, 30) = "��ע"
End Sub
