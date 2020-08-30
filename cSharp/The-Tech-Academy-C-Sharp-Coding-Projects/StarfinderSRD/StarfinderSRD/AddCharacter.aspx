<%@ Page Title="" Language="C#" MasterPageFile="~/Site.Master" AutoEventWireup="true" CodeBehind="AddCharacter.aspx.cs" Inherits="StarfinderSRD.AddCharacter" %>
<asp:Content ID="Content1" ContentPlaceHolderID="MainContent" runat="server">
<asp:ValidationSummary runat="server" ShowModelStateErrors="true" />
<asp:FormView runat="server" ID="addCharacterForm"
    ItemType="StarfinderSRDModelBinding.Models.Character" 
    InsertMethod="addCharacterForm_InsertItem" DefaultMode="Insert"
    RenderOuterTable="false" OnItemInserted="addCharacterForm_ItemInserted">
    <InsertItemTemplate>
        <fieldset>
            <ol>
                <asp:DynamicEntity runat="server" Mode="Insert" />
            </ol>
            <asp:Button runat="server" Text="Create" CommandName="Insert" />
            <asp:Button runat="server" Text="Cancel" CausesValidation="false" OnClick="cancelButton_Click" />
        </fieldset>
    </InsertItemTemplate>
</asp:FormView>
</asp:Content>
