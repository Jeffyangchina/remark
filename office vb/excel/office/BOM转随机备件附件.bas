Attribute VB_Name = "ģ��1"
Sub BOMת�����������()
Attribute BOMת�����������.VB_Description = "ZCH4537 ��¼�ĺ� 2007-8-21"
Attribute BOMת�����������.VB_ProcData.VB_Invoke_Func = " \n14"
    Range("B:C,G:K,P:R,T:AA,AB:AC,AE:AF").Select
    Range("AE1").Activate
    Selection.Delete Shift:=xlToLeft
    ActiveWindow.SmallScroll ToRight:=-22
    Columns("C:C").Select
    Selection.ColumnWidth = 24
    ActiveWindow.SmallScroll ToRight:=6
    Columns("J:J").Select
    Selection.ColumnWidth = 16
    Cells.Select
    With Selection
        .VerticalAlignment = xlBottom
        .WrapText = True
        .Orientation = 0
        .AddIndent = False
        .ShrinkToFit = False
        .MergeCells = False
    End With
End Sub
