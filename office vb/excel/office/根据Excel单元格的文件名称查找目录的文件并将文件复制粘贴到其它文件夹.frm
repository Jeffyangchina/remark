VERSION 5.00
Begin {C62A69F0-16DC-11CE-9E98-00AA00574A4F} UserForm1 
   Caption         =   "UserForm1"
   ClientHeight    =   3120
   ClientLeft      =   45
   ClientTop       =   435
   ClientWidth     =   4710
   OleObjectBlob   =   "����Excel��Ԫ����ļ����Ʋ���Ŀ¼���ļ������ļ�����ճ���������ļ���.frx":0000
   StartUpPosition =   1  '����������
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

    sTemp = "D:\MyPcs\" ' ָ����ɨ��Ŀ¼���ļ���ʹ��Ӣ�ģ�ע�⣬·���ĺ�����һ��\����
    CopyPath = "D:\goodpc\" '���ҵ����ļ�ճ�������Ŀ¼���ļ���ʹ��Ӣ�ģ�ע�⣬·���ĺ�����һ��\����

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

    ''s = s & sTemp1'��ȡ�ļ���
    ''s = s & vbCrLf'��������һ���س���

    MyPCName = Left(sTemp1, Len(sTemp1) - 4) '��ȡ�ļ����Ļ���������Ҫ��չ��
      For i = 1 To 1000 '�е����ֵ
        For j = 1 To 500 '�е����ֵ
            If (Trim(Worksheets(1).Cells(i, j).Value) = MyPCName) Then
                FileCopy sTemp & sTemp1, CopyPath & sTemp1 '����ճ�������Ŀ¼
            End If
        Next
      Next
    Next iTemp1

    'MsgBox s '���ļ��е��ļ�����ͨ���Ի�����ʾ����

    End If
    End With
End Sub



