Attribute VB_Name = "模块12"
Sub 比较父项代码()
    Columns("V:V").Select
    Selection.TextToColumns Destination:=Range("V1"), DataType:=xlFixedWidth, _
        FieldInfo:=Array(Array(0, 1), Array(5, 1), Array(17, 1))
    Selection.Delete Shift:=xlToLeft
    Columns("W:W").Select
    Selection.Delete Shift:=xlToLeft
    ActiveCell.FormulaR1C1 = "=AND(RC[-2]=RC[-1])"
End Sub
