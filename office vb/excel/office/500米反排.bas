Attribute VB_Name = "模块11"
Sub 数量统计()
    Const jzm As String = "合计"
    Columns("D:D").Select
    Selection.NumberFormatLocal = "0_);[红色](0)"
    Columns("F:F").Select
    Selection.Insert Shift:=xlToRight
    Selection.Insert Shift:=xlToRight
    Columns("E:E").Select
    Selection.Copy
    Columns("G:G").Select
    ActiveSheet.Paste
    For l = 1 To 60
        If Cells(1, l + 1) = 0 And Cells(1, l + 2) = 0 And Cells(1, l + 3) = 0 Then
            lall = l
            Exit For
        End If
    Next
    For H = 1 To 65000
        If Cells(H + 1, 4) = 0 And Cells(H + 2, 4) = 0 And Cells(H + 3, 4) = 0 Then
            heall = H
            Exit For
        End If
    Next

    MsgBox "共" & heall & "行信息"
    MsgBox "共" & lall - 2 & "列信息"
    Cells(2, 6) = 1
    k = 1
    a = 0
    For i = 3 To heall
    If Cells(i, 2) = 0 Then
        Cells(i, 6) = 1
    Else
        If Cells(i, 2) = Cells(i - 1, 2) + 1 Then
            Cells(i, 6) = Cells(i - 1, 7)
        Else
            If Cells(i, 2) = Cells(i - 1, 2) Then
                Cells(i, 6) = Cells(i - 1, 6)
            Else
                If Cells(i, 2) < Cells(i - 1, 2) Then
                    For j = 2 To i
                        If Cells(i, 2) = Cells(j, 2) + 1 Then
                            a = j
                        End If
                    Next
                End If
                If a <> 0 Then
                    Cells(i, 6) = Cells(a, 7)
                End If
            End If
        End If
    End If
        Cells(i, 7) = Cells(i, 5) * Cells(i, 6)
    Next
    Columns("E:F").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    Cells.Select
    Selection.Sort Key1:=Range("D2"), Order1:=xlAscending, Key2:=Range("O2") _
        , Order2:=xlAscending, Key3:=Range("Y2"), Order3:=xlAscending, Header:= _
        xlYes, OrderCustom:=1, MatchCase:=False, Orientation:=xlTopToBottom, _
        SortMethod:=xlPinYin
    Cells.Select
    Selection.Sort Key1:=Range("D2"), Order1:=xlAscending, Key2:=Range("AB2") _
        , Order2:=xlAscending, Key3:=Range("B2"), Order3:=xlAscending, Header:= _
        xlYes, OrderCustom:=1, MatchCase:=False, Orientation:=xlTopToBottom, _
        SortMethod:=xlPinYin
    Columns("F:F").Select
    Selection.Insert Shift:=xlToRight
    Selection.Insert Shift:=xlToRight
    Selection.Insert Shift:=xlToRight
    Cells(1, 6) = "用于部件"
    Cells(1, 7) = "总数量"
    For i = 2 To heall + 1
        If Cells(i, 4) = Cells(i - 1, 4) Then
            Cells(i, 7) = Cells(i - 1, 7) + Cells(i, 5)
            If Cells(i, 31) = Cells(i - 1, 31) And Cells(i, 2) = Cells(i - 1, 2) And Cells(i, 18) = Cells(i - 1, 18) And Cells(i, 28) = Cells(i - 1, 28) Then
                Cells(i, 6) = Cells(i - 1, 6) + Cells(i, 5)
                Cells(i - 1, 8) = 1
            Else
                Cells(i, 6) = Cells(i, 5)
            End If
        Else
            Cells(i, 6) = Cells(i, 5)
            Cells(i, 7) = Cells(i, 5)
            If Cells(i, 4) <> Cells(i - 1, 4) And Cells(i, 8) <> 1 Then
                For j = 1 To lall + 1
                    Cells(i + heall + 1, j) = Cells(i - 1, j)
                Next
            End If
        End If
        Cells(i, 5) = Cells(i, 6)
        Cells(i + heall + 1, 5) = Cells(i + heall + 1, 7)
        Cells(i + heall + 1, lall + 2) = Cells(i + heall + 1, lall + 1)
        Cells(i + heall + 1, lall + 1) = jzm
    Next
    Cells.Select
    Selection.Sort Key1:=Range("D2"), Order1:=xlDescending, Header:=xlYes, _
        OrderCustom:=1, MatchCase:=False, Orientation:=xlTopToBottom, SortMethod _
        :=xlPinYin
    i = 2
    Do While Cells(i, 4) <> "" Or Cells(i, 24) <> ""
        If Cells(i, 4) = Cells(1, 4) Then
            Rows(i).Select
            Selection.Delete Shift:=xlUp
            i = i - 1
        Else
            If Cells(i, 8) = 1 Then
                Rows(i).Select
                Selection.Delete Shift:=xlUp
                i = i - 1
            Else
                If Cells(i, 4) = "" And Cells(i, 24) <> "" Then
                    Rows(i).Select
                    Selection.Delete Shift:=xlUp
                    i = i - 1
                End If
            End If
        End If
        i = i + 1
    Loop
    Columns("F:H").Select
    Selection.Delete Shift:=xlToLeft
    Cells.Select
    Selection.Sort Key1:=Range("D2"), Order1:=xlAscending, Key2:=Range("O2") _
        , Order2:=xlAscending, Key3:=Range("Y2"), Order3:=xlAscending, Header:= _
        xlYes, OrderCustom:=1, MatchCase:=False, Orientation:=xlTopToBottom, _
        SortMethod:=xlPinYin
    Cells.Select
    Selection.Sort Key1:=Range("D2"), Order1:=xlAscending, Key2:=Range("AB2") _
        , Order2:=xlAscending, Key3:=Range("B2"), Order3:=xlAscending, Header:= _
        xlYes, OrderCustom:=1, MatchCase:=False, Orientation:=xlTopToBottom, _
        SortMethod:=xlPinYin
    Columns("A:A").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    Columns("AB:AB").Select
    Selection.Delete Shift:=xlToLeft
    Columns("C:C").Select
    Selection.Cut
    Columns("A:A").Select
    Selection.Insert Shift:=xlToRight
    Columns("H:L").Select
    Selection.Cut
    Columns("B:B").Select
    Selection.Insert Shift:=xlToRight
    Columns("P:P").Select
    Selection.Cut
    Columns("G:G").Select
    Selection.Insert Shift:=xlToRight
    Columns("O:O").Select
    Selection.Cut
    Columns("H:H").Select
    Selection.Insert Shift:=xlToRight
    Columns("S:U").Select
    Selection.Cut
    Columns("I:I").Select
    Selection.Insert Shift:=xlToRight
    Columns("W:W").Select
    Selection.Cut
    Columns("L:L").Select
    Selection.Insert Shift:=xlToRight
    Columns("X:X").Select
    Selection.Cut
    Columns("N:N").Select
    Selection.Insert Shift:=xlToRight
    Columns("AA:AA").Select
    Selection.Cut
    Columns("O:O").Select
    Selection.Insert Shift:=xlToRight
    Columns("P:P").Select
    Selection.EntireColumn.Hidden = True
    Columns("H:H").Select
    Selection.Cut
    Columns("S:S").Select
    Selection.Insert Shift:=xlToRight
    Columns("W:Y").Select
    Selection.Cut
    Columns("S:S").Select
    Selection.Insert Shift:=xlToRight
    Columns("V:AA").Select
    Selection.EntireColumn.Hidden = True
    Columns("O:O").Select
    Selection.EntireColumn.Hidden = True
    i = 2
    Do While Cells(i, 14) <> ""
        If Cells(i, 1) = "" Then
            Rows(i).Select
            Selection.Delete Shift:=xlUp
            i = i - 1
        End If
        i = i + 1
    Loop
End Sub


