VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} UserForm1 
   Caption         =   "UserForm1"
   ClientHeight    =   3120
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   4710
   OleObjectBlob   =   "根据Excel单元格的文件名称查找目录的文件并将文件复制粘贴到其它文件夹.frx":0000
   StartUpPosition =   1  '所有者中心
End
Attribute VB_Name = "UserForm1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub CommandButton1_Click()
    Dim iTemp1, iTemp2 As Integer

    Dim sTemp1 As String

    Dim totalFiles As Integer

    Dim MyPCName

    sTemp = "D:\MyPcs\" ' 指定的扫描目录，文件夹使用英文，注意，路径的后面有一个\符号
    CopyPath = "D:\goodpc\" '将找到的文件粘贴到这个目录，文件夹使用英文，注意，路径的后面有一个\符号

    Set FS = Application.FileSearch

    With FS
    .LookIn = sTemp
    .Filename = "*.*"
    .MatchAllWordForms = False
    If .Execute(SortBy:=msoSortByFileName, SortOrder:=msoSortOrderAscending) > 0 Then
    totalFiles = .FoundFiles.Count

    For iTemp1 = 1 To totalFiles
    sTemp1 = .FoundFiles(iTemp1)
    iTemp2 = InStrRev(sTemp1, "\")
    If iTemp2 <> 0 Then sTemp1 = Mid(sTemp1, iTemp2 + 1)

    ''s = s & sTemp1'截取文件名
    ''s = s & vbCrLf'给变量加一个回车符

    MyPCName = Left(sTemp1, Len(sTemp1) - 4) '截取文件名的基本名，不要扩展名
      For i = 1 To 1000 '行的最大值
        For j = 1 To 500 '列的最大值
            If (Trim(Worksheets(1).Cells(i, j).Value) = MyPCName) Then
                FileCopy sTemp & sTemp1, CopyPath & sTemp1 '复制粘贴到这个目录
            End If
        Next
      Next
    Next iTemp1

    'MsgBox s '将文件夹的文件名称通过对话框显示出来

    End If
    End With
End Sub



