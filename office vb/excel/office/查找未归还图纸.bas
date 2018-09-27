Attribute VB_Name = "模块21"
Sub 查找未归还图纸()
    Cells.Select
    Selection.Interior.ColorIndex = xlNone
    Selection.Sort Key1:=Range("A2"), Order1:=xlAscending, Key2:=Range("B2") _
        , Order2:=xlAscending, Key3:=Range("C2"), Order3:=xlAscending, Header:= _
        xlYes, OrderCustom:=1, MatchCase:=False, Orientation:=xlTopToBottom, _
        SortMethod:=xlPinYin
    i = 2
    Do While Cells(i, 1) <> ""
        If Cells(i, 1) = Cells(i - 1, 1) Then
            Cells(i, 2) = Cells(i - 1, 2)
            Cells(i, 3) = Cells(i - 1, 3)
        End If
        i = i + 1
    Loop
    i = 2
    Do While Cells(i, 1) <> ""
        If Cells(i, 2) <> "" Or Cells(i, 3) = "利用" Then
            Rows(i).Select
            Selection.Delete Shift:=xlUp
            i = i - 1
        End If
        i = i + 1
    Loop
    i = 2
    Do While Cells(i, 1) <> ""
        If Cells(i, 1) = Cells(i - 1, 1) Then
            Rows(i).Select
            Selection.Delete Shift:=xlUp
            i = i - 1
        End If
        i = i + 1
    Loop
    Columns("A:A").Select
    Selection.Insert Shift:=xlToRight
    Cells(1, 1) = "序号"
End Sub

