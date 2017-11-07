 <%@ Page Language="C#" AutoEventWireup="true" CodeFile="Webform.aspx.cs" Inherits="Webform" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div style="font-family:Arial">
        </div>
        <asp:FileUpload ID="FileUpload1" runat="server" Width="1028px" />
        <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="Upload" />
        <br />
    </form>
</body>
</html>
