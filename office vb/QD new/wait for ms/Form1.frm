VERSION 5.00
Object = "{248DD890-BB45-11CF-9ABC-0080C7E7B78D}#1.0#0"; "MSWINSCK.OCX"
Begin VB.Form Form1 
   BackColor       =   &H00FFFFFF&
   Caption         =   "IPC CONFIGURATION"
   ClientHeight    =   6150
   ClientLeft      =   60
   ClientTop       =   450
   ClientWidth     =   7440
   LinkTopic       =   "Form1"
   ScaleHeight     =   6150
   ScaleWidth      =   7440
   StartUpPosition =   3  '窗口缺省
   Begin VB.CommandButton Command8 
      BackColor       =   &H00C0C0C0&
      Caption         =   "BACK to IPC05"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   9
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   120
      TabIndex        =   20
      Top             =   3600
      Width           =   735
   End
   Begin VB.CommandButton Command7 
      BackColor       =   &H00C0C0C0&
      Caption         =   "BACK to IPC04"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   9
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   735
      Left            =   120
      TabIndex        =   19
      Top             =   1800
      Width           =   735
   End
   Begin VB.Frame Frame15 
      BackColor       =   &H00C0C000&
      Caption         =   "192.168.1.205"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   2760
      TabIndex        =   18
      Top             =   4800
      Width           =   2895
   End
   Begin VB.Frame Frame14 
      BackColor       =   &H00C0C000&
      Caption         =   "192.168.1.204"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   2760
      TabIndex        =   17
      Top             =   4200
      Width           =   2895
   End
   Begin VB.Frame Frame13 
      BackColor       =   &H00C0C000&
      Caption         =   "192.168.1.203"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   2760
      TabIndex        =   16
      Top             =   3600
      Width           =   2895
   End
   Begin VB.Frame Frame12 
      BackColor       =   &H00C0C000&
      Caption         =   "192.168.1.202"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   2760
      TabIndex        =   15
      Top             =   3000
      Width           =   2895
   End
   Begin VB.CommandButton Command6 
      BackColor       =   &H00C0C0C0&
      Caption         =   "修改"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   5760
      MaskColor       =   &H00C0C0FF&
      Style           =   1  'Graphical
      TabIndex        =   14
      Top             =   4800
      Width           =   1335
   End
   Begin VB.CommandButton Command5 
      BackColor       =   &H00C0C0C0&
      Caption         =   "修改"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   5760
      MaskColor       =   &H00C0C0FF&
      Style           =   1  'Graphical
      TabIndex        =   13
      Top             =   4200
      Width           =   1335
   End
   Begin VB.CommandButton Command4 
      BackColor       =   &H00C0C0C0&
      Caption         =   "修改"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   5760
      MaskColor       =   &H00C0C0FF&
      Style           =   1  'Graphical
      TabIndex        =   12
      Top             =   3600
      Width           =   1335
   End
   Begin VB.CommandButton Command3 
      BackColor       =   &H00C0C0C0&
      Caption         =   "修改"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   5760
      MaskColor       =   &H00C0C0FF&
      Style           =   1  'Graphical
      TabIndex        =   11
      Top             =   3000
      Width           =   1335
   End
   Begin VB.CommandButton Command2 
      BackColor       =   &H00C0C0C0&
      Caption         =   "修改"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   5760
      MaskColor       =   &H00C0C0FF&
      Style           =   1  'Graphical
      TabIndex        =   10
      Top             =   2400
      Width           =   1335
   End
   Begin VB.Frame Frame11 
      BackColor       =   &H00C0C000&
      Caption         =   "QD05"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   960
      TabIndex        =   9
      Top             =   4200
      Width           =   1815
   End
   Begin VB.Frame Frame10 
      BackColor       =   &H00C0C000&
      Caption         =   "QD06"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   960
      TabIndex        =   8
      Top             =   4800
      Width           =   1815
   End
   Begin VB.Frame Frame9 
      BackColor       =   &H00C0C000&
      Caption         =   "QD04"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   960
      TabIndex        =   7
      Top             =   3600
      Width           =   1815
   End
   Begin VB.Frame Frame8 
      BackColor       =   &H00C0C000&
      Caption         =   "QD03"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   960
      TabIndex        =   6
      Top             =   3000
      Width           =   1815
   End
   Begin VB.Frame Frame7 
      BackColor       =   &H00C0C000&
      Caption         =   "QD02"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   960
      TabIndex        =   5
      Top             =   2400
      Width           =   1815
   End
   Begin VB.Frame Frame6 
      BackColor       =   &H00C0C000&
      Caption         =   "192.168.1.201"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   2760
      TabIndex        =   4
      Top             =   2400
      Width           =   2895
   End
   Begin MSWinsockLib.Winsock Winsock1 
      Left            =   7200
      Top             =   1800
      _ExtentX        =   741
      _ExtentY        =   741
      _Version        =   393216
   End
   Begin VB.Frame Frame5 
      BackColor       =   &H00C0C000&
      Caption         =   "192.168.1.200"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   2760
      TabIndex        =   2
      Top             =   1800
      Width           =   2895
   End
   Begin VB.CommandButton Command1 
      BackColor       =   &H00C0C0C0&
      Caption         =   "修改"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   5760
      MaskColor       =   &H00C0C0FF&
      Style           =   1  'Graphical
      TabIndex        =   1
      Top             =   1800
      Width           =   1335
   End
   Begin VB.Frame Frame1 
      BackColor       =   &H00C0C000&
      Caption         =   "QD01"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   400
      Left            =   960
      TabIndex        =   0
      Top             =   1800
      Width           =   1815
   End
   Begin VB.Image Image3 
      Height          =   900
      Left            =   720
      Picture         =   "Form1.frx":0000
      Top             =   960
      Width           =   6480
   End
   Begin VB.Label Label1 
      Alignment       =   2  'Center
      AutoSize        =   -1  'True
      BackColor       =   &H00FFFFC0&
      Caption         =   "Label1"
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   15.75
         Charset         =   134
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   315
      Left            =   3240
      TabIndex        =   3
      Top             =   240
      Width           =   1095
   End
   Begin VB.Image Image1 
      Height          =   1080
      Left            =   0
      Picture         =   "Form1.frx":1EDD
      Stretch         =   -1  'True
      Top             =   5160
      Width           =   7425
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim pcname As String
Dim pcname2 As String
Dim pcip As Variant
Dim pcip0 As String
Dim pcip1 As String
'Private Declare Sub sleep Lib "kernel32.dll" (ByVal dwmilliseconds As Long)
Private Sub waitforms(ms As Long)
Dim s As Long
b = Second(Now)

s = b + ms
If s > 59 Then
s = s - 60
End If

Do
b = Second(Now)
If s = b Then Exit Sub
Loop

End Sub



Private Sub Command1_Click()
f2 = "D:\oracle\ora92\network\admin\tnsnames.ora"
Dim c() As Byte
If Dir(f2, vbDirectory) <> "" Then
Open f2 For Binary As #2
ReDim c(LOF(2) - 1)
Get #2, , c
Close #2
d = StrConv(c, vbUnicode)
d = Replace(d, pcip0, "192.168.1.200")
Open f2 For Output As #2
Print #2, d
Close #2
End If
f1 = "D:\oracle\ora92\network\admin\listener.ora"

Dim a() As Byte
If Dir(f1, vbDirectory) <> "" Then
Open f1 For Binary As #1
ReDim a(LOF(1) - 1)
Get #1, , a
Close #1
b = StrConv(a, vbUnicode)
b = Replace(b, pcname, "QD01")
b = Replace(b, pcname2, "QD01")
Open f1 For Output As #1
Print #1, b
Close #1
Set WshShell = CreateObject("WScript.Shell")
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName", "QD01", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\NV Hostname", "QD01", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\Hostname", "QD01", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\ControlSet001\Control\ComputerName\ComputerName\ComputerName", "QD01", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\AltDefaultDomainName", "QD01", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\DefaultDomainName", "QD01", "REG_SZ"

Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 192.168.1.200 255.255.0.0"), vbHide

waitforms (3)
pcname = WshShell.RegRead("HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName")
pcname2 = LCase(pcname)



MsgBox "Execution success！", vbOKOnly, "RESULT"
Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 192.168.1.200 255.255.0.0"), vbHide
pcip1 = Winsock1.LocalIP
Label1.Caption = " IPC-NAME： " & pcname & "  IPC-IP：" & pcip1
Else
MsgBox "Execution failure！", vbOKOnly, "RESULT"
End If



End Sub

Private Sub Command2_Click()
f2 = "D:\oracle\ora92\network\admin\tnsnames.ora"
Dim c() As Byte
If Dir(f2, vbDirectory) <> "" Then
Open f2 For Binary As #2
ReDim c(LOF(2) - 1)
Get #2, , c
Close #2
d = StrConv(c, vbUnicode)
d = Replace(d, pcip0, "192.168.1.201")
Open f2 For Output As #2
Print #2, d
Close #2
End If
f1 = "D:\oracle\ora92\network\admin\listener.ora"
Dim a() As Byte
If Dir(f1, vbDirectory) <> "" Then
Open f1 For Binary As #1
ReDim a(LOF(1) - 1)
Get #1, , a
Close #1
b = StrConv(a, vbUnicode)
b = Replace(b, pcname, "QD02")
b = Replace(b, pcname2, "QD02")
Open f1 For Output As #1
Print #1, b
Close #1
Set WshShell = CreateObject("WScript.Shell")
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName", "QD02", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\NV Hostname", "QD02", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\Hostname", "QD02", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\ControlSet001\Control\ComputerName\ComputerName\ComputerName", "QD02", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\AltDefaultDomainName", "QD02", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\DefaultDomainName", "QD02", "REG_SZ"
Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 192.168.1.201 255.255.0.0"), vbHide

waitforms (3)


pcname = WshShell.RegRead("HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName")
pcname2 = LCase(pcname)
Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 192.168.1.201 255.255.0.0"), vbHide
pcip1 = Winsock1.LocalIP
Label1.Caption = " IPC-NAME： " & pcname & "  IPC-IP：" & pcip1
MsgBox "Execution success！", vbOKOnly, "RESULT"
Else
MsgBox "Execution failure！", vbOKOnly, "RESULT"
End If



End Sub

Private Sub Command3_Click()
f2 = "D:\oracle\ora92\network\admin\tnsnames.ora"
Dim c() As Byte
If Dir(f2, vbDirectory) <> "" Then
Open f2 For Binary As #2
ReDim c(LOF(2) - 1)
Get #2, , c
Close #2
d = StrConv(c, vbUnicode)
d = Replace(d, pcip0, "192.168.1.202")
Open f2 For Output As #2
Print #2, d
Close #2
End If
f1 = "D:\oracle\ora92\network\admin\listener.ora"
Dim a() As Byte
If Dir(f1, vbDirectory) <> "" Then
Open f1 For Binary As #1
ReDim a(LOF(1) - 1)
Get #1, , a
Close #1
b = StrConv(a, vbUnicode)
b = Replace(b, pcname, "QD03")
b = Replace(b, pcname2, "QD03")
Open f1 For Output As #1
Print #1, b
Close #1
Set WshShell = CreateObject("WScript.Shell")
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName", "QD03", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\NV Hostname", "QD03", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\Hostname", "QD03", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\ControlSet001\Control\ComputerName\ComputerName\ComputerName", "QD03", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\AltDefaultDomainName", "QD03", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\DefaultDomainName", "QD03", "REG_SZ"
Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 192.168.1.202 255.255.0.0"), vbHide
pcname = WshShell.RegRead("HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName")
pcname2 = LCase(pcname)
Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 192.168.1.202 255.255.0.0"), vbHide
waitforms (3)
pcip1 = Winsock1.LocalIP
Label1.Caption = " IPC-NAME： " & pcname & "  IPC-IP：" & pcip1

MsgBox "Execution success！", vbOKOnly, "RESULT"
Else
MsgBox "Execution failure！", vbOKOnly, "RESULT"
End If

End Sub

Private Sub Command4_Click()
f2 = "D:\oracle\ora92\network\admin\tnsnames.ora"
Dim c() As Byte
If Dir(f2, vbDirectory) <> "" Then
Open f2 For Binary As #2
ReDim c(LOF(2) - 1)
Get #2, , c
Close #2
d = StrConv(c, vbUnicode)
d = Replace(d, pcip0, "192.168.1.203")
Open f2 For Output As #2
Print #2, d
Close #2
End If
f1 = "D:\oracle\ora92\network\admin\listener.ora"
Dim a() As Byte
If Dir(f1, vbDirectory) <> "" Then
Open f1 For Binary As #1
ReDim a(LOF(1) - 1)
Get #1, , a
Close #1
b = StrConv(a, vbUnicode)
b = Replace(b, pcname, "QD04")
b = Replace(b, pcname2, "QD04")
Open f1 For Output As #1
Print #1, b
Close #1
Set WshShell = CreateObject("WScript.Shell")
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName", "QD04", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\NV Hostname", "QD04", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\Hostname", "QD04", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\ControlSet001\Control\ComputerName\ComputerName\ComputerName", "QD04", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\AltDefaultDomainName", "QD04", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\DefaultDomainName", "QD04", "REG_SZ"
Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 192.168.1.203 255.255.0.0"), vbHide
pcname = WshShell.RegRead("HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName")
pcname2 = LCase(pcname)
Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 192.168.1.203 255.255.0.0"), vbHide
waitforms (3)

pcip1 = Winsock1.LocalIP
Label1.Caption = " IPC-NAME： " & pcname & "  IPC-IP：" & pcip1

MsgBox "Execution success！", vbOKOnly, "RESULT"
Else
MsgBox "Execution failure！", vbOKOnly, "RESULT"
End If

End Sub

Private Sub Command5_Click()

f2 = "D:\oracle\ora92\network\admin\tnsnames.ora"
Dim c() As Byte
If Dir(f2, vbDirectory) <> "" Then
Open f2 For Binary As #2
ReDim c(LOF(2) - 1)
Get #2, , c
Close #2
d = StrConv(c, vbUnicode)
d = Replace(d, pcip0, "192.168.1.204")
Open f2 For Output As #2
Print #2, d
Close #2
End If
f1 = "D:\oracle\ora92\network\admin\listener.ora"
Dim a() As Byte
If Dir(f1, vbDirectory) <> "" Then
Open f1 For Binary As #1
ReDim a(LOF(1) - 1)
Get #1, , a
Close #1
b = StrConv(a, vbUnicode)
b = Replace(b, pcname, "QD05")
b = Replace(b, pcname2, "QD05")
Open f1 For Output As #1
Print #1, b
Close #1
Set WshShell = CreateObject("WScript.Shell")
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName", "QD05", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\NV Hostname", "QD05", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\Hostname", "QD05", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\ControlSet001\Control\ComputerName\ComputerName\ComputerName", "QD05", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\AltDefaultDomainName", "QD05", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\DefaultDomainName", "QD05", "REG_SZ"
Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 192.168.1.204 255.255.0.0"), vbHide
waitforms (3)
pcname = WshShell.RegRead("HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName")
pcname2 = LCase(pcname)
Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 192.168.1.204 255.255.0.0"), vbHide
pcip1 = Winsock1.LocalIP
Label1.Caption = " IPC-NAME： " & pcname & "  IPC-IP：" & pcip1

MsgBox "Execution success！", vbOKOnly, "RESULT"
Else
MsgBox "Execution failure！", vbOKOnly, "RESULT"
End If


End Sub

Private Sub Command6_Click()
f2 = "D:\oracle\ora92\network\admin\tnsnames.ora"
Dim c() As Byte
If Dir(f2, vbDirectory) <> "" Then
Open f2 For Binary As #2
ReDim c(LOF(2) - 1)
Get #2, , c
Close #2
d = StrConv(c, vbUnicode)
d = Replace(d, pcip0, "192.168.1.205")
Open f2 For Output As #2
Print #2, d
Close #2
End If

f1 = "D:\oracle\ora92\network\admin\listener.ora"
Dim a() As Byte
If Dir(f1, vbDirectory) <> "" Then
Open f1 For Binary As #1
ReDim a(LOF(1) - 1)
Get #1, , a
Close #1
b = StrConv(a, vbUnicode)
b = Replace(b, pcname, "QD06")
b = Replace(b, pcname2, "QD06")
Open f1 For Output As #1
Print #1, b
Close #1



Set WshShell = CreateObject("WScript.Shell")
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName", "QD06", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\NV Hostname", "QD06", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\Hostname", "QD06", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\ControlSet001\Control\ComputerName\ComputerName\ComputerName", "QD06", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\AltDefaultDomainName", "QD06", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\DefaultDomainName", "QD06", "REG_SZ"
Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 192.168.1.205 255.255.0.0"), vbHide
waitforms (3)
pcname = WshShell.RegRead("HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName")
pcname2 = LCase(pcname)
Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 192.168.1.205 255.255.0.0"), vbHide
pcip1 = Winsock1.LocalIP
Label1.Caption = " IPC-NAME： " & pcname & "  IPC-IP：" & pcip1

MsgBox "Execution success！", vbOKOnly, "RESULT"
Else
MsgBox "Execution failure！", vbOKOnly, "RESULT"
End If

End Sub

Private Sub Command7_Click()
f2 = "D:\oracle\ora92\network\admin\tnsnames.ora"
Dim c() As Byte
If Dir(f2, vbDirectory) <> "" Then
Open f2 For Binary As #2
ReDim c(LOF(2) - 1)
Get #2, , c
Close #2
d = StrConv(c, vbUnicode)
d = Replace(d, pcip0, "10.11.16.4")
Open f2 For Output As #2
Print #2, d
Close #2
End If

f1 = "D:\oracle\ora92\network\admin\listener.ora"
Dim a() As Byte
If Dir(f1, vbDirectory) <> "" Then
Open f1 For Binary As #1
ReDim a(LOF(1) - 1)
Get #1, , a
Close #1
b = StrConv(a, vbUnicode)
b = Replace(b, pcname, "IPC04")
b = Replace(b, pcname2, "IPC04")
Open f1 For Output As #1
Print #1, b
Close #1



Set WshShell = CreateObject("WScript.Shell")
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName", "IPC04", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\NV Hostname", "IPC04", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\Hostname", "IPC04", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\ControlSet001\Control\ComputerName\ComputerName\ComputerName", "IPC04", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\AltDefaultDomainName", "IPC04", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\DefaultDomainName", "IPC04", "REG_SZ"
Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 11.10.16.8 255.255.0.0"), vbHide
waitforms (3)
pcname = WshShell.RegRead("HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName")
pcname2 = LCase(pcname)

pcip1 = Winsock1.LocalIP

Label1.Caption = " IPC-NAME： " & pcname & "  IPC-IP：" & pcip1

MsgBox "Back to IPC04 success！", vbOKOnly, "RESULT"
Else
MsgBox "Back to IPC04 failure！", vbOKOnly, "RESULT"
End If
End Sub

Private Sub Command8_Click()
f2 = "D:\oracle\ora92\network\admin\tnsnames.ora"
Dim c() As Byte
If Dir(f2, vbDirectory) <> "" Then
Open f2 For Binary As #2
ReDim c(LOF(2) - 1)
Get #2, , c
Close #2
d = StrConv(c, vbUnicode)
d = Replace(d, pcip0, "10.11.16.5")
Open f2 For Output As #2
Print #2, d
Close #2
End If

f1 = "D:\oracle\ora92\network\admin\listener.ora"
Dim a() As Byte
If Dir(f1, vbDirectory) <> "" Then
Open f1 For Binary As #1
ReDim a(LOF(1) - 1)
Get #1, , a
Close #1
b = StrConv(a, vbUnicode)
b = Replace(b, pcname, "IPC05")
b = Replace(b, pcname2, "IPC05")
Open f1 For Output As #1
Print #1, b
Close #1



Set WshShell = CreateObject("WScript.Shell")
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName", "IPC05", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\NV Hostname", "IPC05", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\Tcpip\Parameters\Hostname", "IPC05", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\System\ControlSet001\Control\ComputerName\ComputerName\ComputerName", "IPC05", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\AltDefaultDomainName", "IPC05", "REG_SZ"
WshShell.Regwrite "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\DefaultDomainName", "IPC05", "REG_SZ"
Shell ("cmd /c netsh interface ip set address name=""Eht1"" source=static 10.11.16.5 255.255.0.0"), vbHide
waitforms (3)
pcname = WshShell.RegRead("HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName")
pcname2 = LCase(pcname)

pcip1 = Winsock1.LocalIP
Label1.Caption = " IPC-NAME： " & pcname & "  IPC-IP：" & pcip1

MsgBox "Back to IPC05 success！", vbOKOnly, "RESULT"
Else
MsgBox "Back to IPC05 failure！", vbOKOnly, "RESULT"
End If
End Sub

Private Sub form_load()
Dim WshShell As Object
pcip1 = Winsock1.LocalIP
Set WshShell = CreateObject("WScript.Shell")
pcname = WshShell.RegRead("HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\ComputerName\ActiveComputerName\ComputerName")
pcname2 = LCase(pcname)



Label1.Caption = " IPC-NAME： " & pcname & "  IPC-IP：" & pcip1


End Sub

Private Sub form_resize()
On Error Resume Next
With Image1
.Top = Me.ScaleHeight - 1100


.Left = 0

.Width = Me.ScaleWidth
End With

End Sub


