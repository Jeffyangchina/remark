VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "ThisDocument"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Sub bplot()

Dim cadpth As String
Dim pdfpth As String
Dim i As Integer


Dim wdapp As Word.Application '����word�ӿ�
Dim wdbook As Word.Document
Dim wdbook2 As Word.Document
Dim xlsapp As New Excel.Application

    Dim xlsbook1 As Excel.Workbook

    Dim xlssheet1 As Excel.Worksheet

 Dim xlssheet2 As Excel.Worksheet
 
    Dim daima As String, v As String, o As String, p As String, w As String
    

    Dim j As Integer, n As Integer, l As Integer

    Set xlsbook1 = xlsapp.Workbooks.Open("E:\BITMAP\1\1.xls")

    Set xlssheet1 = xlsbook1.Worksheets("sheet5")
    
    
   
Set wdapp = CreateObject("Word.Application") '����Word




MyPath = "E:\BITMAP\1\"
MyFile = Dir(MyPath & "���㿨Ƭ.doc")


'Do While MyFile <> ""
cadpth = MyPath & MyFile
Set wdbook = Documents.Open(cadpth)
Set wdbook2 = Documents.Open("E:\BITMAP\1\1.doc")
  For i = 2 To 500
    daima = xlssheet1.Cells(i, 4)
    daima2 = xlssheet1.Cells(i + 1, 4)
    v = xlssheet1.Cells(i, "K") '��������
   
       
    o = xlssheet1.Cells(i, "L") '�ͺ�
    p = xlssheet1.Cells(i, "G") '����ͼ��
    w = xlssheet1.Cells(i, "I") '��������
   
    If daima2 <> "" Then
      Set myrange = wdbook.Tables(i - 1).Range
      myrange.Copy
      Set myrange = wdbook.Content

      myrange.Paragraphs.Add '����һ���հ׶��䣬���ǼӸ��س�
      myrange.Paragraphs.Add
      myrange.Collapse (wdCollapseEnd)

      myrange.Paste
     End If
    If daima <> "" Then
      Set myrange = wdbook.Tables(i - 1).Range
      With myrange
      n = myrange.Words.Count
      l = 1
      For j = 15 To n
      
       If l < 6 Then
      If .Words(j).Text = "yang" And l = 1 Then
     .Words(j).Text = daima
     l = l + 1
      End If
      
      If .Words(j).Text = "yang" And l = 2 Then
        .Words(j).Text = v
        l = l + 1
      End If
      
      If .Words(j).Text = "yang" And l = 3 Then
      .Words(j).Text = w
      l = l + 1
      End If
      
    
      If .Words(j).Text = "yang" And l = 4 Then
       .Words(j).Text = o
       l = l + 1
      End If
      
     If .Words(j).Text = "yang" And l = 5 Then
      .Words(j).Text = "  " & p & "  "
          l = l + 1
      End If
     
     End If
     Next j
   
     End With
     'Set myrange = wdbook2.Tables(i - 1).Range
      'Set myrange = myrange.Rows(6).Cells(1).Range 'ѡ�е����еĵ�һ����Ԫ��
     ' myrange.Copy

      'Set myrange = wdbook.Tables(i - 1).Range '�ڵ������ڵĵ�4���ڲ���ͼƬ

    ' Set myrange = myrange.Rows(6).Cells(1).Range
     'Set myrange = myrange.Paragraphs(3).Range
    ' myrange.Paste
    End If
On Error Resume Next
  Next i
wdbook.Save
wdbook.Close


 xlsbook1.Close

    xlsapp.Quit
wdapp.Quit
End Sub






