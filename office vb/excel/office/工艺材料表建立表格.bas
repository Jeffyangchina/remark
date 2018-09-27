Attribute VB_Name = "模块1"
Sub 建立表格()
Attribute 建立表格.VB_Description = "宏由 微软用户 录制，时间: 2006-5-8"
Attribute 建立表格.VB_ProcData.VB_Invoke_Func = " \n14"
    Dim b As String, c As String, m1 As String, m As String, n As String
    Dim n1 As String, n2 As String, d1 As String, d2 As String, d As String
    For a = 1 To 2
        b = 1 + 26 * a
        c = "A" + b
        Range("A1:AJ26").Select
        Selection.Copy
        Range(c).Select
        ActiveSheet.Paste
        m1 = 4 + 26 * a
        m = m1 + ":" + m1
        Rows(m).Select
        Selection.RowHeight = 54
        n1 = 23 + 26 * a
        n2 = 25 + 26 * a
        n = n1 + ":" + n2
        Rows(n).Select
        Selection.RowHeight = 18
        d1 = 28 + 26 * a
        d2 = 54 + 26 * a
        d = d1 + ":" + d2
        Rows(d).Select
        Selection.RowHeight = 27
    Next
End Sub
